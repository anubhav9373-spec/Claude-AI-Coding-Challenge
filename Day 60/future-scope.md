# LearnInsight AI --- Future Scope

## Current v1.0.0 Baseline

LearnInsight AI v1.0.0 is a deployed document-learning application built
with Flask, SQLite, Vanilla JavaScript, and the Google Gemini API. It
accepts PDF, DOCX, and TXT files up to 10 MB and generates five learning
outputs in one consolidated AI request: Summary, Simplified Explanation,
Quiz, Flashcards, and AI Notes. Processed documents can be reopened from
the Learning Library.

The next phase should improve persistence, learning depth, reliability,
and product usability without losing the simplicity of the current
workflow.

## Next 3 Months --- Make the MVP Reliable and Personal

### 1. Persistent cloud database

Replace local SQLite persistence in production with PostgreSQL so
document history survives Render restarts and redeployments.

### 2. User authentication

Add secure sign-up/login and associate each document with its owner. The
Learning Library should become private per user.

### 3. Better document processing

Add chunking for long documents instead of limiting AI context to the
first portion of extracted text. Preserve headings and document
structure where possible.

### 4. Improved AI generation pipeline

Keep quota efficiency, but introduce schema-based structured output,
stronger validation, and graceful recovery when one generated section is
malformed.

### 5. Learning experience upgrades

Add quiz answer review, flashcard progress, copy/export actions, and
clearer study-session states.

### 6. Automated testing

Add unit tests for parsers, database operations, validation, and API
endpoints plus a small integration test for the document-processing
flow.

## Next 6 Months --- Turn It Into a Real Study Workspace

### 1. Chat with documents

Allow users to ask grounded questions about an uploaded document while
keeping answers tied to source content.

### 2. Multi-document study spaces

Let users group related documents into subjects or courses and generate
combined study material.

### 3. YouTube learning support

Accept a YouTube transcript and transform it through the same Summary,
Explanation, Quiz, Flashcards, and Notes pipeline.

### 4. PPT/PPTX support

Extend document ingestion to lecture slides while preserving slide-level
context.

### 5. Search and organization

Add document search, filters, folders/tags, sorting, and favorites.

### 6. Export

Export generated notes, summaries, quizzes, and flashcards to PDF or
printable study sheets.

### 7. Learning analytics

Track quiz performance, reviewed flashcards, weak topics, and study
activity without turning the product into a noisy dashboard.

## Next 12 Months --- Evolve Into an AI Learning Platform

### 1. Retrieval-Augmented Generation

Introduce embeddings and a vector store so questions and generated study
material can retrieve relevant chunks from large document collections.

### 2. Adaptive learning

Use quiz and flashcard performance to identify weak concepts and
generate targeted revision material.

### 3. Knowledge maps

Generate visual relationships between concepts and allow users to move
from a document to a structured knowledge graph.

### 4. Study plans

Create revision plans based on available material, deadlines, and weak
topics.

### 5. Collaborative learning

Support shared study spaces, shared notes, and controlled collaboration
for classmates or project teams.

### 6. Production observability

Add structured logs, error monitoring, performance metrics, rate-limit
handling, and AI-cost/quota monitoring.

### 7. Mature deployment architecture

Move from a single-service MVP to a production architecture with managed
PostgreSQL, object storage for uploads where needed, background jobs for
long processing tasks, and CI/CD.

## Product Principle

LearnInsight AI should not evolve by adding AI features simply because
they are possible. Every addition should improve one of three outcomes:
understanding material faster, remembering it longer, or organizing
learning more effectively.
