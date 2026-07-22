# LearnInsight AI — Project Structure

**Status:** Approved — Day 2 Design

---

## 1. Full Folder Structure

```
learninsight-ai/                     ← shared, continuous project root (lives once in the repo)
│
├── backend/
│   ├── app.py                       ← Flask app entry point; all route definitions
│   ├── parsers.py                   ← PDF/DOCX/TXT text extraction functions
│   ├── ai_service.py                ← All Gemini API calls + prompt logic (isolated module)
│   ├── database.py                  ← SQLite schema init + save/get functions
│   ├── requirements.txt             ← Python dependencies (pinned versions)
│   ├── test_gemini.py               ← One-off Day 2 script to verify API key/connectivity
│   ├── .env                         ← Local-only secrets (GEMINI_API_KEY) — NEVER committed
│   ├── .env.example                 ← Template showing required env vars, safe to commit
│   ├── .gitignore                   ← Excludes venv/, .env, __pycache__/, *.db
│   └── learninsight.db              ← Auto-created SQLite file (git-ignored)
│
├── frontend/
│   ├── index.html                   ← Single HTML file containing both Dashboard and Results views
│   ├── style.css                    ← All styling: layout, colors, tabs, cards, responsiveness
│   └── script.js                    ← All frontend logic: fetch calls, view switching, quiz/flashcard interactivity
│
├── README.md                        ← Written on Day 10: overview, setup, screenshots, live demo link
└── TESTING_NOTES.md                 ← Written on Day 9: test cases run and issues found/fixed
```

Day-by-day progress documentation, screenshots, and notes are organized separately according to the user's own existing repository workflow (outside this project root) — not duplicated here.

---

## 2. What Each Major Folder Is Responsible For

### `backend/`
Everything server-side. Deployed as its own service on Render. Responsible for: accepting uploads, extracting text, calling Gemini, persisting data, and serving the four API endpoints defined in `API.md`.

### `frontend/`
Everything client-side. Deployed as its own static site on GitHub Pages. Responsible for: rendering the Dashboard and Results views, calling the backend API, and all interactive UI logic (quiz scoring, flashcard flipping, tab switching).

The frontend/backend split mirrors the two independent hosting targets decided in `ARCHITECTURE.md` — this is not an arbitrary convention, it's required by the deployment plan.

---

## 3. Where Future Code Will Live

| Day | New Files | Location |
|---|---|---|
| Day 2 | `app.py`, `requirements.txt`, `.env`, `.gitignore`, `test_gemini.py`, skeleton `index.html`/`style.css`/`script.js` | `backend/`, `frontend/` |
| Day 3 | `parsers.py`; upload route added to `app.py` | `backend/` |
| Day 4 | `ai_service.py` (Summary, Explanation functions) | `backend/` |
| Day 5 | Quiz/Flashcard functions added to `ai_service.py`; interactive JS added to `script.js` | `backend/`, `frontend/` |
| Day 6 | `database.py`; `/api/process`, `/api/history`, `/api/document/<id>` routes added to `app.py` | `backend/` |
| Day 7 | Full dashboard/results structure in `index.html`; view-switching logic in `script.js` | `frontend/` |
| Day 8 | Polish-only changes across existing `script.js`/`style.css`/`app.py` | `backend/`, `frontend/` |
| Day 9 | `TESTING_NOTES.md`; bug fixes across existing files | project root, `backend/`, `frontend/` |
| Day 10 | `README.md`; production config tweaks to `app.py`/`script.js` | project root, `backend/`, `frontend/` |

No new top-level folders are introduced after Day 2 — every remaining day adds files *within* this existing structure, which is intentional (see below).

---

## 4. Why This Structure Was Chosen

- **Two folders, one clear split:** `backend/` and `frontend/` map directly to the two independently deployed services (Render and GitHub Pages). This isn't just tidy organization — it's required, since each host needs to serve only its own folder's contents.
- **Flat file layout within `backend/`:** with only 4 core Python files (`app.py`, `parsers.py`, `ai_service.py`, `database.py`), a deeper folder hierarchy (e.g., `routes/`, `services/`, `models/` subfolders) would add navigation overhead with no real benefit at this scale. Flat is simpler and matches the beginner/intermediate comfort level.
- **Single-file frontend:** one `index.html`, one `style.css`, one `script.js` is appropriate for a 2-screen app with no build tooling. Splitting into multiple HTML files or JS modules would require either a bundler or manual `<script>` ordering — unnecessary complexity for this scope.
- **Secrets isolated and git-ignored from Day 2 onward:** `.env` / `.gitignore` are set up on the very first implementation day so there's no risk of accidentally committing the Gemini API key later under time pressure.
- **No premature subfolders for future features:** the Future Roadmap items (YouTube support, AI Chat, etc.) do **not** get placeholder folders today. Adding empty structure for unbuilt features would be scope creep in the *planning* sense — this structure reflects exactly v1.0, nothing more.

---

## 5. Validation Against Architecture & Blueprint

This structure matches every file path already referenced in `ARCHITECTURE.md`'s component diagram and every "Files & Folders to Create/Modify" list in the Day 2–10 Implementation Blueprint — no renaming or reorganization is required going into Day 3.
