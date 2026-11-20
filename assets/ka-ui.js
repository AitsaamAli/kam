/* Kamboh Associates shared UI behaviour (Nov 2026). Progressive enhancement only: pages work without it. */
(function () {
  'use strict';
  var d = document;

  // One action bar on phones: mark floating WhatsApp/call buttons so CSS hides them under 768px,
  // and on wider screens keep only the first floating WhatsApp button.
  function markFloats() {
    if (!d.querySelector('.ka-mbar, .mobile-cta-bar')) return;
    if (d.querySelector('.ka-mbar')) d.body.classList.add('ka-has-mbar');
    var seen = false;
    var nodes = d.querySelectorAll('a[href*="wa.me"], a[href^="tel:"]');
    var done = [];
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (el.closest('.ka-mbar, .mobile-cta-bar, nav, header, footer, .topbar, .mobile-nav, .mn, #mn, [role="dialog"], [aria-modal]')) continue;
      var box = el, hit = null;
      for (var k = 0; k < 3 && box && box !== d.body; k++) {
        var cs = getComputedStyle(box);
        if (cs.position === 'fixed') {
          // floating buttons are small; menus and panels are not
          var w = parseFloat(cs.width), h = parseFloat(cs.height);
          if (w > 0 && w <= 140 && h > 0 && h <= 140) hit = box;
          break;
        }
        box = box.parentElement;
      }
      if (!hit || done.indexOf(hit) > -1) continue;
      done.push(hit);
      hit.classList.add('ka-float');
      var isWa = /wa\.me/.test(el.getAttribute('href') || '');
      if (isWa && !seen) { seen = true; } else { hit.classList.add('ka-float-extra'); }
    }
  }

  // Table of contents: closed by default on phones, current section highlighted, reading progress bar.
  function toc() {
    var box = d.querySelector('.ka-toc');
    if (!box) return;
    if (window.matchMedia('(max-width: 767px)').matches) box.removeAttribute('open');
    var links = box.querySelectorAll('a[href^="#"]');
    var map = {};
    var targets = [];
    for (var i = 0; i < links.length; i++) {
      var id = decodeURIComponent(links[i].getAttribute('href').slice(1));
      var h = d.getElementById(id);
      if (h) { map[id] = links[i]; targets.push(h); }
    }
    if ('IntersectionObserver' in window && targets.length) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) {
            for (var j = 0; j < links.length; j++) links[j].classList.remove('on');
            var a = map[e.target.id];
            if (a) a.classList.add('on');
          }
        });
      }, { rootMargin: '-80px 0px -70% 0px' });
      targets.forEach(function (t) { io.observe(t); });
    }
    var bar = d.createElement('div');
    bar.className = 'ka-progress';
    bar.setAttribute('aria-hidden', 'true');
    d.body.appendChild(bar);
    var ticking = false;
    function upd() {
      var h = d.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? Math.min(100, (h.scrollTop || d.body.scrollTop) / max * 100) : 0) + '%';
      ticking = false;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(upd); } }, { passive: true });
    upd();
  }

  function init() { try { markFloats(); } catch (e) {} try { toc(); } catch (e) {} }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init); else init();
})();
