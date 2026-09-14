# Picberry website

This repository owns only the public privacy and support website. The desktop and companion applications are separate repositories and must not be changed by website work.

- Read `docs/specs/public-pages.md` before behavior or publication changes.
- Keep public content factual and in English. Preserve the approved contact email unless the owner changes it.
- Keep the site static: no analytics, visitor forms, client-side JavaScript, external fonts, cookies, or backend without explicit owner authorization.
- Preserve `/privacy/` and `/support/`. Only `site/` belongs in the Pages artifact.
- Reuse the canonical Picberry icon unchanged; do not regenerate or redraw it.
- Check privacy assertions against the exact application version being released; website publication does not certify App Store readiness.
- Run `npm run check` and `npm run build`. Inspect changed pages on desktop and mobile before publication.
- Increment the website version and append a matching changelog entry for later changes. Never bump the separate desktop app for website-only work.
- Keep generated `_site/`, caches, logs, temporary files, and credentials out of source control.
- Document approved behavior and maintenance steps in `README.md`.
