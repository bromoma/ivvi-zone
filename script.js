const header = document.querySelector(".header");
const nav = document.getElementById("nav");
const burger = document.getElementById("burger");

const setMenu = (open) => {
  nav.classList.toggle("is-open", open);
  burger.setAttribute("aria-expanded", String(open));
  burger.setAttribute("aria-label", open ? "Закрити меню" : "Відкрити меню");
};

burger.addEventListener("click", () => setMenu(!nav.classList.contains("is-open")));
nav.addEventListener("click", (e) => {
  if (e.target.closest("a")) setMenu(false);
});

const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

const revealTargets = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-visible");
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  revealTargets.forEach((el) => observer.observe(el));
} else {
  revealTargets.forEach((el) => el.classList.add("is-visible"));
}

const filters = document.querySelectorAll(".filter");
const slots = document.querySelectorAll(".slot");
filters.forEach((btn) => {
  btn.addEventListener("click", () => {
    const type = btn.dataset.filter;
    filters.forEach((b) => b.classList.toggle("is-active", b === btn));
    slots.forEach((slot) => {
      const match = type === "all" || slot.dataset.type.split(" ").includes(type);
      slot.classList.toggle("is-dim", !match);
    });
  });
});

const form = document.getElementById("signup-form");
const direction = document.getElementById("direction");
const ageField = form.querySelector(".form__age");
const status = form.querySelector(".form__status");

const syncAge = () => {
  ageField.hidden = !/дитин/i.test(direction.value);
};
direction.addEventListener("change", syncAge);

document.querySelectorAll("[data-direction]").forEach((link) => {
  link.addEventListener("click", () => {
    const wanted = link.dataset.direction;
    const option = [...direction.options].find((o) => o.value.startsWith(wanted));
    if (option) direction.value = option.value;
    syncAge();
  });
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = form.elements.name;
  const phone = form.elements.phone;
  const phoneOk = phone.value.replace(/\D/g, "").length >= 10;
  name.classList.toggle("is-invalid", !name.value.trim());
  phone.classList.toggle("is-invalid", !phoneOk);
  if (!name.value.trim() || !phoneOk) {
    status.textContent = "Будь ласка, вкажіть ім’я та номер телефону.";
    return;
  }
  status.textContent = `Дякуємо, ${name.value.trim()}! Ми зателефонуємо вам найближчим часом 💜`;
  form.reset();
  syncAge();
});

document.getElementById("year").textContent = new Date().getFullYear();
