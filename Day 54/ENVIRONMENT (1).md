# LearnInsight AI — Environment Reference (ENVIRONMENT.md)

**Status:** Day 3 — Foundation Complete

---

## 1. Environment Variables

| Variable | Where Defined | Required | Purpose |
|---|---|---|---|
| `GEMINI_API_KEY` | `backend/.env` (local, git-ignored) | Yes | Authenticates all Gemini API calls made from `ai_service.py` (built Day 4). Loaded via `python-dotenv`'s `load_dotenv()` in `app.py`. |

**Template file (`backend/.env.example` — safe to commit):**
```
GEMINI_API_KEY=your_gemini_api_key_here
```

**Production (Day 10):** the same `GEMINI_API_KEY` variable will be set directly in Render's dashboard (Environment tab) — never in a committed file — when the backend is deployed.

---

## 2. Tools & Runtime Versions

| Tool | Version | Notes |
|---|---|---|
| Python | 3.13.9 | Confirmed via `python --version` |
| pip | Bundled with Python 3.13.9 | Package manager |
| Flask | 3.1.3 | Web framework |
| flask-cors | 6.0.5 | Cross-origin request handling |
| python-dotenv | 1.2.2 | Loads `.env` into environment variables |
| google-genai | (current, installed Day 4) | **Replaces** deprecated `google-generativeai` — see Section 4.1 (resolved) |
| PyPDF2 | 3.0.1 | PDF text extraction |
| python-docx | 1.2.0 | DOCX text extraction |

Full pinned list (including transitive dependencies) is in `backend/requirements.txt`.

**Gemini Model in Use:** `gemini-3.5-flash` — confirmed working as of Day 4. (`gemini-2.0-flash`, used in the original Day 3 test script, was shut down by Google on June 1, 2026 — this was the actual root cause of Day 3's errors, not a quota lockout.)

---

## 3. Local Configuration Files

| File | Committed? | Purpose |
|---|---|---|
| `backend/.env` | ❌ No (git-ignored) | Real secrets (API key) |
| `backend/.env.example` | ✅ Yes | Template showing required variable names |
| `backend/.gitignore` | ✅ Yes | Excludes `venv/`, `.env`, `__pycache__/`, `*.db`, `*.pyc` from version control |
| `backend/requirements.txt` | ✅ Yes | Exact dependency versions for reproducible installs (including on Render) |

---

## 4. Known Issues & Action Items

### 4.1 Deprecated Gemini SDK — ✅ RESOLVED (Day 4)
`google-generativeai` was deprecated in favor of `google-genai`. **Resolved on Day 4:** uninstalled the old package, installed `google-genai`, and rewrote all Gemini calls using the new `from google import genai` / `genai.Client()` pattern in `ai_service.py`.

### 4.2 Gemini Free-Tier Quota — ✅ RESOLVED (Day 4, was a model-name issue, not quota)
The Day 3 `RESOURCE_EXHAUSTED` and "unsupported model" errors were caused by `gemini-2.0-flash` having been shut down by Google on June 1, 2026 — not an actual quota lockout on the account. **Resolved on Day 4:** switched to `gemini-3.5-flash`, confirmed working via `test_gemini.py` and subsequently via live Summary/Explanation generation.

### 4.3 Transient 503 "Model Overloaded" Errors — ✅ RESOLVED (Day 4)
During testing, Gemini occasionally returned `503 UNAVAILABLE` ("This model is currently experiencing high demand"). This is expected, transient behavior on shared model capacity — not an application bug. **Resolved on Day 4:** added retry logic with exponential backoff (2s → 4s → 8s, up to 3 attempts) in `ai_service.py`'s `_generate_with_retry()`, which retries only on transient errors (503/429) and fails fast on genuine errors (e.g., bad API key).

### 4.4 Markdown Formatting in AI Output — ✅ RESOLVED (Day 4)
Gemini occasionally returned `**bold**` Markdown syntax in Summary/Explanation text, which rendered as literal asterisks in the plain-text frontend. **Resolved on Day 4:** added a `_clean_markdown()` helper in `ai_service.py` that strips `**`, `__`, and `#` heading symbols, plus explicit "no Markdown formatting" instructions in both prompts.

### 4.5 GitHub Connection — Still Deferred
The project continues to live outside the existing 60-Day Challenge Git repository (see `PROJECT-STRUCTURE.md`). This remains an explicit, intentional decision to keep momentum on core implementation — no environment/config impact. Will be connected once core implementation is complete and stable, per Day 4 discussion.
