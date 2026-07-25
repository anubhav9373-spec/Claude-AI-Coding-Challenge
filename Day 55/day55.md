# Day 5 - LearnInsight AI: Interactive Study Workspace

## Overview

Day 5 focused on expanding LearnInsight AI into a complete AI-powered learning workspace by introducing interactive quizzes, flashcards, and a more efficient backend architecture.

A major engineering challenge was encountered during development: the Gemini API free-tier request limit. Instead of making separate API calls for each AI feature, the application was redesigned to generate all learning resources using a single AI request, resulting in a more scalable and production-oriented solution.

---

## Features

### AI Document Processing
- Upload PDF, DOCX, and TXT documents
- Automatic text extraction
- AI-generated structured summaries
- Beginner-friendly explanations

### Interactive Learning
- Multiple-choice quizzes
- Instant scoring
- Correct answer explanations
- Interactive flashcards
- Flip-card animations
- Previous/Next navigation

### Study Utilities
- Extracted text viewer
- Tab-based interface
- Responsive learning workspace

### Backend Improvements
- Single consolidated Gemini API request
- JSON-based AI response handling
- Reduced API usage by approximately 4×
- Improved quota efficiency
- Cleaner backend architecture
- Better error handling

---

## Technologies Used

- HTML5
- CSS3
- Vanilla JavaScript
- Python
- Flask
- Google Gemini API
- PyPDF2
- python-docx
- JSON

---

## Learning Outcomes

During this challenge, I learned how to:

- Build interactive AI-powered learning experiences
- Design structured AI prompts for multiple outputs
- Validate and parse AI-generated JSON safely
- Optimize backend architecture for API efficiency
- Solve real-world rate-limit problems through architectural improvements
- Develop scalable AI workflows instead of relying on temporary fixes

---

## Challenge

This project is part of the **60 Days of Claude AI Challenge** by AB Talks.

**Day 5 Objective:**
- Implement interactive quizzes
- Build AI flashcards
- Improve backend efficiency
- Optimize Gemini API usage through request consolidation

---

## Author

**Anubhav Maurya**

60 Days Claude AI Challenge – Day 5
