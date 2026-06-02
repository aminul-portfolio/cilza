# Submission Test Log - Cilza Cakes Studio

## Environment

- OS: Windows 10
- Runtime: Django development server
- Project path: `G:\healthcakes_project\healthcakes_project`
- Date: 2026-06-02

## Django Validation

- Command: `python manage.py check`
- Result: Pass with warning:
  - `staticfiles.W004` previously observed due to missing project-level static directory (addressed by adding `healthcakes_project/static/`).

## Pages Tested (Manual checklist)

- [x] Home (`/`)
- [x] Cakes (`/cakes/`)
- [x] Cake detail (`/cakes/<slug>/`)
- [x] Occasions (`/welcome/`)
- [x] Offers (`/offers/`)
- [x] About (`/about/`)
- [x] Contact (`/contact/`)
- [x] Cart (`/cart/`)
- [x] Plan an Order (`/plan-order/`)
- [x] Privacy Policy (`/privacy/`)

## Navigation / Link Checks

- [x] Logo links to Home.
- [x] Main nav visible and consistent.
- [x] Footer links no longer use `#` placeholders for policy/order/contact paths.
- [x] Privacy Policy linked in footer and relevant forms.

## Cakes Filter Checks

- [x] All Cakes
- [x] Wedding
- [x] Anniversary
- [x] Party
- [x] Everyday / Other
- [x] Birthday Zone
- [x] Kids Collection
- [x] Chocolate Collection

## Form Checks

- [x] Contact form has labels and required fields.
- [x] Contact form includes email type validation.
- [x] Plan an Order form includes required fields and browser validation classes.
- [x] Privacy wording linked near form submission.

## Responsive Check Targets

- [x] 1440px
- [x] 1280px
- [x] 1024px
- [x] 768px
- [x] 430px
- [x] 390px
- [x] 375px

## Accessibility Basics Reviewed

- [x] Semantic page landmarks.
- [x] One main `h1` per page.
- [x] Focus-visible styles on interactive elements.
- [x] Form labels present.
- [x] Keyboard-accessible links/buttons.

## Known Limitations

- Final visual QA screenshots still need manual capture in browser.
- Image assets referenced by templates should be verified against local static/media inventory.
- Demo forms are not persisted server-side in this submission build.

## Required Screenshot Checklist (Manual Capture)

- [ ] Desktop Home
- [ ] Desktop Cakes
- [ ] Desktop Occasions
- [ ] Desktop About
- [ ] Desktop Contact
- [ ] Mobile Home
- [ ] Mobile Cakes
- [ ] Mobile Contact
- [ ] Navbar mobile expanded state
- [ ] Footer mobile state
- [ ] Form validation / confirmation state
