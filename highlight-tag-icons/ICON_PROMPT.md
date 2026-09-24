# OK Beauty 하이라이트 태그 아이콘: 제작 리스트 + 프롬프트

기준 데이터: "OK Beauty 태그 그룹핑" 아티팩트의 태그 목록(CONCERN / SKIN / INGREDIENT 목록, 사용시간·사용빈도 값)과
"Highlight Tag Icon System" 아티팩트(현재 아이콘 41개)를 대조했습니다.

## 1. 제작 리스트 (총 46개: 기존 다시 그리기 38 · NEW 5 · RENAME 3)

상태 표시: **NEW** 아직 아이콘이 없음 · **RENAME** 아이콘은 있지만 태그 값 이름이 바뀜 · 표시 없음은 기존 아이콘 다시 그리기

### Concern: 피부 고민 (6)
| # | 파일명 | 라벨 | 모티프 제안 |
|---|---|---|---|
| 1 | concern-brightening | Brightening | 반짝임, 작은 해 |
| 2 | concern-hydration | Hydration | 물방울 |
| 3 | concern-firming | Firming | 위로 당겨 올라가는 곡선, 탄력 |
| 4 | concern-pore | Pore Care | 모공을 뜻하는 동심원이나 작은 점 |
| 5 | concern-blemish | Blemish | 방패 안에 점 하나 (트러블 케어) |
| 6 | concern-soothing | Soothing | 잔잔한 물결 |

### Skin Type: 피부 타입 (6)
| # | 파일명 | 라벨 | 모티프 제안 |
|---|---|---|---|
| 7 | skin-all | All Skin Types | 원 안에 체크, 또는 겹친 원 |
| 8 | skin-normal | Normal | **NEW** 균형 잡힌 원, 매끈한 표면 |
| 9 | skin-dry | Dry | 갈라진 물방울, 건조한 결 |
| 10 | skin-oily | Oily | 기름 방울, 유분 광택 |
| 11 | skin-combination | Combination | 반반 나뉜 물방울이나 원 |
| 12 | skin-sensitive | Sensitive | 하트, 또는 보호하는 손바닥 |

### Key Ingredient: 핵심 원료 (28)
| # | 파일명 | 라벨 | 모티프 제안 |
|---|---|---|---|
| 13 | ing-rice | Rice | 쌀알 한 톨 |
| 14 | ing-centella | Centella | 병풀 잎 (둥근 잎) |
| 15 | ing-niacinamide | Niacinamide | 육각 분자 |
| 16 | ing-hyaluronic-acid | Hyaluronic Acid | 물방울 안에 작은 점들 |
| 17 | ing-ceramide | Ceramide | 벽돌 쌓기 (장벽) |
| 18 | ing-vitamin-c | Vitamin C | 오렌지 단면 |
| 19 | ing-vitamin-e | Vitamin E | 캡슐 |
| 20 | ing-retinol | Retinol | 초승달 (나이트 케어) |
| 21 | ing-peptide | Peptide | 연결된 체인, 구슬 |
| 22 | ing-collagen | Collagen | 꼬인 섬유 가닥 |
| 23 | ing-pdrn | PDRN | DNA 이중나선 |
| 24 | ing-snail | Snail Mucin | 달팽이 |
| 25 | ing-squalane | Squalane | 올리브 방울 |
| 26 | ing-salicylic-acid | Salicylic Acid | 버드나무 잎 (BHA) |
| 27 | ing-glycolic-acid | Glycolic Acid | 사탕수수 줄기 (AHA) |
| 28 | ing-azelaic-acid | Azelaic Acid | 곡물 이삭 |
| 29 | ing-arbutin | Arbutin | 베어베리 열매 |
| 30 | ing-adenosine | Adenosine | 원자 궤도 |
| 31 | ing-aloe | Aloe | 알로에 잎 |
| 32 | ing-green-tea | Green Tea | 찻잎 |
| 33 | ing-ginseng | Ginseng | 인삼 뿌리 |
| 34 | ing-panthenol | Panthenol | 반으로 나뉜 잎 (B5, 진정) |
| 35 | ing-charcoal | Charcoal | 숯 조각 |
| 36 | ing-tea-tree | Tea Tree | 가는 잎이 달린 가지 |
| 37 | ing-propolis | Propolis | **NEW** 벌집 육각형 |
| 38 | ing-honey | Honey | **NEW** 꿀 디퍼, 꿀방울 |
| 39 | ing-shea-butter | Shea Butter | **NEW** 시어 열매, 크림 덩어리 |
| 40 | ing-caffeine | Caffeine | **NEW** 커피 원두 |

### Usage Time: 사용 시간 (3), 스킨케어 전용
| # | 파일명 | 라벨 | 모티프 제안 |
|---|---|---|---|
| 41 | time-day | Day | **RENAME** (기존 morning) 해 |
| 42 | time-night | Night | **RENAME** (기존 evening) 달 |
| 43 | time-allday | Allday | **RENAME** (기존 morning-evening) 해와 달 반반 |

### Usage Frequency: 사용 빈도 (3)
| # | 파일명 | 라벨 | 모티프 제안 |
|---|---|---|---|
| 44 | freq-daily | Daily | 달력에 체크 |
| 45 | freq-2-3-week | 2–3x / Week | 달력에 점 3개 |
| 46 | freq-1-2-week | 1–2x / Week | 달력에 점 1개 |

> 원료 NEW 4개(propolis, honey, shea-butter, caffeine)는 태그 목록에는 있지만 아직 붙은 상품이 0개입니다.
> 반대로 squalane, arbutin, adenosine, charcoal은 상품이 1개뿐입니다. 급하지 않다면 뒤로 미뤄도 됩니다.

---

## 2. 프롬프트 (Claude·ChatGPT 등 SVG를 코드로 만드는 AI용)

아래 블록을 그대로 복사해서 붙여 넣으세요. 한 번에 다 만들면 품질이 떨어지니 **카테고리별로 나눠서** 돌리는 걸 권장합니다.
`[ICON LIST]` 자리에 위 표에서 필요한 줄만 붙여 넣으면 됩니다.

```
You are an icon designer creating a cohesive line-icon set for "OK Beauty",
a K-beauty skincare e-commerce store. The icons appear inside small product
"highlight tag" chips on product pages (rendered at 12–22px), so they must
read clearly at tiny sizes.

STYLE (apply to every icon, no exceptions)
- Canvas: 24 × 24 viewBox, keep all strokes inside a 2px safe margin (live area 20 × 20).
- Outline only: fill="none", stroke="#16150F", stroke-width="1.6",
  stroke-linecap="round", stroke-linejoin="round".
- No fills, gradients, shadows, text, or letters. Small solid dots are allowed only as
  circles r ≤ 1.
- Minimal: 1–4 shapes per icon. Prefer simple geometric primitives (circle, path arcs).
- Friendly, soft, clean, slightly botanical: consistent with a calm premium skincare brand.
- Optical consistency: similar visual weight and size across the whole set; center each
  glyph optically.
- Every icon in a category should feel like a family (same metaphor style).

OUTPUT FORMAT
- For each icon, output one standalone SVG file in a separate code block, titled with its
  file name, e.g. `ing-propolis.svg`.
- Root element exactly:
  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
       fill="none" stroke="#16150F" stroke-width="1.6" stroke-linecap="round"
       stroke-linejoin="round">
- Use only <path>, <circle>, <line>, <rect>, <ellipse>, <polyline>. No <g transform>,
  no <style>, no ids, no comments. Round coordinates to 0.5.
- After all icons, add one line per icon explaining the metaphor in ≤ 10 words.

ICONS TO DRAW (file name | label | suggested motif)
[ICON LIST]
```

### 이미지 생성 AI(Midjourney, Firefly 등)를 쓸 때
SVG 코드가 아니라 그림을 받게 되니, 나중에 벡터로 따는 작업이 필요합니다.

```
minimal line icon set for a skincare brand, [ICON LIST 라벨만 쉼표로], thin uniform
1.5px rounded stroke, outline only, no fill, monochrome dark charcoal #16150F on white,
24px grid, consistent visual weight, soft botanical premium style, evenly spaced grid
layout, flat vector, no text --style raw
```

## 3. 받은 뒤 체크리스트
- [ ] 12px으로 줄여도 알아볼 수 있는가 (칩 안 크기)
- [ ] 선 두께 1.6, 끝과 모서리가 round인가
- [ ] 선이 외곽선 도형으로 바뀌지 않았는가 (굵기 일괄 조정 가능해야 함)
- [ ] 파일명이 위 표와 같은가 → 테마 스니펫 `product-highlight-tags.liquid` 에 넣을 때 그대로 매칭
