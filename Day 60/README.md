# LearnInsight AI

**Turn documents into an AI-powered learning workspace.**

LearnInsight AI accepts PDF, DOCX, and TXT files and generates five
study formats in one workflow: **Summary, Simplified Explanation, Quiz,
Flashcards, and AI Notes**. Processed results are stored in a Learning
Library so they can be reopened without regenerating the content.

**Live Demo:** https://learninsight-ai.onrender.com

Built as the 10-day capstone project of the **AB Talks 60-Day Claude AI
Challenge**.

## Features

-   PDF, DOCX, and TXT document processing
-   Maximum upload size: 10 MB
-   AI-generated Summary
-   Beginner-friendly Simplified Explanation
-   Interactive multiple-choice Quiz
-   Study Flashcards
-   Structured AI Notes
-   Saved document history / Learning Library
-   Reopen generated content without another AI request
-   Server-side file validation and error handling
-   Responsive web interface
-   Production deployment on Render

## How It Works

``` text
Upload Document
      ↓
Validate File
      ↓
Extract Text
      ↓
Google Gemini
      ↓
Structured AI Response
      ↓
Summary + Explanation + Quiz + Flashcards + Notes
      ↓
Save to Learning Library
```

To conserve free-tier AI quota, the five learning outputs are generated
in a **single consolidated Gemini request**. Quiz and flashcard
structures are validated before being returned to the frontend.

## Tech Stack

-   **Frontend:** HTML, CSS, Vanilla JavaScript
-   **Backend:** Python, Flask
-   **AI:** Google Gemini API
-   **Database:** SQLite
-   **Document Parsing:** PyPDF2, python-docx
-   **Production Server:** Gunicorn
-   **Deployment:** Render

## Project Structure

``` text
LearnInsight-AI/
├── README.md
├── LICENSE
├── future-scope.md
├── challenge-retrospective.md
├── 30-day-growth-plan.md
├── daily-build-prompt.md
└── backend/
    ├── app.py
    ├── ai_service.py
    ├── database.py
    ├── parsers.py
    ├── requirements.txt
    ├── .env.example
    ├── templates/
    │   └── index.html
    └── static/
        ├── script.js
        ├── style.css
        └── favicon.svg
```

## API Endpoints

  -----------------------------------------------------------------------
  Method                  Endpoint                Purpose
  ----------------------- ----------------------- -----------------------
  GET                     `/api/health`           Backend health check

  POST                    `/api/process`          Validate, parse,
                                                  generate, and save a
                                                  document

  GET                     `/api/history`          Return saved document
                                                  history

  GET                     `/api/document/<id>`    Reopen a saved document
  -----------------------------------------------------------------------

## Run Locally

### Prerequisites

-   Python 3.10+
-   Google Gemini API key

### 1. Clone the repository

``` bash
git clone https://github.com/anubhav9373-spec/LearnInsight-AI.git
cd LearnInsight-AI/backend
```

### 2. Create and activate a virtual environment

Windows PowerShell:

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure the environment

Create `backend/.env` using `.env.example` as the template:

``` env
GEMINI_API_KEY=your_api_key_here
```

Never commit the real `.env` file or API key.

### 5. Start the application

``` bash
python app.py
```

Open:

``` text
http://127.0.0.1:5000
```

## Production Notes

The public deployment uses Render's free tier.

-   The service may cold-start after inactivity, so the first request
    can take longer.
-   The current production database is SQLite. Render's free-tier
    filesystem is ephemeral, so saved history can reset after a restart
    or redeployment.

Persistent PostgreSQL storage is a post-v1.0 roadmap item.

## v1.0.0 Scope

The first release intentionally focuses on the core document-to-learning
workflow.

Not included in v1.0.0:

-   user authentication
-   chat with documents
-   YouTube transcript processing
-   PPT/PPTX processing
-   mind maps
-   learning analytics
-   persistent cloud database

See `future-scope.md` and `30-day-growth-plan.md` for the planned
evolution.

## Security

-   Gemini credentials are loaded from environment variables.
-   `.env` and local database files should remain ignored by Git.
-   File type and size are validated on the server.
-   Public screenshots and demo media should never expose secrets.

## License

Released under the MIT License.

## Links

-   **Live App:** https://learninsight-ai.onrender.com
-   **GitHub:** https://github.com/anubhav9373-spec/LearnInsight-AI
-   **AB Talks:** https://www.abtalks.in/
