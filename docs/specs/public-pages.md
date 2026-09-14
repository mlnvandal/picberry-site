# Picberry public pages

The website introduces Picberry with a concise product overview and real application screenshots, and provides public privacy and support information. It is a small static GitHub Pages site with no app backend, visitor accounts, forms, client-side scripts, analytics, external fonts, or cookies set by the site.

## Routes and publication

- `/` introduces the Mac photo and video library with two real screenshots, concise browsing, Albums/Favorites, People, and playback descriptions, and links to Privacy and Support.
- `/privacy/` contains the effective date, product identity and contact, local processing and storage practices, device connections, support handling, Apple services, website hosting, and privacy contact.
- `/support/` contains the public support email, supported Mac requirements, and verified troubleshooting actions.
- `/404.html` provides a working route back to the site root from unknown URLs.
- Directory `index.html` files give stable extension-free paths. Source paths do not include Jekyll dates, categories, or `.html` in public links.
- The initial origin is `https://mlnvandal.github.io/picberry-site/`. Relative internal links work under the project prefix and a future custom domain.
- Only `site/` is published. Repository documentation and maintenance scripts are excluded from the Pages artifact.

## Content and presentation

- Public identity is Picberry. Use the contact email instead of publishing the owner's personal name, including in footers, policy copy, repository documentation, and commit authorship.
- Public copy is in English and uses `milanvandal@gmail.com` for support and privacy requests, as provided by the owner for publication.
- Do not claim release availability, approval by Apple, cloud sync, Intel support, automatic diagnostics uploads, or unsupported features.
- Describe local processing separately from voluntary support correspondence and the hosting provider's technical logs.
- Use the existing Picberry icon unchanged. Use system fonts and the product's established colors. Keep the information readable on mobile and desktop.
- Semantic headings, landmark navigation, visible keyboard focus, and a skip link are required.
- No App Store Connect changes, desktop application changes, domain purchase, or release operation belongs to this website task.

## Acceptance

Check HTML structure, internal links and fragments, resource paths, route responses, public access, email links, HTTPS, desktop/mobile rendering, and the completed Pages deployment. Recheck privacy copy whenever released application behavior changes.

## Homepage overview

The homepage uses the app's dark palette and squircle surface geometry. A large Library capture, three short feature descriptions, and a Preview capture explain the app without implying App Store availability or introducing a download action.

- Keep the homepage responsive and use complete, proportionate captures; never reconstruct the interface or place invented controls over it.
- Use locally hosted WebP derivatives of the existing build-owned screenshots. `docs/screenshot-sources.json` records the original capture set, hashes, dimensions, and encoding. Source screenshots and application files remain unchanged.
- The selected set is the last successful capture from September 5, 2026, version `0.1.267`; it is not the current desktop version. Newer capture attempts failed, preserving that set. Do not describe the images as a current-build certification.
- Review replacement captures for local paths, personal details, unfinished states, and correspondence with public feature copy. Do not publish Settings captures containing the local username.
- Images have descriptive alternative text and explicit dimensions. Load the hero eagerly and the lower Preview image lazily. Screenshots are illustrations; no interactive screenshot controls or client-side scripts are added.
- Scope homepage styling under `.landing`; Privacy, Support, and the custom 404 retain their existing layout and content.
