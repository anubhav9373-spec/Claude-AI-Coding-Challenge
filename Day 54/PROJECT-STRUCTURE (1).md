# LearnInsight AI — Project Structure (Updated Day 4)

**Status:** Updated to reflect actual Day 4 implementation state

---

## 1. Current Actual Structure

```
C:\Users\anubh\Desktop\Learninsight-AI\          ← still NOT connected to the 60-Day Challenge repo (deferred by choice)
│
├── backend/
│   ├── venv/                        ← Python virtual environment (git-ignored)
│   ├── app.py                       ← Flask app; /api/health, /api/upload, /api/generate/summary, /api/generate/explanation
│   ├── parsers.py                   ← PDF/DOCX/TXT text extraction (built Day 4, carried over from Day 3 scope)
│   ├── ai_service.py                ← NEW (Day 4): all Gemini calls, prompts, retry logic, Markdown cleanup
│   ├── test_gemini.py               ← Gemini connectivity test script (updated Day 4 to use google-genai)
│   ├── requirements.txt             ← Frozen dependency versions (updated Day 4: google-genai replaces google-generativeai)
│   ├── .env                         ← Contains real GEMINI_API_KEY (git-ignored, never committed)
│   ├── .env.example                 ← Safe template, committable
│   └── .gitignore                   ← Excludes venv/, .env, __pycache__/, *.db, *.pyc
│
└── frontend/
    ├── index.html                   ← Updated Day 4: upload form + tabbed results (Summary / Explanation / Extracted Text)
    ├── style.css                    ← Updated Day 4: tab styling
    └── script.js                    ← Updated Day 4: upload → extract → generate Summary + Explanation, tab switching
```

Not yet created (scheduled for later days per the Blueprint): `database.py` (Day 6), quiz/flashcard generation logic (Day 5), `README.md` / `TESTING_NOTES.md` (Days 9–10).

---

## 2. What Changed Since Day 3

| File | Change |
|---|---|
| `backend/parsers.py` | New — carried over from Day 3's originally-scheduled scope, built at the start of Day 4 |
| `backend/ai_service.py` | New — isolates all Gemini API calls per `ARCHITECTURE.md`'s design |
| `backend/app.py` | Added `/api/upload`, `/api/generate/summary`, `/api/generate/explanation` routes |
| `backend/test_gemini.py` | Rewritten to use `google-genai` instead of deprecated `google-generativeai` |
| `frontend/index.html`, `script.js`, `style.css` | Rebuilt to support upload → AI generation → tabbed results display |

No structural folder changes — `backend/` and `frontend/` remain siblings exactly as designed on Day 2.

---

## 3. Validation Against Architecture & API Design

| Design Document | Requirement | Day 4 Status |
|---|---|---|
| `ARCHITECTURE.md` | Gemini calls isolated in `ai_service.py` | ✅ Confirmed |
| `API.md` | `/api/generate/summary`, `/api/generate/explanation` as intermediate endpoints before Day 6 consolidation | ✅ Confirmed, matches documented plan exactly |
| `API.md` | Consistent error response shape (`{"error": "..."}`) | ✅ Confirmed across all routes |

No design deviations required — only the model name (`gemini-3.5-flash` vs. an unspecified placeholder) and SDK package (`google-genai` vs. `google-generativeai`) were finalized in practice, both anticipated as implementation-level details rather than architectural decisions.
