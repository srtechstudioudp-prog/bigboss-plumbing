(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // mobile menu
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // spirit level in the hero: the bubble follows the pointer, then settles back to level
  var level = document.querySelector('.level');
  if (level) {
    var vial = level.querySelector('.vial');
    var bubble = level.querySelector('.bubble');
    var out = level.querySelector('[data-angle]');
    var box = level.querySelector('.readout');
    var pos = reduce ? 0 : -0.9, vel = 0, target = 0, raf = null;

    function travel() { return Math.max(0, vial.clientWidth / 2 - bubble.offsetWidth / 2 - 6); }
    function paint() {
      var angle = pos * 2.4;
      bubble.style.setProperty('--bx', (pos * travel()).toFixed(1) + 'px');
      var s = Math.abs(angle) < 0.05 ? '0.00' : (angle > 0 ? '+' : '-') + Math.abs(angle).toFixed(2);
      out.textContent = s + '°';
      box.classList.toggle('is-level', Math.abs(angle) < 0.12);
      box.querySelector('em').textContent = Math.abs(angle) < 0.12 ? 'LEVEL' : 'OFF LEVEL';
    }
    function step() {
      var k = 0.045, damp = 0.9;
      vel = (vel + (target - pos) * k) * damp;
      pos += vel;
      paint();
      if (Math.abs(vel) > 0.0004 || Math.abs(target - pos) > 0.002) { raf = requestAnimationFrame(step); }
      else { pos = target; paint(); raf = null; }
    }
    function kick() { if (!raf) { raf = requestAnimationFrame(step); } }

    paint();
    if (!reduce) { setTimeout(kick, 500); }

    var hero = level.closest('.hero') || level;
    function move(e) {
      if (reduce) return;
      var r = vial.getBoundingClientRect();
      var x = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
      target = Math.max(-1, Math.min(1, x));
      kick();
    }
    hero.addEventListener('pointermove', move);
    hero.addEventListener('pointerleave', function () { target = 0; kick(); });
    window.addEventListener('resize', paint);
  }

  // demo-mode form: nothing is sent anywhere
  var modal = document.createElement('div');
  modal.className = 'demo-modal';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  modal.setAttribute('aria-label', 'Demo mode');
  modal.innerHTML =
    '<div class="demo-box">' +
    '<span class="demo-tag">DEMO MODE</span>' +
    '<h3>Nothing was sent</h3>' +
    '<p>On the live site, this request goes straight to <b>(832) 659-7540</b> and the company email.</p>' +
    '<button type="button" class="btn btn-ink">Back to the preview</button>' +
    '</div>';
  document.body.appendChild(modal);
  function close() { modal.classList.remove('show'); }
  modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
  modal.querySelector('button').addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

  document.querySelectorAll('form[data-demo]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      modal.classList.add('show');
      modal.querySelector('button').focus();
      form.reset();
    });
  });
})();
