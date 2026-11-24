# Guttenbergovitz for Firefox

Warm, low-contrast static WebExtension themes for Firefox in **Dark** and **Light** variants, generated from [`palette.json`](../palette.json).

## Variants

- `firefox/dark/manifest.json` — **Guttenbergovitz** (`guttenbergovitz-dark@guttenbergovitz.dev`)
- `firefox/light/manifest.json` — **Guttenbergovitz Light** (`guttenbergovitz-light@guttenbergovitz.dev`)

## Try Locally (Temporary)

1. Open `about:debugging#/runtime/this-firefox` in Firefox.
2. Click **Load Temporary Add-on...**.
3. Select `firefox/dark/manifest.json` or `firefox/light/manifest.json`.

## Package for AMO (addons.mozilla.org)

Build both `.xpi` packages from the repository root:

```bash
make package.firefox
```

This creates:
- `firefox/guttenbergovitz-dark.xpi`
- `firefox/guttenbergovitz-light.xpi`

Upload either `.xpi` (or `.zip`) to the [Mozilla Add-ons Developer Hub](https://addons.mozilla.org/developers/) as **Listed** (public store) or **Unlisted** (signed `.xpi` for self-distribution).
