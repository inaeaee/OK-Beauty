// 인쇄 전에 각 가격표의 글자 크기를 칸에 맞게 줄인다.
(function () {
  function shrink(el, fits, maxMm, minMm) {
    let size = maxMm;
    el.style.fontSize = size + 'mm';
    while (!fits(el) && size > minMm) {
      size = Math.max(minMm, +(size - 0.1).toFixed(2));
      el.style.fontSize = size + 'mm';
    }
    return fits(el);
  }

  document.querySelectorAll('.tag').forEach(function (tag) {
    // 제품명: 2줄 안에 들어갈 때까지 2.9mm → 2.3mm, 그래도 길면 말줄임(…)
    const product = tag.querySelector('.product');
    product.style.webkitLineClamp = 'unset';
    product.style.display = 'block';
    product.style.maxHeight = 'none';
    const twoLines = function (el) {
      return el.scrollHeight <= parseFloat(getComputedStyle(el).lineHeight) * 2 + 0.5;
    };
    const fitted = shrink(product, twoLines, 2.9, 2.3);
    product.style.display = '';
    product.style.maxHeight = '';
    product.style.webkitLineClamp = '';
    if (!fitted) tag.dataset.productClamped = '1';

    // 멤버십가: 가로 폭 안에 들어갈 때까지 16mm → 8mm
    const member = tag.querySelector('.member');
    const oneLine = function (el) { return el.scrollWidth <= el.clientWidth + 0.5; };
    if (!shrink(member, oneLine, 16, 8)) tag.dataset.memberOverflow = '1';

    // 기존가가 라벨과 겹치면 라벨을 줄인다
    const meta = tag.querySelector('.meta');
    if (meta.scrollWidth > meta.clientWidth + 0.5) {
      tag.querySelector('.label').textContent = 'MEMBER';
    }
  });
  document.body.dataset.fitted = '1';
})();
