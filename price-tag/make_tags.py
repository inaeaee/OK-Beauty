#!/usr/bin/env python3
"""OK Beauty 가격표(70×40mm, 가격 강조형) 생성기.

엑셀의 제품명·브랜드명·기존가·멤버십가·수량·통화를 읽어
A4 인쇄용 HTML과 PDF(실치수)를 만든다.

  python3 make_tags.py 가격표.xlsx -o out/가격표.pdf
"""
import argparse
import base64
import html
import json
import re
import subprocess
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent

# 엑셀 머리글 → 내부 필드 (한글/영문 모두 허용, 공백·대소문자 무시)
HEADERS = {
    "product": ["제품명", "상품명", "product", "productname", "name"],
    "brand": ["브랜드명", "브랜드", "brand", "brandname"],
    "regular": ["기존가", "정가", "정상가", "regular", "regularprice", "rrp", "price"],
    "member": ["멤버십가", "멤버십가격", "회원가", "member", "memberprice", "membershipprice"],
    "qty": ["수량", "qty", "quantity", "count"],
    "currency": ["통화", "currency"],
}
REQUIRED = ["product", "brand", "member"]

CURRENCY_SYMBOLS = {
    "AUD": "$", "USD": "$", "NZD": "$", "CAD": "$", "SGD": "$", "HKD": "$",
    "KRW": "₩", "JPY": "¥", "CNY": "¥", "EUR": "€", "GBP": "£",
}
ZERO_DECIMAL = {"KRW", "JPY"}


def norm(s):
    return re.sub(r"[\s_\-()/]", "", str(s or "")).lower()


def slug(s):
    return re.sub(r"[^a-z0-9가-힣]+", "-", str(s).strip().lower()).strip("-")


def to_decimal(v):
    if v is None or str(v).strip() == "":
        return None
    try:
        return Decimal(re.sub(r"[^\d.\-]", "", str(v)))
    except InvalidOperation:
        return None


def read_rows(xlsx, sheet=None):
    wb = openpyxl.load_workbook(xlsx, data_only=True, read_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    rows = ws.iter_rows(values_only=True)
    header = next(rows)
    col = {}
    for i, h in enumerate(header):
        for field, names in HEADERS.items():
            if norm(h) in names and field not in col:
                col[field] = i
    missing = [f for f in REQUIRED if f not in col]
    if missing:
        sys.exit(f"엑셀 머리글을 찾지 못했습니다: {', '.join(HEADERS[f][0] for f in missing)} (현재 머리글: {list(header)})")

    items, problems = [], []
    for n, r in enumerate(rows, start=2):
        get = lambda f: r[col[f]] if f in col and col[f] < len(r) else None
        if not any(v not in (None, "") for v in r):
            continue
        product = str(get("product") or "").strip()
        brand = str(get("brand") or "").strip()
        member = to_decimal(get("member"))
        regular = to_decimal(get("regular"))
        qty_dec = to_decimal(get("qty"))
        qty = 1 if qty_dec is None else int(qty_dec)  # 수량 칸이 비면 1장, 0이면 출력 안 함
        currency = str(get("currency") or "AUD").strip().upper()
        if not product or member is None:
            problems.append(f"{n}행: 제품명 또는 멤버십가가 비어 있어 건너뜀")
            continue
        if regular is not None and regular <= member:
            problems.append(f"{n}행: 기존가({regular})가 멤버십가({member})보다 크지 않아 기존가를 표시하지 않음")
            regular = None
        items.append(dict(row=n, product=product, brand=brand, member=member,
                          regular=regular, qty=max(qty, 0), currency=currency))
    return items, problems


def fmt_price(value, currency):
    sym = CURRENCY_SYMBOLS.get(currency, currency + " ")
    if currency in ZERO_DECIMAL:
        whole, dec = f"{int(value.quantize(Decimal('1'), ROUND_HALF_UP)):,}", ""
    else:
        q = value.quantize(Decimal("0.01"), ROUND_HALF_UP)
        whole, dec = f"{int(q):,}", "." + f"{q:.2f}".split(".")[1]
    return sym, whole, dec


def find_logo(brand, logo_dir):
    s = slug(brand)
    for ext in ("svg", "png", "jpg", "jpeg", "webp"):
        p = logo_dir / f"{s}.{ext}"
        if p.exists():
            return p
    return None


def logo_html(brand, logo_dir, cache, missing):
    if brand not in cache:
        p = find_logo(brand, logo_dir)
        if p is None:
            missing.add(brand)
            cache[brand] = f'<span class="brand-text">{html.escape(brand)}</span>'
        else:
            mime = {"svg": "image/svg+xml", "png": "image/png", "webp": "image/webp"}.get(p.suffix[1:].lower(), "image/jpeg")
            data = base64.b64encode(p.read_bytes()).decode()
            cache[brand] = f'<img src="data:{mime};base64,{data}" alt="{html.escape(brand)}">'
    return cache[brand]


def tag_html(it, logo):
    sym, whole, dec = fmt_price(it["member"], it["currency"])
    regular = ""
    if it["regular"] is not None:
        rs, rw, rd = fmt_price(it["regular"], it["currency"])
        regular = f'<span class="regular">{html.escape(rs + rw + rd)}</span>'
    member = (f'<span class="cur">{html.escape(sym.strip())}</span>{whole}'
              + (f'<span class="dec">{dec}</span>' if dec else ""))
    return (f'<div class="tag" data-row="{it["row"]}">'
            f'<div class="logo">{logo}</div>'
            f'<div class="product">{html.escape(it["product"])}</div>'
            f'<div class="prices"><div class="meta"><span class="label">MEMBER PRICE</span>{regular}</div>'
            f'<div class="member">{member}</div></div></div>')


def build_html(items, logo_dir, cols, rows, gap_mm, cutlines):
    cache, missing = {}, set()
    tags = [tag_html(it, logo_html(it["brand"], logo_dir, cache, missing))
            for it in items for _ in range(it["qty"])]
    per = cols * rows
    sheets = ["".join(tags[i:i + per]) for i in range(0, len(tags), per)] or [""]
    css = (HERE / "tag.css").read_text(encoding="utf-8")
    js = (HERE / "fit.js").read_text(encoding="utf-8")
    top = (297 - rows * 40 - (rows - 1) * gap_mm) / 2
    body = "".join(
        f'<section class="sheet" style="--cols:{cols};--gap:{gap_mm}mm;--top:{top}mm">{s}</section>' for s in sheets)
    doc = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>OK Beauty 가격표</title>'
           f'<style>{css}</style></head><body class="{"cutlines" if cutlines else ""}">{body}'
           f'<script>{js}</script></body></html>')
    return doc, len(tags), len(sheets), sorted(missing)


def main():
    ap = argparse.ArgumentParser(description="OK Beauty 70×40mm 가격표 → A4 PDF")
    ap.add_argument("xlsx")
    ap.add_argument("-o", "--out", default="가격표.pdf")
    ap.add_argument("--sheet")
    ap.add_argument("--logos", default=str(HERE / "logos"), help="브랜드 로고 폴더 (파일명 = 브랜드명, 예: anua.svg)")
    ap.add_argument("--cols", type=int, default=2)
    ap.add_argument("--rows", type=int, default=7)
    ap.add_argument("--gap", type=float, default=0, help="가격표 사이 간격(mm)")
    ap.add_argument("--no-cutlines", action="store_true", help="재단선(점선) 숨기기")
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()

    if a.cols * 70 + (a.cols - 1) * a.gap > 210 or a.rows * 40 + (a.rows - 1) * a.gap > 297:
        sys.exit(f"{a.cols}열×{a.rows}행(간격 {a.gap}mm)은 A4(210×297mm)에 들어가지 않습니다.")

    items, problems = read_rows(a.xlsx, a.sheet)
    doc, n_tags, n_pages, missing = build_html(items, Path(a.logos), a.cols, a.rows, a.gap, not a.no_cutlines)

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    html_path = out.with_suffix(".html")
    html_path.write_text(doc, encoding="utf-8")

    report = {"products": len(items), "tags": n_tags, "pages": n_pages, "html": str(html_path)}
    if not a.html_only:
        res = subprocess.run(["node", str(HERE / "render_pdf.js"), str(html_path), str(out)],
                             capture_output=True, text=True)
        if res.returncode != 0:
            sys.exit("PDF 생성 실패:\n" + res.stderr)
        report.update(json.loads(res.stdout))
    for p in problems:
        print("주의:", p)
    if missing:
        print("로고 파일 없음(브랜드명 글자로 대신 표시):", ", ".join(missing),
              f"→ {a.logos}/<브랜드명>.svg 로 추가하세요")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
