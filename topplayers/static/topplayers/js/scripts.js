/* ============================================================
   TOP PLAYERS · Copa do Mundo 2026 — Scripts Principal
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── REVEAL ON SCROLL ──────────────────────────────────────── */
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  /* ── EQUIPE — FILTER TABS ──────────────────────────────────── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  if (filterBtns.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // update active state
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.dataset.filter;

        document.querySelectorAll('.player-item').forEach(item => {
          const match = filter === 'all' || item.dataset.pos === filter;
          item.style.display = match ? '' : 'none';
        });
      });
    });
  }

});
