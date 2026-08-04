# Fee Review Assistant — candidate instructions

## Purpose

You will extend a small starter application that helps a user review fictional card-network fee records and identify fees that may require investigation. The exercise assesses practical engineering judgment across backend development, frontend development, APIs, data, testing, debugging, and responsible AI-assisted development.

This is not a memorisation or unaided-coding test. You may use any tools you would normally use: ChatGPT, Claude, Codex, Cursor, GitHub Copilot, coding agents, IDE integrations, documentation, internet searches, terminal tools, and code generators. AI use is permitted and encouraged.

Share your screen throughout. Explain important decisions, especially how you scope the work, what you ask tools to do, and how you inspect or validate generated changes. You remain responsible for requirements, architecture, correctness, security, tests, and maintainability. If a tool produces something questionable, investigate it and decide whether to fix, reject, or replace it.

> You will not be assessed on whether you can complete every feature. You will be assessed on how you understand the problem, prioritise work, use development tools, review generated output, test your solution and explain technical decisions.

## Time box and priorities

You will have about 35 minutes of active implementation within a one-hour interview. Completeness is less important than sound judgment. Start by clarifying assumptions and choose a useful end-to-end path. Do not spend time on visual polish.

You may change the starter structure when you can explain why. Prefer small, understandable changes and preserve an operational application.

## Fork, branch, and submit your work

You have read access to the public starter repository but cannot push branches directly to the Pay-IP repository. Before you begin implementation, create a fork under your own GitHub account and work in a dedicated branch on that fork.

1. Sign in to GitHub and open <https://github.com/Pay-IP/fee-review-assistant-candidate>.
2. Select **Fork**, choose your personal GitHub account as the owner, and create the fork.
3. Clone your fork, replacing `<your-github-username>` below:

   ```bash
   git clone https://github.com/<your-github-username>/fee-review-assistant-candidate.git
   cd fee-review-assistant-candidate
   git switch development
   git pull --ff-only
   git switch -c interview/<your-name>
   ```

4. Confirm that `origin` points to your fork:

   ```bash
   git remote -v
   ```

5. Implement and test your solution. Commit your work before the interview ends:

   ```bash
   git status
   git add <files-you-intend-to-submit>
   git commit -m "Implement fee review flow"
   git push -u origin interview/<your-name>
   ```

6. Share the URL of your fork and branch with the interviewer. If requested, open a pull request from your branch to `Pay-IP/fee-review-assistant-candidate:development`; do not merge it yourself.

If you already cloned the Pay-IP repository before creating your fork, keep that checkout and change its remotes after the fork exists:

```bash
git remote rename origin upstream
git remote add origin https://github.com/<your-github-username>/fee-review-assistant-candidate.git
git fetch origin
git switch development
git switch -c interview/<your-name>
```

Your GitHub fork and pushed interview branch will be public because the starter repository is public. Do not commit credentials, personal information, real company/client data, local environment files, or unrelated work.

## Technology choice

The supplied default is Python 3.12 with FastAPI for the backend and JavaScript with React and Vite for the frontend. You may replace the backend, the frontend, or both with languages and frameworks that better represent how you normally work. You will not be penalised for using an alternative stack.

If you choose an alternative, tell the interviewer during planning and preserve equivalent evidence: a runnable HTTP API, a usable browser interface, business logic, data handling, validation and errors, and automated tests. Keep the documented user flow and API behavior unless you agree a justified change with the interviewer. You are responsible for having alternative tooling available; the provided installation and Docker commands support only the default stack. The same time box applies, so avoid spending the session rebuilding unnecessary boilerplate.

## Core user flow

Build as much of this flow as time allows:

1. View card-network fee records.
2. Filter records by scheme.
3. Filter records by country.
4. Enter or select an amount threshold.
5. Identify records whose amount exceeds that threshold.
6. Select a record.
7. View a deterministic explanation of why it may require review.

The explanation must use normal business logic, not a real LLM. A useful explanation can mention threshold status and percentage change from the previous period. Decide and explain how zero or missing previous amounts should behave.

The intended API surface is:

```text
GET /health
GET /fees
GET /fees?scheme=Visa
GET /fees?country=South%20Africa
GET /fees?scheme=Visa&country=South%20Africa
GET /fees/anomalies?threshold=10000
GET /fees/{fee_id}
GET /fees/{fee_id}/explanation?threshold=10000
```

Consider query validation, not-found behavior, useful error messages, and separation between route and business logic. On the frontend, consider loading, error, empty-results, selection, and review-indication states.

## Run the default backend

From the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r backend/requirements-dev.txt
python -m uvicorn backend.app.main:app --reload --port 8000
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. The health endpoint is <http://localhost:8000/health> and API documentation is at <http://localhost:8000/docs>.

## Run the default frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open <http://localhost:5173>.

## Run tests

From the repository root with the Python virtual environment active:

```bash
python -m pytest backend
```

From `frontend/`:

```bash
npm test -- --run
npm run build
```

## Docker alternative

From the repository root:

```bash
docker compose up --build
```

Docker is optional. Native startup is equally acceptable.

## Data and security

All included records are fictional. Do not paste real company, client, or personal data into external LLMs. For any production LLM use, consider what the provider receives, retention and model-training policies, redaction, and output validation. Business-rule calculations should remain deterministic; generated explanations must never be accepted as an unquestioned source of truth.

## Optional stretch goals

Only attempt these after a useful core flow works:

- sorting or pagination;
- CSV upload;
- additional tests;
- accessible table markup;
- URL-based filters;
- Docker improvements;
- caching;
- configurable percentage-change threshold;
- a mocked LLM explanation service;
- explanation audit metadata.
