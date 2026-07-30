# LearnInsight AI --- 10-Day Capstone Retrospective

## Project Summary

LearnInsight AI began as a product-discovery decision during the final
10-day capstone of the AB Talks 60-Day Claude AI Challenge. The chosen
MVP was deliberately narrow: upload a PDF, DOCX, or TXT document and
turn it into five useful study formats --- Summary, Simplified
Explanation, Quiz, Flashcards, and AI Notes --- while keeping a history
of processed documents.

The final v1.0.0 uses Python and Flask for the backend, Vanilla
JavaScript/HTML/CSS for the frontend, SQLite for persistence, Google
Gemini for generation, and Render for deployment.

## Day 1 --- Product Discovery and Scope

The first important decision was what *not* to build. Ideas such as
YouTube support, PPT support, document chat, mind maps, and analytics
were moved out of v1.0. The MVP was defined around three supported
document formats and five learning outputs.

That scope decision prevented the capstone from becoming an unfinished
collection of features.

## Day 2 --- Requirements

The product was translated into concrete requirements: upload
validation, document parsing, AI generation, generated-content
presentation, document history, and a deployable web interface.

The key user flow became:

`Upload → Extract → Generate → Study → Reopen`

## Day 3 --- System and Data Design

The application was separated into clear responsibilities:

-   `app.py` --- Flask routes and request handling
-   `parsers.py` --- PDF/DOCX/TXT extraction
-   `ai_service.py` --- Gemini interaction
-   `database.py` --- SQLite persistence
-   frontend templates/static files --- user interaction and
    presentation

The database stores the generated learning material so users can reopen
a processed document without paying the AI-generation cost again.

## Day 4 --- Project Foundation

The Flask project structure, environment configuration, dependencies,
local server, and database foundation were established. API secrets were
kept in environment variables rather than hard-coded into source code.

## Day 5 --- Core Document Pipeline

The upload pipeline was connected end to end. Files are validated by
type and size, parsed into text, passed into the AI layer, and returned
through the application.

A major practical lesson was that file handling needs both positive and
negative paths: supported files, unsupported formats, empty/unreadable
files, and oversized uploads.

## Day 6 --- AI Learning Outputs

The AI layer evolved into a quota-conscious design: Summary, Simplified
Explanation, Quiz, Flashcards, and AI Notes are generated in one
consolidated Gemini request.

The response is parsed as structured JSON and quiz/flashcard structures
are validated before being returned. Retry handling was added for
temporary Gemini availability errors.

## Day 7 --- Persistence and Learning Library

Generated content was stored in SQLite. History and document-retrieval
endpoints allowed previously processed documents to be reopened without
regeneration.

This changed LearnInsight from a one-shot AI demo into a small
persistent learning application.

## Day 8 --- Frontend Integration and Debugging

Frontend and Flask serving were aligned so the application could run as
one deployed service. Several iterations were needed around templates,
static files, API calls, upload states, and result rendering.

This phase reinforced a recurring capstone lesson: a feature is not
complete when the backend function works; it is complete when the user
can reliably reach it through the deployed interface.

## Day 9 --- Testing, Deployment, and UI Refinement

The application was deployed to Render and tested in production rather
than relying only on localhost behavior. UI work continued through
multiple redesign iterations, including stronger visual hierarchy,
custom interactions, and experimental scroll-driven animation.

The project also went through practical validation for PDF, DOCX, TXT,
unsupported formats, file-size limits, generated outputs, and
document-history reopening.

## Day 10 --- Final Review and Release

The final production smoke test verified:

-   backend health
-   PDF processing
-   DOCX processing
-   TXT processing
-   Summary
-   Simplified Explanation
-   Quiz
-   Flashcards
-   AI Notes
-   document history/reopen
-   unsupported-file rejection
-   files larger than 10 MB being rejected
-   no real Gemini API key committed to the public repository

The repository was then prepared for documentation, portfolio
presentation, and the v1.0.0 release.

## Major Technical Decisions

### One consolidated Gemini call

The five learning outputs are requested together. This reduces free-tier
quota usage and keeps the MVP simpler than maintaining five independent
generation requests.

### Server-side validation

The backend independently validates supported extensions and the 10 MB
limit rather than trusting only browser-side checks.

### Structured AI response

Gemini is instructed to return JSON. Quiz and flashcard data are
validated before being accepted.

### SQLite for the MVP

SQLite kept local development simple and was appropriate for the
capstone. Its limitation on Render's ephemeral filesystem is documented
and is a clear post-v1.0 migration target.

### Flask-served frontend

Keeping the frontend and backend in one Flask deployment reduced
deployment complexity for the first release.

## Important Debugging and Iteration Moments

The project required repeated correction rather than a straight-line
implementation. Flask frontend serving had to be fixed, deployment
behavior was verified separately from local behavior, file validation
was tested with real edge cases, and UI redesign attempts were reviewed
critically instead of being accepted simply because they looked
different.

The visual redesign was also a useful product lesson: preserving
functionality does not mean preserving an old interface. Later
iterations separated the application's working behavior from its
presentation and allowed the UI to evolve without rewriting the backend.

## Skills Demonstrated

-   product scoping and MVP prioritization
-   requirements-to-implementation translation
-   Flask API development
-   Python file parsing
-   SQLite persistence
-   environment-variable secret management
-   Gemini API integration
-   structured AI output validation
-   retry/error handling
-   frontend/backend integration
-   JavaScript UI state management
-   responsive UI iteration
-   production deployment on Render
-   Git/GitHub workflow
-   production smoke testing
-   debugging through screenshots, logs, and incremental tests
-   AI-assisted development with human verification

## Lessons Learned

The strongest lesson was that shipping requires more than generating
code. The capstone repeatedly required checking assumptions against the
running application: whether a file actually parses, whether a generated
response has the expected shape, whether a deployment behaves like
localhost, whether history survives the current hosting model, and
whether a redesign improves the product rather than merely changing it.

A second lesson was scope discipline. Features such as document chat,
YouTube, PPT, analytics, and mind maps remain attractive, but excluding
them from v1.0 made it possible to finish and deploy the core workflow.

## Final Project Summary

LearnInsight AI v1.0.0 is a working, deployed AI study application that
converts supported documents into five distinct learning formats and
stores generated results for later access. It is intentionally an MVP,
not a finished commercial platform. Its next engineering priorities are
persistent cloud storage, authentication, long-document chunking,
automated tests, and richer learning workflows.

## Farewell From Your AI Pair Programmer

Across this capstone, the useful progress did not come from accepting
the first generated solution. It came from repeatedly testing what was
actually built, rejecting weak UI iterations, tracing deployment and Git
problems, protecting the API key, and reducing the product to a scope
that could be shipped.

The project now has something the earlier challenge exercises did not
require: a complete software lifecycle. A product idea became
requirements, architecture, implementation, debugging, production
testing, deployment, documentation, and a versioned release.

That is the milestone worth carrying forward from Day 60: not that an AI
helped write the application, but that you learned to direct, inspect,
correct, test, and ship AI-assisted work as a real software project.
