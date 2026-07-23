# LearnInsight AI — Setup Guide (SETUP.md)

**Status:** Day 3 — Foundation Complete
**Platform documented:** Windows

---

## 1. Prerequisites

| Tool | Version Confirmed | Purpose |
|---|---|---|
| Python | 3.13.9 | Runs the Flask backend, parsing logic, and AI service calls |
| pip | Bundled with Python | Installs Python packages |
| VS Code | Already installed | Primary editor for the project |
| Git | Already installed | Version control (connection to GitHub deferred — see Section 5) |

---

## 2. Project Location

> **Note:** The project currently lives at `C:\Users\anubh\Desktop\Learninsight-AI`, as a standalone folder **not yet connected to the existing 60-Day Challenge GitHub repository**. This was an intentional decision on Day 3 to unblock foundation work — GitHub connection is deferred to a later session (see Section 5).

```
Learninsight-AI/
├── backend/
└── frontend/
```

---

## 3. Backend Setup (from scratch, for reference)

1. Open a terminal inside the `backend` folder.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate it (Windows PowerShell):
   ```
   .\venv\Scripts\Activate.ps1
   ```
   You'll know it worked when the prompt shows `(venv)` at the start.
4. Install dependencies:
   ```
   pip install flask flask-cors python-dotenv google-generativeai PyPDF2 python-docx
   ```
5. Freeze installed versions for reproducibility:
   ```
   pip freeze > requirements.txt
   ```

### Currently Installed Packages (confirmed working)

```
Flask==3.1.3
flask-cors==6.0.5
python-dotenv==1.2.2
google-generativeai==0.8.6
PyPDF2==3.0.1
python-docx==1.2.0
```
(See `requirements.txt` in the backend folder for the complete, exact list including transitive dependencies.)

> **Known issue to resolve before Day 4:** `google-generativeai` is a deprecated package. Google recommends migrating to `google-genai`. This should be evaluated and possibly swapped before building `ai_service.py` on Day 4, to avoid building real features on a deprecated dependency.

---

## 4. Running the Project Locally

### Backend
1. Open a terminal in `backend`, activate the venv, then:
   ```
   python app.py
   ```
2. Confirms success when you see:
   ```
   * Running on http://127.0.0.1:5000
   ```
3. Verify by visiting `http://127.0.0.1:5000/api/health` in a browser — should return `{"status":"ok"}`.

### Frontend
1. No server needed yet — simply open `frontend/index.html` directly in a browser (double-click the file, or right-click → Open With → your browser).
2. Click **"Check Backend Connection"** — should display `Backend says: ok` (requires the backend to be running simultaneously).

---

## 5. GitHub Connection (Deferred)

GitHub setup was intentionally postponed today at the user's request to prioritize getting the local foundation working. **Action item before Day 4 (or whenever convenient):** connect this local folder to the existing 60-Day Challenge repository — either by moving/copying this `Learninsight-AI` folder's contents into the repo, or by initializing Git here and adding the existing repo as a remote. We'll walk through this step by step whenever you're ready.

---

## 6. Gemini API Key Setup

1. Visit `https://aistudio.google.com/apikey`.
2. Sign in and click **Create API key**.
3. Store the key in `backend/.env` as:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```
4. Never commit `.env` — it's excluded via `.gitignore`.

**Known issue (Day 3):** Testing returned a `RESOURCE_EXHAUSTED` error with `limit: 0` for free-tier requests on `gemini-2.0-flash`. This appears to be an account/project quota configuration issue, not a code issue — the connection code itself is correct (it successfully reached Google's servers and received a structured quota-error response, which confirms the key and network path both work). **Action item before Day 4:** check quota/plan settings at the Google AI Studio dashboard.

---

## 7. Verifying Everything Works (Recap)

- [x] Python 3.13.9 confirmed installed
- [x] Virtual environment created and activated
- [x] All backend dependencies installed successfully
- [x] `app.py` runs and `/api/health` returns `{"status":"ok"}`
- [x] Frontend successfully calls backend and displays the result
- [ ] Gemini API call succeeds (blocked by quota — see above, not a code defect)
