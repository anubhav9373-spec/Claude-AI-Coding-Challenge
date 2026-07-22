# LearnInsight AI — API Design

**Status:** Approved — Day 2 Design
**Base URL (local):** `http://localhost:5000`
**Base URL (production):** Render-assigned URL, configured in `frontend/script.js` on Day 10
**Authentication:** None in v1.0 (single-user, no accounts)
**Format:** All requests/responses use JSON, except file upload which uses `multipart/form-data`.

> **Implementation note:** During Days 4–5, individual endpoints (`/api/generate/summary`, `/api/generate/quiz`, etc.) may be built and tested in isolation for easier debugging of each AI feature, exactly as described in the Blueprint. By Day 6, these are consolidated behind the single `POST /api/process` endpoint below, which represents the **final v1.0 API contract**. This document describes that final contract.

---

## 1. `GET /api/health`

**Purpose:** Confirm the backend service is running and reachable. Used in Day 2 setup and as a general uptime check.

- **Request:** No parameters.
- **Response (200):**
  ```json
  { "status": "ok" }
  ```
- **Validation:** None required.
- **Authentication:** None.
- **Error Cases:** None expected — if the server is unreachable, the frontend's `fetch()` call itself fails (network error), which the frontend handles as a generic connectivity error.

---

## 2. `POST /api/process`

**Purpose:** The core endpoint. Accepts an uploaded document, extracts its text, generates all five AI learning artifacts, saves the complete record, and returns it.

- **Request:** `multipart/form-data` with a single field:
  | Field | Type | Required | Notes |
  |---|---|---|---|
  | `file` | File | Yes | Must be `.pdf`, `.docx`, or `.txt`. Max size 10MB. |

- **Response (200):**
  ```json
  {
    "id": 14,
    "filename": "chapter3_notes.pdf",
    "upload_date": "2026-07-23T10:15:00Z",
    "summary": "...",
    "explanation": "...",
    "quiz": [
      { "question": "...", "options": ["A", "B", "C", "D"], "correct_answer": "B", "explanation": "..." }
    ],
    "flashcards": [
      { "front": "...", "back": "..." }
    ],
    "notes": "..."
  }
  ```

- **Validation:**
  - File extension must be one of `pdf`, `docx`, `txt` → else `400`.
  - File size must not exceed 10MB → else `413`.
  - Extracted text must not be empty/near-empty → else `422`.

- **Authentication:** None.

- **Error Cases:**
  | Status | Condition | Body |
  |---|---|---|
  | 400 | Unsupported file type / no file provided | `{ "error": "Unsupported file type. Please upload a PDF, DOCX, or TXT file." }` |
  | 413 | File exceeds size limit | `{ "error": "File is too large. Maximum size is 10MB." }` |
  | 422 | File parsed but contains no usable text | `{ "error": "This file appears to be empty or unreadable. Please try a different file." }` |
  | 502 | Gemini API failure (timeout, rate limit, malformed response) at any generation step | `{ "error": "AI generation is temporarily unavailable. Please try again in a moment." }` |
  | 500 | Any unhandled server error | `{ "error": "Something went wrong processing your document." }` |

---

## 3. `GET /api/history`

**Purpose:** Return a lightweight list of previously processed documents for the dashboard's history view.

- **Request:** No parameters.
- **Response (200):**
  ```json
  {
    "documents": [
      { "id": 14, "filename": "chapter3_notes.pdf", "upload_date": "2026-07-23T10:15:00Z" },
      { "id": 13, "filename": "biology_intro.docx", "upload_date": "2026-07-22T18:42:00Z" }
    ]
  }
  ```
  Ordered by `upload_date DESC` (most recent first). Returns `{ "documents": [] }` if none exist yet (frontend renders the empty state).

- **Validation:** None required.
- **Authentication:** None.
- **Error Cases:**
  | Status | Condition | Body |
  |---|---|---|
  | 500 | Database read failure | `{ "error": "Could not load document history." }` |

---

## 4. `GET /api/document/<id>`

**Purpose:** Return the complete saved record for one past document, so the user can revisit its generated materials without reprocessing.

- **Request:** Path parameter `id` (integer).
- **Response (200):** Same shape as `POST /api/process`'s response.
- **Validation:** `id` must be a positive integer → else `400`. Must correspond to an existing record → else `404`.
- **Authentication:** None.
- **Error Cases:**
  | Status | Condition | Body |
  |---|---|---|
  | 400 | `id` is not a valid integer | `{ "error": "Invalid document ID." }` |
  | 404 | No document exists with that `id` | `{ "error": "Document not found." }` |
  | 500 | Database read failure | `{ "error": "Could not load this document." }` |

---

## 5. Endpoint Summary Table

| Method | Path | Purpose | Auth |
|---|---|---|---|
| GET | `/api/health` | Service uptime check | None |
| POST | `/api/process` | Upload, parse, generate all 5 outputs, save | None |
| GET | `/api/history` | List past documents | None |
| GET | `/api/document/<id>` | Retrieve one full past document record | None |

Four endpoints, matching exactly the PRD's functional scope — no unused or speculative endpoints included.

---

## 6. Error Response Convention

Every error response follows the same shape across all endpoints:
```json
{ "error": "Human-readable message safe to display directly in the UI." }
```
This lets the frontend handle all API errors with one shared code path (extract `error` field, display it) rather than special-casing each endpoint — directly supporting the Day 8 polish work on error states.
