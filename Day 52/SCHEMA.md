# LearnInsight AI — Database Schema

**Status:** Approved — Day 2 Design
**Engine:** SQLite (file: `learninsight.db`)

---

## 1. Design Philosophy

v1.0 is single-user with no authentication, so the schema is intentionally minimal: **one table** holds each processed document and all five of its generated AI artifacts together as a single record. This avoids premature normalization (e.g., splitting quiz questions into their own table) that would add joins and complexity with no current benefit — quizzes and flashcards are always read/written as a whole unit per document, never queried individually across documents in v1.0.

---

## 2. Table: `documents`

| Field | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier for the processed document. |
| `filename` | TEXT | NOT NULL | Original uploaded filename, shown in the history list. |
| `file_type` | TEXT | NOT NULL, CHECK (`file_type` IN ('pdf','docx','txt')) | Supported format the file was parsed as. |
| `upload_date` | TEXT | NOT NULL, DEFAULT CURRENT_TIMESTAMP | ISO 8601 timestamp of when the document was processed. |
| `extracted_text` | TEXT | NOT NULL | Raw text extracted from the uploaded file (kept for potential re-generation/debugging). |
| `summary` | TEXT | NOT NULL | AI-generated summary. |
| `explanation` | TEXT | NOT NULL | AI-generated simplified explanation. |
| `quiz` | TEXT (JSON) | NOT NULL | AI-generated quiz, stored as a JSON string: array of `{question, options[4], correct_answer, explanation}`. |
| `flashcards` | TEXT (JSON) | NOT NULL | AI-generated flashcards, stored as a JSON string: array of `{front, back}`. |
| `notes` | TEXT | NOT NULL | AI-generated structured notes. |

### SQL Definition

```sql
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    file_type TEXT NOT NULL CHECK (file_type IN ('pdf', 'docx', 'txt')),
    upload_date TEXT NOT NULL DEFAULT (datetime('now')),
    extracted_text TEXT NOT NULL,
    summary TEXT NOT NULL,
    explanation TEXT NOT NULL,
    quiz TEXT NOT NULL,
    flashcards TEXT NOT NULL,
    notes TEXT NOT NULL
);
```

---

## 3. Relationships

There is only one table in v1.0 — no foreign keys or joins are required. Quiz and flashcard data are stored as JSON blobs within the same row rather than as separate related tables, per the design philosophy above.

**Future Roadmap consideration (not v1.0):** if Progress Tracking or multi-user accounts are added later, this schema would extend with a `users` table (`id`, `username`, ...) and a foreign key `user_id` on `documents`, plus a `quiz_attempts` table (`id`, `document_id`, `score`, `attempted_at`) to support tracking performance over time. No schema changes are needed now to accommodate this later — it's an additive extension.

---

## 4. Constraints & Validation Rules

- `file_type` is constrained to the three supported formats at the database level as a safety net, in addition to backend validation before insertion.
- `filename`, `extracted_text`, `summary`, `explanation`, `quiz`, `flashcards`, and `notes` are all `NOT NULL` — a document record is only ever saved after **all five** AI generations succeed, so there should never be a partially-complete row. If any generation step fails, the backend does not call `save_document()` at all; it returns an error to the frontend instead.
- `quiz` and `flashcards` are validated as well-formed JSON in the backend (`ai_service.py`) *before* being passed to `database.py` — the database itself does not validate JSON structure (SQLite has no native JSON column type), so this responsibility lives in the application layer.

---

## 5. Schema Validation Against PRD User Stories

| PRD User Story / Requirement | Supported By |
|---|---|
| User uploads a PDF/DOCX/TXT file | `file_type` field with CHECK constraint |
| System generates and displays a Summary | `summary` field |
| System generates and displays a Simplified Explanation | `explanation` field |
| System generates an interactive Quiz | `quiz` field (JSON, parsed by frontend) |
| System generates Flashcards | `flashcards` field (JSON, parsed by frontend) |
| System generates AI Notes | `notes` field |
| History Dashboard lists past uploads with filename + date | `id`, `filename`, `upload_date` (returned via `GET /api/history`) |
| User can revisit a past document's full results | Full row lookup via `id` (returned via `GET /api/document/<id>`) |
| Data persists across sessions/restarts | SQLite file-based storage, not in-memory |

Every functional requirement in the PRD's Feature Requirements section (6.1–6.7) maps directly to a field or query against this single table — no gaps identified.

---

## 6. Indexing Notes

No additional indexes are needed for v1.0. The `id` primary key is auto-indexed, and `GET /api/history` is expected to return, at most, a small number of rows for a single-user demo — a full table scan ordered by `upload_date DESC` is more than performant enough at this scale.
