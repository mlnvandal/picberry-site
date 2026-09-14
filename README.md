# Picberry website

Public privacy information and support for Picberry. This standalone static website is hosted on GitHub Pages; maintaining its published pages does not depend on a ChatGPT subscription.

- [Website](https://mlnvandal.github.io/picberry-site/)
- [Privacy Policy](https://mlnvandal.github.io/picberry-site/privacy/)
- [Support](https://mlnvandal.github.io/picberry-site/support/)

The public identity is **Picberry**. Use the product name and contact email in public copy and Git authorship; do not publish the owner's personal name.

The public support and privacy contact is **milanvandal@gmail.com**. There are no visitor accounts, forms, JavaScript, analytics, external fonts, or cookies set by this website. GitHub operates the hosting infrastructure under its own privacy terms.

<details><summary>Edit, check, and preview</summary>

Edit the authored HTML in `site/`. Shared presentation lives in `site/assets/site.css`. The Picberry icon is an unchanged copy of the product's canonical artwork; do not regenerate it.

No packages need to be installed. Python 3.9+ is sufficient; the npm commands are optional shortcuts.

```sh
npm run check
npm run build
npm run preview
```

Alternatively, run `python3 scripts/build.py` and `python3 -m http.server 4173 --bind 127.0.0.1 --directory _site`.

Open `http://127.0.0.1:4173/picberry-site/`. The preview deliberately keeps the GitHub project prefix so it can reveal incorrect root-relative links. `_site/` is generated and ignored by Git.

The checker validates local references and fragments, email links, required routes, basic HTML accessibility structure, and the absence of scripts, forms, and externally loaded resources. Also inspect the changed pages in a browser at desktop and mobile sizes.

</details>

<details><summary>Publish and maintain stable URLs</summary>

The repository's **Settings → Pages → Source** must be **GitHub Actions**. Every push to `main` validates the source, builds the public output, and publishes through the **Publish Picberry website** workflow. Pull requests validate without publishing. The workflow can also run manually.

Only `_site/picberry-site/` is uploaded. Repository documentation and scripts do not become public web routes, although repository files themselves are public.

The site uses `privacy/index.html` and `support/index.html`, giving extension-free `/privacy/` and `/support/` paths. No Jekyll permalink configuration is needed. Keep those routes stable after entering them in App Store Connect. Do not rename the repository without planning the URL change.

Check the successful workflow, both live pages, HTTPS, and the custom not-found page after publication. To revert content, revert the relevant Git commit and let the same workflow publish it.

</details>

<details><summary>Connect a custom domain later</summary>

No domain is currently configured. A domain purchase or DNS change requires the owner's separate instruction.

1. Verify the domain under the owner's GitHub account **Settings → Pages**, using GitHub's TXT record.
2. Set the domain directly on this repository under **Settings → Pages → Custom domain** before changing the routing DNS records.
3. Use GitHub's supplied DNS instructions: a subdomain normally points by CNAME to `mlnvandal.github.io`; an apex domain uses ALIAS/ANAME or the published GitHub Pages A records.
4. In `pages.yml`, build with `python3 scripts/build.py --base-path /` and change the artifact path to `_site`. This also updates the 404 page's resource and navigation prefixes. Normal page links are relative and require no changes.
5. Update the public links in this README, wait for domain verification and certificate issuance, and enable **Enforce HTTPS**. Test the domain and both page routes before updating App Store metadata.

See [GitHub's custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). Custom Actions deployments manage the domain in Pages settings; a source `CNAME` file is not required.

</details>

<details><summary>Privacy and release maintenance</summary>

Review the policy whenever the app's data handling, permissions, network behavior, diagnostics, recognition, support handling, or website hosting changes. Update its effective date when changing the policy. Verify statements against the application build being submitted; publishing this website does not complete the App Store privacy questionnaire or add an in-app privacy link.

Support correspondence is handled by the developer through email. No response-time guarantee or invented fixed retention period is published. The developer is responsible for responding to privacy requests and managing support correspondence.

This site contains product-owned content and artwork. It does not grant a separate license to reuse Picberry branding.

</details>
