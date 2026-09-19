# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This is "Spendly," a Flask expense tracker being built incrementally as a step-by-step course project. Most backend logic does not exist yet — `app.py` routes like `/logout`, `/profile`, `/expenses/add`, `/expenses/<id>/edit`, and `/expenses/<id>/delete` are placeholders that return plain strings with comments like `"coming in Step N"`. `database/db.py` is currently just a comment describing what it should contain (Step 1). Do not assume functionality exists just because a route or file is present — check whether it's still a placeholder.

## Commands

Activate the venv before running anything (Windows):
```
venv\Scripts\activate
```

Run the dev server (serves on port 5001, debug mode on):
```
python app.py
```

Run tests (pytest + pytest-flask are installed, but no test files exist yet):
```
pytest
```

Install dependencies:
```
pip install -r requirements.txt
```

There is no lint/format tooling configured in this repo.

## Architecture

- **`app.py`** — single Flask application file; all routes are defined here (no blueprints). This is the natural place to add new routes as features are built out.
- **`database/db.py`** — intended to hold `get_db()` (SQLite connection with `row_factory` and foreign keys enabled), `init_db()` (creates tables with `CREATE TABLE IF NOT EXISTS`), and `seed_db()` (sample data for development). None of this is implemented yet.
- **`templates/`** — Jinja2 templates. `base.html` defines the shared layout (nav, footer, font/CSS includes) via `{% block title %}`, `{% block content %}`, `{% block head %}`, and `{% block scripts %}`; page templates (`landing.html`, `login.html`, `register.html`, `terms.html`, `privacy.html`) extend it.
- **`static/css/style.css`** / **`static/js/main.js`** — global stylesheet and script, both linked from `base.html`. `main.js` is currently empty aside from a placeholder comment; JS is added per-feature as steps are implemented.
- No database file, ORM, or auth/session layer exists yet — routes currently just render templates with no data.
