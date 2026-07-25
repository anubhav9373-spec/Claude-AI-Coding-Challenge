# LearnInsight AI — Project Structure (Updated Day 5)

**Status:** Updated to reflect actual Day 5 implementation state

---

## 1. Current Actual Structure

```
C:\Users\anubh\Desktop\Learninsight-AI\          ← still NOT connected to the 60-Day Challenge repo (deferred by choice)
│
├── backend/
│   ├── venv/                        ← Python virtual environment (git-ignored)
│   ├── app.py                       ← Flask app; /api/health, /api/upload, /api/generate/all
│   ├── parsers.py                   ← PDF/DOCX/TXT text extraction (Day 4)
│   ├── ai_service.py                ← UPDATED (Day 5): consolidated single-call generation (Summary+Explanation+Quiz+Flashcards)
│   ├── test_gemini.py               ← Gemini connectivity test script
│   ├── requirements.txt             ← Frozen dependency versions
│   ├── .env                         ← Contains real GEMINI_API_KEY (git-ignored, never committed)
│   ├── .env.example                 ← Safe template, committable
│   └── .gitignore                   ← Excludes venv/, .env, __pycache__/, *.db, *.pyc
│
└── frontend/
    ├── index.html                   ← Updated Day 5: added Quiz and Flashcards tabs
    ├── style.css                    ← Updated Day 5: quiz option styling, flip-card CSS animation
    └── script.js                    ← Updated Day 5: single consolidated fetch call, quiz scoring logic, flashcard flip/nav logic
```

Not yet created (scheduled for later days per the Blueprint): AI Notes generation, `database.py` (Day 6), `README.md` / `TESTING_NOTES.md` (Days 9–10).

---

## 2. What Changed Since Day 4

| File | Change |
|---|---|
| `backend/ai_service.py` | Replaced 4 separate generation functions with one `generate_all_content()` making a single Gemini call; added quota-aware error handling (429 no longer retried) |
| `backend/app.py` | Replaced 4 separate `/api/generate/*` routes with one `/api/generate/all` route |
| `frontend/index.html` | Added Quiz and Flashcards tabs |
| `frontend/script.js` | Replaced 4 sequential fetch calls with 1; added quiz rendering/scoring logic and flashcard flip/navigation logic |
| `frontend/style.css` | Added quiz option and flip-card styling |

No structural folder changes.

---

## 3. Key Architectural Decision — Consolidated AI Generation

**Why this matters going forward:** the Gemini free tier's 20 requests/day/model limit means every future feature addition (Day 6's AI Notes) must be added to the existing `generate_all_content()` prompt rather than introduced as a new separate call. This is now a hard constraint on the codebase, not just a Day 5 fix — documented here so it isn't accidentally reversed in a future session.

---

## 4. Validation Against Architecture & API Design

| Design Document | Requirement | Day 5 Status |
|---|---|---|
| `ARCHITECTURE.md` | Gemini calls isolated in `ai_service.py` | ✅ Confirmed, still true after consolidation |
| `API.md` | Final v1.0 contract is one consolidated endpoint (originally planned as `/api/process` by Day 6) | ✅ Consolidation arrived one day early, driven by the quota constraint — fully consistent with the documented plan, just accelerated |

No conflicts with existing design documents — the consolidation was already the planned end-state; Day 5 simply implemented it sooner than scheduled, out of necessity.
