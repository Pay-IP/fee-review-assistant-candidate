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

## Layout

- `src/App.jsx`: page shell and future state coordination
- `src/api.js`: small incomplete fetch helper
- `src/components/`: incomplete filter, table, and explanation components
- `src/styles.css`: minimal starter styling
- `tests/App.test.jsx`: passing starter test

Use plain React state and native `fetch`; additional state-management or component libraries are not needed.
