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
| google-generativeai | 0.8.6 | **Deprecated** — see Section 4 |
| PyPDF2 | 3.0.1 | PDF text extraction |
| python-docx | 1.2.0 | DOCX text extraction |

Full pinned list (including transitive dependencies) is in `backend/requirements.txt`.

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

### 4.1 Deprecated Gemini SDK
`google-generativeai` is deprecated in favor of `google-genai`. The Day 3 test script (`test_gemini.py`) uses the deprecated package (it was the version specified in the original Blueprint). **Recommendation:** before Day 4's `ai_service.py` is built, evaluate switching to `google-genai` to avoid building the core AI feature set on a deprecated dependency. This is a small, contained change (different import and client initialization syntax) and does not affect any other architectural decision.

### 4.2 Gemini Free-Tier Quota
Testing on Day 3 returned:
```
grpc._channel._InactiveRpcError: ... RESOURCE_EXHAUSTED
Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-2.0-flash
```
This indicates the connected Google Cloud project currently has a **0 quota** for free-tier requests on this model — not a bug in our code (the request successfully reached Google's servers and returned a structured, correctly-parsed error). **Action item before Day 4:** check the quota/billing configuration at `https://aistudio.google.com` and `https://ai.dev/rate-limits` (referenced directly in the error message) to confirm free-tier access is properly enabled for this project.

### 4.3 GitHub Connection Deferred
The project currently lives outside the existing 60-Day Challenge Git repository (see `PROJECT-STRUCTURE.md` for full detail). No environment/config impact — this is purely a version-control workflow item to resolve before pushing any commits.
