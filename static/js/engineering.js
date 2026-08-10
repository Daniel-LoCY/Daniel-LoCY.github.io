(() => {
  const explorer = document.querySelector('[data-engineering-explorer]');
  if (!explorer) return;

  const cards = Array.from(explorer.querySelectorAll('[data-project-card]'));
  const sections = Array.from(explorer.querySelectorAll('[data-project-section]'));
  const searchInput = explorer.querySelector('[data-project-search]');
  const filters = Array.from(explorer.querySelectorAll('[data-project-filter]'));
  const resultCount = explorer.querySelector('[data-project-result-count]');
  const emptyState = explorer.querySelector('[data-project-empty]');
  const total = cards.length;
  let activeFilter = 'all';
  let query = '';

  const matches = (card) => {
    const matchesFilter = activeFilter === 'all' || card.dataset.category === activeFilter;
    const matchesQuery = !query || (card.dataset.search || '').includes(query);
    return matchesFilter && matchesQuery;
  };

  const render = () => {
    let visible = 0;

    cards.forEach((card) => {
      const visibleCard = matches(card);
      card.hidden = !visibleCard;
      if (visibleCard) visible += 1;
    });

    sections.forEach((section) => {
      const visibleCards = section.querySelectorAll('[data-project-card]:not([hidden])').length;
      section.hidden = visibleCards === 0;
    });

    if (resultCount) {
      const template = explorer.dataset.countTemplate || 'projects';
      resultCount.textContent = `${visible} / ${total} ${template}`;
    }
    if (emptyState) emptyState.hidden = visible !== 0;
  };

  filters.forEach((filter) => {
    filter.addEventListener('click', () => {
      activeFilter = filter.dataset.projectFilter || 'all';
      filters.forEach((item) => {
        const isActive = item === filter;
        item.classList.toggle('is-active', isActive);
        item.setAttribute('aria-pressed', String(isActive));
      });
      render();
    });
  });

  searchInput?.addEventListener('input', (event) => {
    query = event.target.value.trim().toLowerCase();
    render();
  });

  render();
})();
