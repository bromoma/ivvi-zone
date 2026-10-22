document.documentElement.classList.add("js");

const header = document.querySelector(".header");
const menu = document.getElementById("menu");
const burger = document.getElementById("burger");

const setMenu = (open) => {
  menu.classList.toggle("is-open", open);
  burger.setAttribute("aria-expanded", String(open));
  burger.setAttribute("aria-label", open ? "Закрити меню" : "Відкрити меню");
  document.body.classList.toggle("is-locked", open);
};
burger.addEventListener("click", () => setMenu(!menu.classList.contains("is-open")));
menu.addEventListener("click", (e) => {
  if (e.target.closest("a")) setMenu(false);
});

document.querySelectorAll(".menu__drop").forEach((drop) => {
  const toggle = drop.querySelector(".menu__toggle");
  toggle.addEventListener("click", () => {
    const open = !drop.classList.contains("is-open");
    drop.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
  });
  document.addEventListener("click", (e) => {
    if (!drop.contains(e.target)) drop.classList.remove("is-open");
  });
});

const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

const animated = document.querySelectorAll(".anim");
const stagger = (el) => {
  const kind = [...el.classList].find((c) => c.startsWith("anim--"));
  const siblings = [...el.parentElement.children].filter((c) => c.classList.contains(kind));
  const index = siblings.indexOf(el);
  if (index > 0) el.style.setProperty("--d", `${Math.min(index, 5) * 0.12}s`);
};
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      stagger(entry.target);
      entry.target.classList.add("animate");
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.2 });
  animated.forEach((el) => observer.observe(el));
} else {
  animated.forEach((el) => el.classList.add("animate"));
}

const hero = document.querySelector("[data-hero]");
if (hero) {
  const slides = hero.querySelectorAll(".hero__slide");
  const dots = hero.querySelectorAll(".hero__dots button");
  let current = 0;
  let timer;
  const show = (i) => {
    current = (i + slides.length) % slides.length;
    slides.forEach((s, n) => s.classList.toggle("is-active", n === current));
    dots.forEach((d, n) => d.classList.toggle("is-active", n === current));
  };
  const play = () => {
    clearInterval(timer);
    timer = setInterval(() => show(current + 1), 6500);
  };
  dots.forEach((dot, i) => dot.addEventListener("click", () => { show(i); play(); }));
  play();
}

document.querySelectorAll("[data-slider]").forEach((slider) => {
  const track = slider.querySelector(".slider__track");
  const slides = slider.querySelectorAll(".slider__slide");
  const dotsBox = slider.querySelector(".slider__dots");
  const [prev, next] = slider.querySelectorAll(".slider__arrow");
  const maxPerView = Number(slider.dataset.perView) || 3;
  let index = 0;
  let timer;

  const perView = () => {
    if (window.innerWidth < 640) return 1;
    if (window.innerWidth < 1024) return Math.min(2, maxPerView);
    return maxPerView;
  };
  const pages = () => Math.max(1, slides.length - perView() + 1);

  const render = () => {
    const pv = perView();
    slider.style.setProperty("--pv", pv);
    index = Math.min(index, pages() - 1);
    track.style.transform = `translateX(${-(100 / pv) * index}%)`;
    dotsBox.querySelectorAll("button").forEach((d, i) => d.classList.toggle("is-active", i === index));
  };
  const buildDots = () => {
    dotsBox.innerHTML = "";
    for (let i = 0; i < pages(); i++) {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", `Слайд ${i + 1}`);
      dot.addEventListener("click", () => go(i));
      dotsBox.append(dot);
    }
    render();
  };
  const go = (i) => {
    const total = pages();
    index = (i + total) % total;
    render();
    autoplay();
  };
  const autoplay = () => {
    clearInterval(timer);
    timer = setInterval(() => go(index + 1), 5000);
  };

  prev.addEventListener("click", () => go(index - 1));
  next.addEventListener("click", () => go(index + 1));
  slider.addEventListener("mouseenter", () => clearInterval(timer));
  slider.addEventListener("mouseleave", autoplay);

  let startX = null;
  slider.addEventListener("touchstart", (e) => { startX = e.touches[0].clientX; }, { passive: true });
  slider.addEventListener("touchend", (e) => {
    if (startX === null) return;
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 40) go(index + (dx < 0 ? 1 : -1));
    startX = null;
  });

  window.addEventListener("resize", buildDots);
  buildDots();
  autoplay();
});

const filters = document.querySelectorAll(".filter");
const slots = document.querySelectorAll(".slot");
const applyFilter = (type) => {
  filters.forEach((b) => b.classList.toggle("is-active", b.dataset.filter === type));
  slots.forEach((slot) => {
    const match = type === "all" || slot.dataset.type.split(" ").includes(type);
    slot.classList.toggle("is-dim", !match);
  });
};
filters.forEach((btn) => btn.addEventListener("click", () => applyFilter(btn.dataset.filter)));
const initialFilter = new URLSearchParams(location.search).get("f");
if (filters.length && initialFilter) applyFilter(initialFilter);

const modal = document.getElementById("modal");
const form = modal.querySelector("[data-form]");
const direction = form.querySelector("[data-direction]");
const age = form.querySelector("[data-age]");
const status = form.querySelector(".form__status");
let lastFocus = null;

const syncAge = () => {
  age.hidden = !/дитин/i.test(direction.value);
};
const openModal = (preset) => {
  lastFocus = document.activeElement;
  if (preset) direction.value = preset;
  syncAge();
  status.textContent = "";
  modal.hidden = false;
  document.body.classList.add("is-locked");
  form.elements.name.focus();
};
const closeModal = () => {
  modal.hidden = true;
  if (!menu.classList.contains("is-open")) document.body.classList.remove("is-locked");
  if (lastFocus) lastFocus.focus();
};

const presetFromPage = () => {
  const page = location.pathname.split("/").pop();
  return {
    "pilates.html": "Пілатес",
    "stretching.html": "Стретчинг",
    "barre.html": "Барре",
    "choreography.html": "Хореографія для дитини",
    "mama.html": "Мама + дитина",
  }[page];
};

document.addEventListener("click", (e) => {
  const opener = e.target.closest("[data-modal-open]");
  if (opener) {
    e.preventDefault();
    openModal(opener.dataset.directionValue || presetFromPage());
  }
  if (e.target.closest("[data-modal-close]")) closeModal();
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !modal.hidden) closeModal();
});
direction.addEventListener("change", syncAge);

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = form.elements.name;
  const phone = form.elements.phone;
  const nameOk = name.value.trim().length > 0;
  const phoneOk = phone.value.replace(/\D/g, "").length >= 10;
  name.classList.toggle("is-invalid", !nameOk);
  phone.classList.toggle("is-invalid", !phoneOk);
  if (!nameOk || !phoneOk) {
    status.textContent = "Вкажіть, будь ласка, ім’я та номер телефону.";
    return;
  }
  status.textContent = `Дякуємо, ${name.value.trim()}! Ми зателефонуємо найближчим часом 💜`;
  form.reset();
  syncAge();
});

document.querySelectorAll("[data-year]").forEach((el) => { el.textContent = new Date().getFullYear(); });
