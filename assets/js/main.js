// Menú móvil
(function () {
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('.nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      const open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
})();

// Desplegables del navbar por clic (no se abren automáticamente al pasar el cursor)
(function () {
  const parents = Array.from(document.querySelectorAll('.nav-menu .has-children > .nav-parent'));
  if (!parents.length) return;

  function closeAll(except) {
    parents.forEach(function (btn) {
      if (btn !== except) {
        btn.setAttribute('aria-expanded', 'false');
        btn.parentElement.classList.remove('open');
      }
    });
  }

  parents.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      const li = btn.parentElement;
      const isOpen = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      closeAll(btn);
    });
  });

  document.addEventListener('click', function () { closeAll(null); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAll(null);
  });
})();
