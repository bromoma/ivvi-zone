from pathlib import Path

ROOT = Path(__file__).parent

ADDRESS = "м. Львів, вул. Стрийська, 45, LAZ"
MAP_QUERY = "Львів, вул. Стрийська, 45"
PHONE = "+380 __ ___ __ __"
INSTAGRAM = "#"
TELEGRAM = "#"

PHOTO = {
    "reformer_arch": "1747239685045-fcbcf98985db",
    "reformer_leg": "1747239069226-55382c570116",
    "reformer_pink": "1788463127138-d17920230de9",
    "studio": "1783841193384-4269c68aa050",
    "reformer_stand": "1747239202356-764770773c9a",
    "reformer_split": "1747238415033-b74eec07eb59",
    "reformer_duo": "1788463127084-9569ff96efbd",
    "mat_group": "1761035005546-62b8018b212a",
    "mat_boat": "1767611126399-830f9e6ee0d8",
    "stretch_arms": "1552196527-bffef41ef674",
    "stretch_leg": "1758599879024-7379d769f664",
    "pilates_ring": "1593431763017-c689a61b729a",
    "stretch_split": "1640262653851-103cbaf802d5",
    "barre_studio": "1779617926288-fde3f7fb7b5d",
    "barre_coach": "1770012905139-713758ded6ec",
    "barre_group": "1518310952931-b1de897abd40",
    "ballet_stage": "1508807526345-15e9b5f4eaff",
    "ballet_feet": "1677603142061-d19e9cbd5e4f",
    "ballet_class": "1685339009948-d807094b1457",
    "ballet_little": "1681312206210-5f52c564d30d",
    "ballet_show": "1558905566-ddbeb2fc2c2f",
    "mom_kid_1": "1714646793234-9e58a9ccfddb",
    "mom_kid_2": "1714646793438-dd6f16aa36d1",
    "mom_kid_3": "1714646793467-3f2b81d8fe1f",
    "mom_kid_4": "1714646793535-687207edbd0f",
}


def img(key, w=1200):
    return f"https://images.unsplash.com/photo-{PHOTO[key]}?auto=format&fit=crop&w={w}&q=70"


ICON = {
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></svg>',
    "telegram": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.5 4.2 2.9 11.4c-1 .4-1 1.1-.2 1.4l4.8 1.5 1.8 5.6c.2.6.4.8.9.8.4 0 .6-.2.9-.4l2.3-2.2 4.7 3.5c.9.5 1.5.2 1.7-.8l3.1-14.6c.3-1.3-.5-1.9-1.4-1.5ZM8.4 14l9.3-5.9c.5-.3.9-.1.5.2l-7.6 6.9-.3 3.2L8.4 14Z" fill="currentColor"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z" fill="currentColor"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5Z" fill="currentColor"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h16a1 1 0 0 1 1 1v11a1 1 0 0 1-1 1H8l-4 4V5a1 1 0 0 1 1-1Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M8 9h8M8 12.5h5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="8" cy="14.5" r="1.2" fill="currentColor"/><circle cx="12" cy="14.5" r="1.2" fill="currentColor"/><circle cx="16" cy="14.5" r="1.2" fill="currentColor"/></svg>',
    "form": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 8h8M8 12h8M8 16h4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "sparkle": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0C12.9 7.6 16.4 11.1 24 12C16.4 12.9 12.9 16.4 12 24C11.1 16.4 7.6 12.9 0 12C7.6 11.1 11.1 7.6 12 0Z" fill="currentColor"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 5 7 7-7 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "chevron": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "play": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',
}

ADULT_LINKS = [("pilates.html", "Пілатес"), ("stretching.html", "Стретчинг"), ("barre.html", "Барре")]
KID_LINKS = [("choreography.html", "Хореографія 4–12 років"), ("mama.html", "Мама + дитина")]


def socials(cls=""):
    return f"""<div class="socials {cls}">
      <a href="{INSTAGRAM}" aria-label="Instagram">{ICON['instagram']}</a>
      <a href="{TELEGRAM}" aria-label="Telegram">{ICON['telegram']}</a>
    </div>"""


def header(active):
    def item(href, label, key):
        cls = ' class="is-current"' if key == active else ""
        return f'<li><a href="{href}"{cls}>{label}</a></li>'

    adult = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in ADULT_LINKS)
    kids = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in KID_LINKS)
    train_cls = " is-current" if active in ("pilates", "stretching", "barre", "choreography") else ""
    return f"""<header class="header" id="top">
  <div class="container header__inner">
    <a class="logo" href="index.html" aria-label="IVVI Zone — на головну">
      <img src="assets/mark-pink.webp" alt="" width="46" height="45">
      <span class="logo__text">IVVI<small>zone</small></span>
    </a>
    <nav class="menu" id="menu" aria-label="Головне меню">
      <ul class="menu__list">
        {item("index.html#about", "Про нас", "about")}
        <li class="menu__drop">
          <button class="menu__toggle{train_cls}" type="button" aria-expanded="false">Тренування {ICON['chevron']}</button>
          <div class="dropdown">
            <div><p class="dropdown__title">Дорослим</p><ul>{adult}</ul></div>
            <div><p class="dropdown__title">Дітям</p><ul>{kids}</ul></div>
          </div>
        </li>
        {item("mama.html", "Мама + дитина", "mama")}
        {item("schedule.html", "Розклад", "schedule")}
        {item("contacts.html", "Контакти", "contacts")}
      </ul>
      <div class="menu__side">
        {socials()}
        <a class="header__phone" href="contacts.html">{PHONE}</a>
        <a class="btn btn--pink" href="schedule.html">Розклад</a>
      </div>
    </nav>
    <button class="burger" id="burger" type="button" aria-label="Відкрити меню" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  </div>
</header>"""


def footer():
    adult = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in ADULT_LINKS)
    kids = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in KID_LINKS)
    return f"""<footer class="footer">
  <div class="container footer__grid">
    <div class="footer__about">
      <a class="logo logo--light" href="index.html"><img src="assets/mark-pink.webp" alt="" width="46" height="45"><span class="logo__text">IVVI<small>zone</small></span></a>
      <p>Студія пілатесу, стретчингу та барре у Львові. Наша фішка — тренування для мам і хореографія для дітей в один час.</p>
      {socials("socials--light")}
    </div>
    <div>
      <h3>Навігація</h3>
      <ul>
        <li><a href="index.html">Головна</a></li>
        <li><a href="index.html#about">Про нас</a></li>
        <li><a href="schedule.html">Розклад</a></li>
        <li><a href="contacts.html">Контакти</a></li>
      </ul>
    </div>
    <div><h3>Для дорослих</h3><ul>{adult}</ul></div>
    <div><h3>Для дітей</h3><ul>{kids}</ul></div>
    <div class="footer__contacts">
      <h3>Контакти</h3>
      <p class="footer__line">{ICON['pin']}<span>{ADDRESS}</span></p>
      <p class="footer__line">{ICON['phone']}<span class="placeholder">{PHONE}</span></p>
      <p class="footer__line">{ICON['instagram']}<span class="placeholder">@instagram</span></p>
    </div>
  </div>
  <div class="container footer__bottom">
    <span>© <span data-year>2026</span> IVVI Zone. Усі права захищені</span>
    <span>Pilates · Barre · Stretching · Dance</span>
  </div>
</footer>"""


def modal():
    options = "".join(f"<option>{t}</option>" for t in ["Пілатес", "Стретчинг", "Барре", "Хореографія для дитини", "Мама + дитина", "Індивідуальне тренування"])
    return f"""<button class="callback" type="button" data-modal-open aria-label="Записатися на тренування">
  <span class="callback__ring"></span>{ICON['phone']}
</button>
<div class="modal" id="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden>
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__box">
    <button class="modal__close" type="button" data-modal-close aria-label="Закрити">×</button>
    <h2 id="modal-title">Запис на тренування</h2>
    <p>Залиште контакти — адміністратор зателефонує, підбере зручний час і відповість на питання.</p>
    <form class="form" data-form novalidate>
      <input name="name" type="text" placeholder="Ваше ім’я" autocomplete="given-name" required>
      <input name="phone" type="tel" placeholder="+380" autocomplete="tel" required>
      <select name="direction" data-direction>{options}</select>
      <input name="age" type="number" min="3" max="14" placeholder="Вік дитини" data-age hidden>
      <button class="btn btn--pink btn--wide" type="submit">Хочу на тренування</button>
      <p class="form__status" role="status" aria-live="polite"></p>
    </form>
  </div>
</div>"""


def page(filename, title, description, body, active=None):
    html = f"""<!doctype html>
<html lang="uk">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#2f1d38">
  <link rel="icon" type="image/png" href="assets/favicon.png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
{header(active)}
<main>
{body}
</main>
{footer()}
{modal()}
<script src="script.js"></script>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


def watermark(text="IVVI ZONE"):
    return f'<span class="watermark" aria-hidden="true">{text}</span>'


def slider(items, cls, per_view=3):
    slides = "".join(f'<div class="slider__slide">{i}</div>' for i in items)
    return f"""<div class="slider {cls}" data-slider data-per-view="{per_view}">
  <div class="slider__viewport"><div class="slider__track">{slides}</div></div>
  <div class="slider__nav">
    <button class="slider__arrow slider__arrow--prev" type="button" aria-label="Назад">{ICON['arrow']}</button>
    <div class="slider__dots"></div>
    <button class="slider__arrow" type="button" aria-label="Далі">{ICON['arrow']}</button>
  </div>
</div>"""


ADVANTAGES = [
    ("Малі групи", "До 8 людей на занятті — тренер бачить кожну, поправляє техніку й підбирає навантаження."),
    ("Мама + дитина", "Пілатес для мами й хореографія для дитини в один час у сусідніх залах. Без няні й чекання."),
    ("Будь-який рівень", "Можна прийти з нуля, після пологів чи довгої перерви — є варіанти вправ для кожної."),
    ("Безпека", "Плавні контрольовані рухи без ударного навантаження: бережемо спину, коліна та суглоби."),
    ("Затишна студія", "Світлі зали, ніжна музика, без поспіху. Сюди хочеться повертатися."),
]


def advantages_block(items=ADVANTAGES, slide=True):
    cards = [f'<article class="adv"><h3>{t}</h3><p>{d}</p></article>' for t, d in items]
    inner = slider(cards, "slider--dark") if slide else f'<div class="adv-grid">{"".join(cards)}</div>'
    return f"""<section class="section section--dark section--tight">
  <div class="container">{inner}</div>
</section>"""


def service_card(href, title, photo, badge=None, sub=None):
    badge_html = f'<span class="service__badge">{badge}</span>' if badge else ""
    sub_html = f"<span class=\"service__sub\">{sub}</span>" if sub else ""
    return f"""<a class="service anim anim--flip" href="{href}">
  <span class="service__bg" style="background-image:url('{img(photo, 900)}')"></span>
  {badge_html}
  <span class="service__body"><span class="service__title">{title}</span>{sub_html}<span class="btn btn--pink btn--sm">Детальніше</span></span>
</a>"""


def info_box(title, bullets):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<div class="info-box anim anim--left">
  <h2>{title}</h2>
  <ul class="bullets">{lis}</ul>
  {watermark("IVVI")}
</div>"""


def trial_block():
    return f"""<section class="trial">
  <div class="container trial__inner">
    <div class="trial__text anim anim--tilt">
      <h2>Пробне тренування</h2>
      <p>Відчуйте IVVI Zone на собі — перше заняття допоможе обрати напрямок і рівень.</p>
    </div>
    <button class="btn btn--dark btn--beat anim" type="button" data-modal-open>Хочу на тренування</button>
  </div>
</section>"""


REVIEWS = [
    ("Ім’я клієнтки", "Пілатес", "Тут буде реальний відгук з Instagram або Google Maps. Додамо, щойно студія збере перші відгуки."),
    ("Ім’я клієнтки", "Мама + дитина", "Тут буде реальний відгук мами, яка ходить на пілатес разом із дитиною на хореографію."),
    ("Ім’я клієнтки", "Стретчинг", "Тут буде реальний відгук про стретчинг. Можна додати фото або коротке відео."),
    ("Ім’я клієнтки", "Хореографія", "Тут буде реальний відгук батьків про дитячу хореографію."),
]


def reviews_block():
    cards = [f"""<article class="review">
  <div class="review__head"><span class="review__avatar">{ICON['sparkle']}</span><div><b>{n}</b><span>{d}</span></div></div>
  <p>{t}</p>
</article>""" for n, d, t in REVIEWS]
    return f"""<section class="section section--dark">
  {watermark()}
  <div class="container">
    <div class="section__head section__head--row">
      <h2>Що кажуть про наші тренування</h2>
    </div>
    {slider(cards, "slider--dark slider--reviews", 2)}
    <a class="btn btn--outline-pink" href="{INSTAGRAM}">Залишити відгук</a>
  </div>
</section>"""


def insta_block():
    keys = ["reformer_pink", "stretch_split", "ballet_little", "barre_group", "pilates_ring", "mat_group"]
    tiles = "".join(f'<a class="insta__tile" href="{INSTAGRAM}" style="background-image:url(\'{img(k, 500)}\')"><span>{ICON["instagram"]}Ми в Instagram</span></a>' for k in keys)
    return f'<section class="insta" aria-label="Instagram">{tiles}</section>'


def page_hero(crumbs, title, photo, buttons=True, sub=None):
    crumb_html = " / ".join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for h, t in crumbs)
    sub_html = f'<p class="page-hero__sub">{sub}</p>' if sub else ""
    btns = f"""<div class="page-hero__actions">
        <a class="btn btn--pink" href="schedule.html">Розклад</a>
        <a class="btn btn--outline-light" href="#more">Детальніше</a>
      </div>""" if buttons else ""
    return f"""<section class="page-hero">
  <div class="page-hero__bg" style="background-image:url('{img(photo, 1800)}')"></div>
  <div class="container page-hero__inner">
    <nav class="crumbs" aria-label="Навігація">{crumb_html}</nav>
    <h1>{title}</h1>
    {sub_html}
    {btns}
  </div>
  <button class="page-hero__play" type="button" data-modal-open aria-label="Записатися">{ICON['play']}</button>
</section>"""


def about_split(title, paragraphs, photos, button=True, dark=False, anchor=None):
    ps = "".join(f"<p>{p}</p>" for p in paragraphs)
    btn = '<button class="btn btn--dark" type="button" data-modal-open>Потрібна консультація</button>' if button else ""
    anchor_attr = f' id="{anchor}"' if anchor else ""
    cls = "section--dark" if dark else "section--pink"
    return f"""<section class="section {cls} about"{anchor_attr}>
  {watermark()}
  <div class="container about__grid">
    <div class="about__text anim anim--left">
      <h2>{title}</h2>
      {ps}
      {btn}
    </div>
    <div class="about__pics anim anim--right">
      <img class="about__pic about__pic--1" src="{img(photos[0], 900)}" alt="" loading="lazy">
      <img class="about__pic about__pic--2" src="{img(photos[1], 700)}" alt="" loading="lazy">
    </div>
  </div>
</section>"""


def plan_block(text, total, steps, photos):
    rows = "".join(f'<li><span class="plan__min">{m}</span><span class="plan__label">{l}</span></li>' for m, l in steps)
    pics = "".join(f'<span class="plan__pic" style="background-image:url(\'{img(p, 600)}\')"></span>' for p in photos)
    return f"""<section class="section">
  {watermark()}
  <div class="container">
    <div class="section__head anim anim--fade">
      <h2>Як проходять тренування</h2>
      <p>{text}</p>
    </div>
    <div class="plan anim anim--fade">
      <div class="plan__total"><b>{total}</b><span>план тренування</span></div>
      <ol class="plan__steps">{rows}</ol>
      <div class="plan__pics">{pics}</div>
    </div>
  </div>
</section>"""


def signup_ways():
    ways = [
        ("chat", "Написати нам", "в Instagram або Telegram — відповімо й запишемо", f'<a class="way__link" href="{TELEGRAM}">Написати</a>'),
        ("calendar", "Обрати час у розкладі", "і повідомити адміністратору, на яке заняття прийдете", '<a class="way__link" href="schedule.html">Розклад</a>'),
        ("form", "Залишити свої дані", "і ми вам зателефонуємо", '<button class="way__link" type="button" data-modal-open>Залишити</button>'),
    ]
    items = "".join(f'<div class="way anim anim--fade"><span class="way__icon">{ICON[i]}</span><div><h3>{t}</h3><p>{d}</p>{l}</div></div>' for i, t, d, l in ways)
    return f"""<section class="section section--soft">
  <div class="container">
    <div class="section__head anim anim--fade"><h2>Як записатися</h2></div>
    <div class="ways">{items}</div>
  </div>
</section>"""


def prices_block(cards, rules, extra=None):
    items = "".join(f"""<article class="price anim anim--rotate">
  {f'<span class="price__tag">{c[3]}</span>' if len(c) > 3 else ''}
  <h3>{c[0]}</h3>
  <p class="price__value">{c[1]}</p>
  <p class="price__note">{c[2]}</p>
  <button class="btn btn--pink btn--sm" type="button" data-modal-open>Придбати</button>
</article>""" for c in cards)
    rule_items = "".join(f"<li>{r}</li>" for r in rules)
    extra_html = ""
    if extra:
        extra_html = '<div class="prices__extra">' + "".join(f"""<article class="price price--row anim anim--rotate">
  <h3>{title}</h3>
  <ul class="price__list">{''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a, b in rows)}</ul>
  <button class="btn btn--pink btn--sm" type="button" data-modal-open>{btn}</button>
</article>""" for title, rows, btn in extra) + "</div>"
    return f"""<section class="section" id="prices">
  <div class="container">
    <div class="section__head anim anim--fade"><h2>Вартість тренувань</h2><p class="placeholder-note">Ціни буде додано — зараз це шаблон.</p></div>
    <div class="prices">
      {items}
      <aside class="price price--rules anim anim--rotate">
        <h3>Правила абонементу</h3>
        <ul class="bullets bullets--small">{rule_items}</ul>
      </aside>
    </div>
    {extra_html}
  </div>
</section>"""


def checklist_block(items):
    lis = "".join(f'<li class="anim anim--fade"><span>{ICON["sparkle"]}</span>{i}</li>' for i in items)
    return f"""<section class="section section--soft">
  <div class="container">
    <div class="section__head anim anim--fade"><h2>Не забудь на тренування</h2></div>
    <ul class="checklist">{lis}</ul>
  </div>
</section>"""


def more_block(exclude):
    all_cards = [
        ("pilates.html", "Пілатес", "reformer_split"),
        ("stretching.html", "Стретчинг", "stretch_arms"),
        ("barre.html", "Барре", "barre_coach"),
        ("choreography.html", "Хореографія для дітей", "ballet_little"),
        ("mama.html", "Мама + дитина", "mom_kid_2"),
    ]
    cards = "".join(service_card(h, t, p) for h, t, p in all_cards if h != exclude)
    return f"""<section class="section section--dark">
  {watermark()}
  <div class="container">
    <div class="section__head section__head--row"><h2>Дивіться ще</h2><a class="link-more" href="index.html#trainings">Усі тренування</a></div>
    <div class="services services--four">{cards}</div>
  </div>
</section>"""


TIMELINE = """<div class="timeline anim anim--fade">
  <div class="timeline__scale"><span>18:00</span><span>18:30</span><span>19:00</span></div>
  <div class="timeline__row"><span class="timeline__who">Мама</span><div class="timeline__bar timeline__bar--mom">Пілатес · зал 1</div></div>
  <div class="timeline__row"><span class="timeline__who">Дитина</span><div class="timeline__bar timeline__bar--kid">Хореографія · зал 2</div></div>
</div>"""


def home():
    slides = [
        ("reformer_arch", "Пілатес для мам,<br>хореографія для дітей&nbsp;—<br>в один час"),
        ("ballet_class", "Хореографія<br>для дітей 4–12 років"),
        ("stretch_arms", "Пілатес, стретчинг<br>і барре у Львові"),
    ]
    slide_html = "".join(f"""<div class="hero__slide{' is-active' if i == 0 else ''}">
      <span class="hero__img" style="background-image:url('{img(p, 1800)}')"></span>
      <div class="hero__content"><h1>{t}</h1></div>
    </div>""" for i, (p, t) in enumerate(slides))
    dots = "".join(f'<button type="button" class="{"is-active" if i == 0 else ""}" aria-label="Слайд {i + 1}"></button>' for i in range(len(slides)))

    adult_cards = "".join([
        service_card("pilates.html", "Пілатес", "reformer_split", badge="Основний напрямок"),
        service_card("stretching.html", "Стретчинг", "stretch_split"),
        service_card("barre.html", "Барре", "barre_coach"),
    ])
    kid_cards = "".join([
        service_card("choreography.html#age-4", "Хореографія", "ballet_little", sub="4–6 років"),
        service_card("choreography.html#age-7", "Хореографія", "ballet_class", sub="7–9 років"),
        service_card("choreography.html#age-10", "Хореографія", "ballet_stage", sub="10–12 років"),
    ])

    events = [
        ("Майстер-класи", "mat_group"),
        ("Звітні концерти дітей", "ballet_show"),
        ("Відкриті уроки для батьків", "ballet_feet"),
    ]
    event_html = "".join(f'<button class="event anim anim--fade" type="button" data-modal-open style="background-image:url(\'{img(p, 1600)}\')"><span class="event__label">{t}</span></button>' for t, p in events)

    body = f"""<section class="hero">
  <div class="hero__main" data-hero>
    {slide_html}
    <img class="hero__mark" src="assets/mark-white.webp" alt="" aria-hidden="true">
    <div class="hero__fixed">
      <div class="hero__actions">
        <button class="btn btn--pink" type="button" data-modal-open>Хочу на тренування</button>
        <a class="btn btn--outline-light" href="mama.html">Детальніше</a>
      </div>
      <div class="hero__dots">{dots}</div>
    </div>
  </div>
  <div class="hero__side">
    <a class="hero__tile hero__tile--dark" href="#trainings">
      <span class="hero__tile-kicker">Студія пілатесу</span>
      <span class="hero__tile-title">Тренування для дорослих</span>
      <span class="btn btn--outline-light btn--sm">Детальніше</span>
    </a>
    <a class="hero__tile hero__tile--pink" href="#kids">
      <span class="hero__tile-kicker">Хореографія</span>
      <span class="hero__tile-title">Тренування для дітей</span>
      <span class="btn btn--outline-dark btn--sm">Детальніше</span>
    </a>
  </div>
</section>
<div class="hero-bar">
  <div class="container hero-bar__inner">
    <a class="hero-bar__scroll" href="#about">Scroll {ICON['chevron']}</a>
    {socials("socials--light")}
  </div>
</div>

{about_split("IVVI Zone", [
    "Це студія пілатесу, стретчингу та барре у Львові, на вул. Стрийській, 45 (LAZ). Наш основний напрямок — пілатес: сильний центр, рівна спина, легкість у тілі.",
    "А ще у нас є те, чого немає в інших студіях: <b>одночасні тренування для мам і дітей</b>. Поки мама займається пілатесом, дитина танцює на хореографії в сусідній залі.",
    "Записуйтесь, приводьте подруг і дітей — ви обов’язково відчуєте атмосферу та результат від наших тренувань!",
], ["studio", "mat_boat"], button=False, anchor="about")}

{advantages_block()}

<section class="section" id="trainings">
  {watermark()}
  <div class="container services">
    {info_box("Тренування для дорослих", [
        "Пілатес — основа студії, плюс стретчинг і барре",
        "Тривалість тренування — 55 хвилин",
        "Підходить з нуля, після пологів чи перерви",
        "Малі групи до 8 людей",
        "Ранкові слоти для мам у декреті",
        "Можна займатися індивідуально",
    ])}
    {adult_cards}
  </div>
</section>

<section class="section section--dark together" id="together">
  {watermark("TOGETHER")}
  <div class="container together__grid">
    <div class="anim anim--left">
      <p class="kicker">Наша фішка</p>
      <h2>Мама + дитина<br>в один час</h2>
      <p>Ми ставимо пілатес для мам і хореографію для дітей на один і той самий час. Ви приходите разом — і кожен займається своїм. Година, яка працює на всю родину.</p>
      <a class="btn btn--pink" href="mama.html">Детальніше</a>
    </div>
    {TIMELINE}
  </div>
</section>

<section class="section section--soft" id="kids">
  {watermark()}
  <div class="container services">
    {info_box("Тренування для дітей", [
        "Хореографія для дітей від 4 до 12 років",
        "Групи за віком: 4–6, 7–9, 10–12 років",
        "Тривалість заняття — 45–55 хвилин",
        "Постава, ритм, пластика та впевненість",
        "Звітні концерти й відкриті уроки для батьків",
        "Заняття в той самий час, що й пілатес для мам",
    ])}
    {kid_cards}
  </div>
</section>

<section class="section section--dark">
  {watermark()}
  <div class="container about__grid">
    <div class="about__text anim anim--left">
      <h2>Індивідуальні тренування</h2>
      <p>Найшвидший спосіб досягти бажаного результату. Тренер підбере вправи під ваші цілі, рівень і фізичні особливості — наприклад, відновлення після пологів чи проблеми зі спиною.</p>
      <p>Можна займатися сам на сам із тренером або вдвох з подругою.</p>
      <button class="btn btn--pink" type="button" data-modal-open>Детальніше</button>
    </div>
    <div class="about__pics anim anim--right">
      <img class="about__pic about__pic--single" src="{img("reformer_stand", 1000)}" alt="" loading="lazy">
    </div>
  </div>
</section>

{trial_block()}

<section class="section section--pink events">
  <div class="container">
    <div class="section__head section__head--row"><h2>Ми організовуємо івенти</h2></div>
    <div class="events__list">{event_html}</div>
  </div>
</section>

{reviews_block()}

<section class="section seo">
  <div class="container about__grid">
    <div class="anim anim--left">
      <h2>Пілатес у Львові</h2>
      <p>Хочете зміцнити спину, підтягнути тіло й почуватися легше — без виснажливих тренувань? Пілатес — саме те, з чого варто почати. А поки ви займаєтесь, дитина може бути поруч, на хореографії в сусідній залі.</p>
      <p>Студія IVVI Zone чекає на вас за адресою: {ADDRESS}.</p>
      <a class="btn btn--dark" href="contacts.html">Як нас знайти</a>
    </div>
    <div class="anim anim--right"><img class="seo__img" src="{img("reformer_duo", 1000)}" alt="" loading="lazy"></div>
  </div>
</section>

{insta_block()}"""
    page("index.html", "IVVI Zone — пілатес, стретчинг, барре та хореографія для дітей у Львові",
         "Студія пілатесу у Львові. Наша фішка: мама займається пілатесом, а дитина в цей же час — хореографією.", body)


ADULT_RULES = [
    "Абонемент діє 1 місяць з першого заняття",
    "Абонемент поширюється на всі дорослі напрямки",
    "Пропущене заняття можна відпрацювати, якщо попередили за 6 годин",
    "При купівлі абонементу на пробному — пробне безкоштовне",
]
ADULT_PRICES = [
    ("Разове тренування", "000 ₴", "Перше тренування безкоштовне при купівлі абонементу"),
    ("4 тренування", "000 ₴", "Абонемент на 1 місяць"),
    ("8 тренувань", "000 ₴", "Абонемент на 1 місяць", "Популярний"),
    ("12 тренувань", "000 ₴", "Абонемент на 1 місяць"),
]
INDIVIDUAL = [
    ("Індивідуальні тренування", [("Разове", "000 ₴"), ("5 тренувань", "000 ₴"), ("10 тренувань", "000 ₴")], "Придбати"),
    ("Тренування вдвох", [("Разове", "000 ₴"), ("5 тренувань", "000 ₴"), ("10 тренувань", "000 ₴")], "Придбати"),
    ("Подарунковий сертифікат", [("Будь-яка сума", "від 000 ₴"), ("Будь-який напрямок", "✓")], "Замовити"),
]
ADULT_CHECKLIST = ["Зручний спортивний одяг", "Шкарпетки з нековзною підошвою", "Пляшка води", "Невеликий рушник", "Прийти за 10 хвилин до початку", "Обов’язково гарний настрій!"]

DIRECTIONS = [
    {
        "file": "pilates.html", "key": "pilates", "title": "Пілатес",
        "seo": "Пілатес у Львові для початківців і мам після пологів — IVVI Zone",
        "desc": "Пілатес у Львові в малих групах: сильний прес і спина, правильне дихання, безпечно після пологів.",
        "hero": "reformer_arch", "crumb": ("index.html#trainings", "Тренування для дорослих"),
        "about": [
            "Пілатес — система вправ, що зміцнює глибокі м’язи, вирівнює поставу й учить правильно дихати. Рухи плавні й контрольовані, без ударного навантаження, тому він безпечний для спини та суглобів.",
            "Це наш основний напрямок. Підходить, якщо ви ніколи не займались спортом, відновлюєтесь після пологів або хочете позбутися болю в спині від сидячої роботи.",
        ],
        "photos": ["reformer_split", "pilates_ring"],
        "plan_text": "Кожне тренування будуємо так, щоб тіло поступово розігрілося, попрацювало в повну силу й відновилося.",
        "plan": ("55 хв", [("10 хв", "Розминка та дихання"), ("35 хв", "Основна частина"), ("10 хв", "Розтяжка й розслаблення")]),
        "plan_photos": ["reformer_leg", "mat_boat", "mat_group"],
    },
    {
        "file": "stretching.html", "key": "stretching", "title": "Стретчинг",
        "seo": "Стретчинг у Львові, розтяжка для початківців — IVVI Zone",
        "desc": "Стретчинг у Львові: м’яка розтяжка для гнучкості, легкості й здорової спини.",
        "hero": "stretch_split", "crumb": ("index.html#trainings", "Тренування для дорослих"),
        "about": [
            "Стретчинг — комплекс вправ для гнучкості та рухливості всього тіла. Знімає затиски в шиї, плечах і спині, покращує кровообіг і самопочуття.",
            "Ми викладаємо стретчинг в оздоровчому форматі: без болю й «дотягування» силою. Відмінне доповнення до пілатесу.",
        ],
        "photos": ["stretch_arms", "stretch_leg"],
        "plan_text": "Тренування проходять з урахуванням особливостей кожної, хто займається, — м’язи й суглоби стають еластичнішими поступово.",
        "plan": ("55 хв", [("15 хв", "Розігрів і підготовка"), ("35 хв", "Основна розтяжка"), ("5 хв", "Завершальна частина")]),
        "plan_photos": ["stretch_split", "stretch_leg", "mat_group"],
    },
    {
        "file": "barre.html", "key": "barre", "title": "Барре",
        "seo": "Барре у Львові — тренування біля балетного станка, IVVI Zone",
        "desc": "Барре у Львові: балетний станок, пілатес і фітнес в одному. Тонус ніг, сідниць і гарна постава.",
        "hero": "barre_studio", "crumb": ("index.html#trainings", "Тренування для дорослих"),
        "about": [
            "Барре — тренування біля балетного станка, що поєднує елементи балету, пілатесу та фітнесу. Невеликі амплітуди, багато повторів — м’язи працюють глибоко, а тіло стає підтягнутим і витонченим.",
            "Не потрібно мати балетного досвіду: тренер покаже базові позиції й підкаже, як тримати поставу.",
        ],
        "photos": ["barre_coach", "barre_group"],
        "plan_text": "Тренування йде у ритмі музики: від розігріву біля станка до вправ на килимку.",
        "plan": ("55 хв", [("10 хв", "Розігрів біля станка"), ("35 хв", "Робота біля станка й на килимку"), ("10 хв", "Розтяжка")]),
        "plan_photos": ["barre_studio", "barre_coach", "barre_group"],
    },
]


def direction(d):
    total, steps = d["plan"]
    body = f"""{page_hero([("index.html", "IVVI Zone"), d["crumb"], (None, d["title"])], d["title"], d["hero"])}
{about_split("Про " + d["title"].lower(), d["about"], d["photos"], anchor="more")}
{advantages_block(ADVANTAGES[:1] + ADVANTAGES[2:4], slide=False)}
{plan_block(d["plan_text"], total, steps, d["plan_photos"])}
{signup_ways()}
{prices_block(ADULT_PRICES, ADULT_RULES, INDIVIDUAL)}
{checklist_block(ADULT_CHECKLIST)}
{trial_block()}
{reviews_block()}
{more_block(d["file"])}"""
    page(d["file"], d["seo"], d["desc"], body, active=d["key"])


def choreography():
    groups = [
        ("age-4", "4–6 років", "Малюки", "Ритміка, музичні ігри, перші танцювальні рухи, координація та увага.", "ballet_little"),
        ("age-7", "7–9 років", "Молодша група", "Основи класичного танцю, розтяжка, постава, перші невеликі постановки.", "ballet_class"),
        ("age-10", "10–12 років", "Старша група", "Сучасна хореографія, техніка, сценічна впевненість і звітні концерти.", "ballet_stage"),
    ]
    group_html = "".join(f"""<article class="group anim anim--flip" id="{a}">
  <span class="group__img" style="background-image:url('{img(p, 800)}')"></span>
  <div class="group__body"><span class="group__age">{age}</span><h3>{t}</h3><p>{txt}</p>
  <button class="btn btn--pink btn--sm" type="button" data-modal-open data-direction-value="Хореографія для дитини">Записатися</button></div>
</article>""" for a, age, t, txt, p in groups)
    kid_prices = [
        ("Разове заняття", "000 ₴", "Пробне заняття — за спеціальною ціною"),
        ("8 занять", "000 ₴", "Абонемент на 1 місяць", "Популярний"),
        ("Мама + дитина", "000 ₴", "8 пілатесу + 8 хореографії на місяць", "Вигідно"),
    ]
    rules = [
        "Абонемент діє 1 місяць з першого заняття",
        "Перші хвилини батьки можуть побути поруч",
        "Пропущене через хворобу заняття переноситься",
        "Звітні концерти — двічі на рік",
    ]
    body = f"""{page_hero([("index.html", "IVVI Zone"), ("index.html#kids", "Тренування для дітей"), (None, "Хореографія")], "Хореографія для дітей", "ballet_class", sub="4–12 років · групи за віком")}
{about_split("Про хореографію", [
    "Дитяча хореографія розвиває поставу, координацію, гнучкість і відчуття ритму. А ще — впевненість у собі: діти виступають на звітних концертах і вчаться не боятися сцени.",
    "Заняття проходять у той самий час, що й пілатес для мам, тож можна прийти разом і кожному зайнятися своїм.",
], ["ballet_feet", "ballet_little"], anchor="more")}
<section class="section section--soft">
  {watermark("DANCE")}
  <div class="container">
    <div class="section__head anim anim--fade"><h2>Групи за віком</h2><p>Навантаження і програма відповідають віку дитини.</p></div>
    <div class="groups">{group_html}</div>
  </div>
</section>
{advantages_block([
    ("Увага до кожної", "Невеликі групи, тренер бачить кожну дитину і м’яко поправляє."),
    ("Через гру", "Для малюків — музичні ігри та казкові сюжети, щоб заняття були в радість."),
    ("Сцена", "Звітні концерти та відкриті уроки, де батьки бачать прогрес."),
], slide=False)}
{plan_block("Заняття побудоване так, щоб дитина не втомлювалась і йшла додому з гарним настроєм.", "45 хв", [("10 хв", "Розминка й ритміка"), ("25 хв", "Вивчення рухів і зв’язок"), ("10 хв", "Розтяжка й гра")], ["ballet_class", "ballet_feet", "ballet_show"])}
{signup_ways()}
{prices_block(kid_prices, rules)}
{checklist_block(["Купальник або футболка з лосинами", "Чешки або шкарпетки", "Волосся зібране в пучок", "Пляшка води", "Прийти за 10 хвилин до початку", "Гарний настрій!"])}
{trial_block()}
{reviews_block()}
{more_block("choreography.html")}"""
    page("choreography.html", "Хореографія для дітей 4–12 років у Львові — IVVI Zone",
         "Дитяча хореографія у Львові: групи 4–6, 7–9, 10–12 років. Заняття в той самий час, що й пілатес для мам.", body, active="choreography")


def mama():
    steps = [
        ("01", "Приходите разом", "Обираєте слот «мама + дитина» в розкладі — він однаковий для обох."),
        ("02", "Тренуєтесь паралельно", "Ви — на пілатесі, дитина — на хореографії в сусідній залі під наглядом тренера."),
        ("03", "Йдете додому разом", "Без пошуку няні та чекання в коридорі. Година, яка працює на всю родину."),
    ]
    step_html = "".join(f'<article class="step anim anim--fade"><span class="step__num">{n}</span><h3>{t}</h3><p>{d}</p></article>' for n, t, d in steps)
    prices = [
        ("Мама + дитина, разове", "000 ₴", "Пілатес + хореографія в один час"),
        ("Мама + дитина, 8+8", "000 ₴", "Абонемент на 1 місяць", "Вигідно"),
        ("Мама + дитина, 12+12", "000 ₴", "Абонемент на 1 місяць"),
    ]
    rules = [
        "Слоти «мама + дитина» позначені в розкладі",
        "Можна ходити з двома дітьми — уточнюйте ціну",
        "Абонемент діє 1 місяць з першого заняття",
        "Пробне заняття — для обох одночасно",
    ]
    body = f"""{page_hero([("index.html", "IVVI Zone"), (None, "Мама + дитина")], "Мама + дитина", "mom_kid_2", sub="Пілатес для мами й хореографія для дитини — в один час")}
{about_split("Як це працює", [
    "Ми знаємо, як складно мамі знайти годину на себе: дитину ні з ким залишити, а чекати в коридорі нудно обом.",
    "Тому ставимо пілатес для мам і хореографію для дітей на один і той самий час у сусідніх залах. Ви тренуєтесь, дитина танцює — і ніхто нікого не чекає.",
], ["mom_kid_1", "ballet_little"], anchor="more")}
<section class="section section--dark">
  {watermark("TOGETHER")}
  <div class="container">
    <div class="section__head anim anim--fade"><h2>Одна година — два тренування</h2></div>
    {TIMELINE}
    <div class="steps">{step_html}</div>
  </div>
</section>
{signup_ways()}
{prices_block(prices, rules)}
{checklist_block(["Мамі — зручний одяг і шкарпетки", "Дитині — форма для танців і чешки", "Вода для обох", "Прийти за 10 хвилин до початку", "Гарний настрій!"])}
{trial_block()}
{reviews_block()}
{more_block("mama.html")}"""
    page("mama.html", "Мама + дитина: пілатес і хореографія в один час — IVVI Zone",
         "Унікальний формат IVVI Zone у Львові: мама на пілатесі, дитина на хореографії — в один і той самий час.", body, active="mama")


SCHEDULE = [
    ("Понеділок", [("09:30", "Пілатес", "pilates"), ("18:00", "Пілатес + хореографія", "together pilates kids"), ("19:30", "Стретчинг", "stretching")]),
    ("Вівторок", [("10:00", "Барре", "barre"), ("17:00", "Хореографія 4–6", "kids"), ("19:00", "Пілатес", "pilates")]),
    ("Середа", [("09:30", "Пілатес", "pilates"), ("18:00", "Пілатес + хореографія", "together pilates kids"), ("19:30", "Барре", "barre")]),
    ("Четвер", [("10:00", "Стретчинг", "stretching"), ("17:00", "Хореографія 7–12", "kids"), ("19:00", "Пілатес", "pilates")]),
    ("П’ятниця", [("09:30", "Пілатес", "pilates"), ("18:00", "Пілатес + хореографія", "together pilates kids")]),
    ("Субота", [("10:00", "Пілатес + хореографія", "together pilates kids"), ("11:30", "Стретчинг", "stretching"), ("12:30", "Барре", "barre")]),
]


def schedule():
    days = "".join(f"""<div class="day anim anim--fade"><h3>{d}</h3>{''.join(f'<div class="slot{" slot--together" if "together" in t else ""}" data-type="{t}"><time>{h}</time><span>{n}</span></div>' for h, n, t in slots)}</div>""" for d, slots in SCHEDULE)
    filters = "".join(f'<button class="filter{" is-active" if k == "all" else ""}" type="button" data-filter="{k}">{t}</button>' for k, t in [("all", "Усі"), ("together", "Мама + дитина"), ("pilates", "Пілатес"), ("stretching", "Стретчинг"), ("barre", "Барре"), ("kids", "Хореографія")])
    body = f"""{page_hero([("index.html", "IVVI Zone"), (None, "Розклад")], "Розклад", "studio", buttons=False, sub="Слоти «мама + дитина» — пілатес і хореографія одночасно")}
<section class="section">
  {watermark()}
  <div class="container">
    <p class="placeholder-note">Розклад орієнтовний — уточнюйте в адміністратора.</p>
    <div class="filters" role="group" aria-label="Фільтр розкладу">{filters}</div>
    <div class="week">{days}</div>
  </div>
</section>
{trial_block()}"""
    page("schedule.html", "Розклад тренувань — IVVI Zone, Львів", "Розклад пілатесу, стретчингу, барре та дитячої хореографії в студії IVVI Zone у Львові.", body, active="schedule")


def contacts():
    map_src = "https://www.google.com/maps?q=" + MAP_QUERY.replace(" ", "+") + "&output=embed"
    body = f"""{page_hero([("index.html", "IVVI Zone"), (None, "Контакти")], "Контакти", "studio", buttons=False)}
<section class="section">
  <div class="container contacts">
    <div class="contacts__card anim anim--left">
      <h2>Як нас знайти</h2>
      <p class="contacts__line">{ICON['pin']}<span>{ADDRESS}</span></p>
      <p class="contacts__line">{ICON['phone']}<span class="placeholder">{PHONE}</span></p>
      <p class="contacts__line">{ICON['instagram']}<span class="placeholder">@instagram</span></p>
      <p class="contacts__line">{ICON['telegram']}<span class="placeholder">Telegram</span></p>
      <p class="contacts__line">{ICON['calendar']}<span class="placeholder">Години роботи</span></p>
      <button class="btn btn--pink" type="button" data-modal-open>Записатися на тренування</button>
      <a class="contacts__maplink" href="https://www.google.com/maps/search/?api=1&amp;query={MAP_QUERY.replace(' ', '+')}" target="_blank" rel="noopener">Відкрити в Google Maps</a>
    </div>
    <div class="contacts__map anim anim--right">
      <iframe src="{map_src}" title="IVVI Zone на мапі" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
{insta_block()}"""
    page("contacts.html", "Контакти — IVVI Zone, Львів, вул. Стрийська, 45", "Студія IVVI Zone: Львів, вул. Стрийська, 45, LAZ. Пілатес, стретчинг, барре та хореографія для дітей.", body, active="contacts")


if __name__ == "__main__":
    home()
    for d in DIRECTIONS:
        direction(d)
    choreography()
    mama()
    schedule()
    contacts()
    print("built:", ", ".join(sorted(p.name for p in ROOT.glob("*.html"))))
