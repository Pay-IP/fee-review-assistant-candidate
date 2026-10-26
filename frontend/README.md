# Frontend starter

This directory contains the supported default React and Vite starter for the Fee Review Assistant. Candidates may replace it with an equivalent browser frontend. It renders a heading and incomplete component shells. The fee-review flow and API integration are deliberately marked with `TODO(candidate)`.

## Native setup

Run from `frontend/`:

```bash
npm install
npm run dev
```

Open <http://localhost:5173>. The frontend expects the API at `http://localhost:8000` unless `VITE_API_BASE_URL` is set.

## Tests and build

```bash
npm test -- --run
npm run build
```

The initial test only verifies the operational starter page.

## Security dependency qualification

The Docker base is Node 22.23.4 Alpine, pinned to the official multi-platform
image digest. Vite 8.2.4 and Vitest 4.1.12 are pinned together with the lockfile.
Scoped overrides keep jsdom's Undici at 8.12.3, css-tree/PostCSS's source-map-js
at 1.2.2, within their parents' supported ranges. The compatible PostCSS update
also brings in patched Nano ID. These address the October 2026 audit, including the newer mocker and Undici
advisories and the additional Nano ID denial-of-service finding.

Use a patched Node release for native dependency commands (22.23.4 for parity
with Docker), run `npm ci`, then run the tests/build above, `npm ls --all`, and
`npm audit`. The **Frontend dependency qualification** PR workflow builds this
Dockerfile, checks the actual container's Node version and complete dependency
tree, runs the audit/tests/build, and smoke tests the server. It does not publish
an image or deploy the application. An existing Compose node_modules volume must
be refreshed with `docker compose run --rm frontend npm ci` after a lockfile update.

The Node security release backports the Brotli decoder fix; its embedded Brotli
version string alone does not establish whether the fix is present. Sources:
[Node security release](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases),
[mocker advisory](https://github.com/advisories/GHSA-qxg6-89mg-rqv8),
[Undici advisories](https://github.com/nodejs/undici/security/advisories), and
[Nano ID advisory](https://github.com/advisories/GHSA-2v37-7h3g-55p8).

## Layout

- `src/App.jsx`: page shell and future state coordination
- `src/api.js`: small incomplete fetch helper
- `src/components/`: incomplete filter, table, and explanation components
- `src/styles.css`: minimal starter styling
- `tests/App.test.jsx`: passing starter test

Use plain React state and native `fetch`; additional state-management or component libraries are not needed.
