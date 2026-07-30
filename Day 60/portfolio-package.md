# LearnInsight AI --- Portfolio Package

## Portfolio Project Description

**LearnInsight AI** is a deployed AI-powered study application that
transforms PDF, DOCX, and TXT documents into five learning formats: a
concise summary, simplified explanation, interactive quiz, flashcards,
and structured AI notes. I built the application as a 10-day
software-development capstone, covering product scoping, architecture,
Flask API development, document parsing, Gemini integration, SQLite
persistence, frontend integration, validation, production testing, and
deployment on Render.

To reduce AI quota usage, the generation layer produces all five
learning outputs in a single structured Gemini request, validates quiz
and flashcard data, and includes retry/error handling. Processed results
are stored so users can reopen them without regenerating content.

**Stack:** Python, Flask, Google Gemini API, SQLite, HTML, CSS, Vanilla
JavaScript, Render.

## Resume Bullets

-   Built and deployed **LearnInsight AI**, a Flask-based
    document-learning application that converts PDF, DOCX, and TXT files
    into summaries, simplified explanations, quizzes, flashcards, and
    structured study notes using Google Gemini.
-   Designed a quota-efficient AI pipeline that generates **five
    learning outputs in one structured API request**, validates
    generated quiz/flashcard schemas, and handles transient AI-service
    failures.
-   Implemented server-side file validation, multi-format text
    extraction, SQLite document history, REST endpoints, responsive
    frontend states, and production deployment/testing on Render.
-   Executed a complete 10-day SDLC workflow from requirements and
    architecture through implementation, debugging, security checks,
    deployment, documentation, and v1.0.0 release preparation.

## Interview Talking Points

### 30-second explanation

LearnInsight AI solves the problem of turning long study documents into
multiple revision formats. A user uploads a PDF, DOCX, or TXT file;
Flask validates and parses it; Gemini generates five structured learning
outputs in one request; and the result is stored in SQLite so it can be
reopened later.

### Why one Gemini call?

The project was built under free-tier constraints. Five separate calls
would consume quota faster and create more failure points, so the
outputs are generated together as structured JSON and validated before
use.

### What was technically difficult?

The hardest part was not one algorithm; it was integrating the full
pipeline reliably: browser upload, server validation, file parsing, AI
response parsing, malformed-response handling, persistence, frontend
rendering, and then verifying the same flow after deployment.

### What would you change for production scale?

Move production persistence from SQLite to managed PostgreSQL, add
authentication and per-user ownership, chunk long documents, add
automated tests/CI, and introduce retrieval for document-grounded chat.

### What did you learn from deployment?

Local success is not enough. Production introduced hosting constraints
such as service cold starts and ephemeral filesystem behavior, so the
deployment model had to be documented and tested explicitly.

## Short Demo Script

"LearnInsight AI turns a study document into a complete revision
workspace. I'll upload a supported PDF. The Flask backend validates and
extracts the document text, then a single Gemini request generates five
outputs. Here is the Summary for quick review, the Simplified
Explanation for easier understanding, an interactive Quiz, Flashcards
for revision, and structured AI Notes. The processed document is also
saved in the Learning Library, so I can reopen the generated material
without processing the file again. The application supports PDF, DOCX,
and TXT files and is deployed on Render."

## Recommended Screenshots / Demo Media

1.  **Hero + Upload Workspace** --- clean first impression with
    supported formats visible.
2.  **Generated Summary** --- show real readable output after
    processing.
3.  **Quiz** --- demonstrate that the product is more than a summarizer.
4.  **Flashcards** --- visually distinctive learning feature.
5.  **Learning Library** --- prove persistence/reopen workflow.
6.  **Short screen recording (30--45 seconds)** --- upload → processing
    → outputs → reopen from library.

Do not include screenshots containing API keys, browser developer
secrets, local file paths, or test data that should remain private.

## GitHub About Description

AI-powered document learning platform that transforms PDF, DOCX, and TXT
files into summaries, explanations, quizzes, flashcards, and study
notes.

## Recommended GitHub Topics

`ai` `generative-ai` `gemini` `flask` `python` `edtech`
`document-processing` `quiz-generator` `flashcards` `ai-learning`

## Repository Metadata

-   **Website:** https://learninsight-ai.onrender.com
-   **License:** MIT
-   **Release:** v1.0.0
-   **Primary language:** Python
