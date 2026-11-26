/* Every paper and navigation link works without JavaScript. */
(() => {
  const search = document.getElementById('publication-search');
  if (!search) return;
  const papers = [...document.querySelectorAll('.publication')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const count = document.getElementById('publication-count');
  const empty = document.getElementById('publication-empty');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const contents = papers.map(paper => normalize(paper.textContent));
  let filter = 'all';
  function update() {
    const words = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    papers.forEach((paper, index) => {
      const matches = (filter === 'all' || paper.dataset.kind === filter) && words.every(word => contents[index].includes(word));
      paper.hidden = !matches;
      if (matches) visible += 1;
    });
    count.textContent = `${visible} ${visible === 1 ? 'publication' : 'publications'}`;
    empty.hidden = visible !== 0;
  }
  search.addEventListener('input', update);
  buttons.forEach(button => button.addEventListener('click', () => {
    filter = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    update();
  }));
  update();
})();
