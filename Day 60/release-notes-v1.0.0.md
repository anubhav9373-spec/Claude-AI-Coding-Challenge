# LearnInsight AI v1.0.0

LearnInsight AI v1.0.0 is the first production-ready capstone release.

## Highlights

-   Upload and process PDF, DOCX, and TXT documents
-   10 MB server-side upload limit
-   AI-generated Summary
-   Simplified Explanation
-   Interactive Quiz
-   Flashcards
-   Structured AI Notes
-   Learning Library with saved document results
-   Reopen previously generated learning material without regeneration
-   Structured Gemini JSON response handling
-   Quiz and flashcard validation
-   Retry/error handling for AI-service failures
-   Responsive web interface
-   Flask production deployment on Render
-   Environment-variable API key configuration

## Stack

Python, Flask, Google Gemini API, SQLite, HTML, CSS, Vanilla JavaScript,
Gunicorn, Render.

## Known v1.0 Limitations

-   Render free-tier services can cold-start after inactivity.
-   SQLite data on an ephemeral Render filesystem can reset after
    service restart/redeployment.
-   Long-document AI input is currently bounded rather than fully
    chunked.
-   v1.0 does not include authentication, document chat, PPT support,
    YouTube support, or persistent cloud database storage.

These are roadmap items rather than hidden production claims.

## Verification

Before release, the production application was smoke-tested for PDF,
DOCX, TXT, all five generated outputs, history/reopen, unsupported-file
validation, files over 10 MB, and public-repository secret exposure.
