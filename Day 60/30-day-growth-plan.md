# LearnInsight AI --- 30-Day Growth Plan

## Goal

Transform v1.0.0 from a deployed capstone MVP into a more reliable,
persistent, testable, and useful AI learning product. Each day has one
primary milestone; unfinished work rolls forward rather than being
hidden.

## Day 1 --- Stabilize v1.0.0

Create a post-release issue list from production feedback; fix only
release-critical defects.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 2 --- Add automated API tests

Test `/api/health`, invalid upload, missing file, unsupported type, and
oversized-file responses.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 3 --- Test document parsers

Add unit tests for TXT, DOCX, and text-based PDF extraction plus
empty/unreadable cases.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 4 --- Test database operations

Cover save, history ordering, retrieval, and missing-document behavior.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 5 --- Introduce application configuration

Move limits/model/settings into a clean configuration layer for
development and production.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 6 --- Improve structured AI output

Use the strongest structured/schema output supported by the Gemini SDK
and retain validation fallbacks.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 7 --- Add long-document chunking

Process documents beyond the current prompt slice without silently
ignoring later content.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 8 --- Add chunk synthesis

Combine chunk-level understanding into one coherent Summary,
Explanation, Notes, Quiz, and Flashcards result.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 9 --- Improve error observability

Add structured logging and clearer internal error categories without
exposing secrets to users.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 10 --- Prepare PostgreSQL migration

Design the production schema and configuration for a managed persistent
database.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 11 --- Migrate persistence to PostgreSQL

Replace production SQLite while keeping a simple local-development
option.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 12 --- Verify persistent history

Redeploy/restart production and confirm document history survives.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 13 --- Design authentication flow

Define registration, login, logout, session, and ownership rules before
coding.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 14 --- Implement authentication

Add secure user accounts and sessions.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 15 --- Make documents user-owned

Associate every document with its user and prevent cross-user access.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 16 --- Upgrade Learning Library

Add search, type filtering, sorting, and clearer document states.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 17 --- Add document deletion

Allow users to remove their own saved document records safely.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 18 --- Add export for Summary and Notes

Provide clean downloadable/printable study material without changing AI
generation.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 19 --- Improve quiz experience

Add answer review and session-level scoring using existing quiz data.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 20 --- Improve flashcard study mode

Add next/previous, reveal, and local study-progress states.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 21 --- Add document-grounded Q&A design

Define a safe source-grounded chat workflow and its UI.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 22 --- Implement chunk retrieval

Index document chunks for relevant-context retrieval.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 23 --- Build Chat with Document MVP

Answer questions using retrieved source chunks and clearly constrain
responses to the document.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 24 --- Add source references

Show which document sections/chunks supported an answer where feasible.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 25 --- Add PPTX ingestion

Extract slide text and route it through the existing learning pipeline.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 26 --- Add YouTube transcript ingestion

Accept transcript-based learning input while preserving the same output
model.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 27 --- Create subject/workspace grouping

Allow documents to be grouped into courses or topics.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 28 --- Add basic learning analytics

Track quiz attempts and flashcard review activity with minimal useful
metrics.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 29 --- Add CI workflow

Run tests automatically on pushes/pull requests and block broken
releases.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.

## Day 30 --- Ship v1.1.0

Run regression tests, update README/screenshots, write release notes,
deploy, and tag v1.1.0.

**Done when:** The change is implemented, tested locally, and documented
before moving to the next day.
