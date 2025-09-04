# ✨ InsightLens: AI-Powered Web Page Analyzer

InsightLens is a full-stack application that analyzes any given web page to extract its core topics and generate a core topics of content and summarize the content. It features a modern, responsive frontend and a powerful FastAPI backend that leverages a custom-built content extraction algorithm and the Google Gemini AI model for analysis.

This project was developed as a take-home assignment.

DEPLOYED PROJECT: https://insightlens.chetansingh.dev/

---

## 🚀 Features

* **Intelligent Content Extraction:** Uses a custom-built, "voting" algorithm to intelligently separate main article content from ads, navigation, and other boilerplate noise.
* **AI-Powered Analysis:** Leverages the Google Gemini (`gemini-1.5-flash-latest`) model to provide a high-quality, contextual summary and a curated list of key topics.
* **Modern API Backend:** Built with FastAPI, providing a fast, asynchronous, and robust API endpoint.
* **Responsive Frontend:** A sleek, self-contained HTML/JS/Tailwind CSS user interface that is fully responsive and provides a great user experience with loading states and error handling.
* **Robust & Compliant:** The architecture fully adheres to the assignment constraint of not using any third-party libraries for density collection or content analysis.

---

## 🛠️ Architecture & Tech Stack

The project follows a decoupled frontend-backend architecture:

#### Backend:

* **Framework:** FastAPI
* **Web Server:** Uvicorn
* **Content Fetching:** `requests`
* **HTML Parsing:** `BeautifulSoup4` with `lxml` for performance.
* **AI Integration:** `langchain-google-genai` to connect with the Google Gemini API.
* **Configuration:** `python-dotenv` for managing API keys.

#### Frontend:

* **Structure:** Single `index.html` file.
* **Logic:** Vanilla JavaScript with the `fetch` API.
* **Styling:** Tailwind CSS (via CDN for simplicity).

---

## ⚙️ Setup and Installation

Follow these steps to get the project running locally.

### Prerequisites

* Python 3.10+
* A Python virtual environment tool (e.g., `venv`)
* A Google Gemini API Key

### 1. Clone the Repository

`git clone https://github.com/chetansingh-2/ai-summariser.git`
### 2. Set up the Environment

Create and activate a Python virtual environment.

For Unix/macOS 
```bash
python3 -m venv .venv` 
source .venv/bin/activate
```
For Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Configure the API Key (SKIP, I hv kept .env file in code for your testing)

Create a `.env` file in the project's root directory. This file will store your Google Gemini API key.

```bash
/.env

GOOGLE_API_KEY="your_google_api_key_goes_here"
```
### 4. Install Dependencies

Install all the required Python libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
---

## ▶️ How to Run

The application consists of a backend server and a frontend file.

### 1. Start the Backend Server

Run the Uvicorn server from the project's root directory. The `--reload` flag will automatically restart the server when you make code changes.
```bash
uvicorn app.main:app --reload
```
> **Note:** The API will be available at `http://127.0.0.1:8000`.

### 2. Launch the Frontend

Navigate to the `frontend/` directory and open the `index.html` file in your web browser.

---

## 🧠 Key Design Decisions

This section highlights the engineering choices made to meet the assignment's requirements and build a robust solution.

### 1. Custom, Compliant Content Extractor

The assignment explicitly forbids the use of third-party libraries for density collection or content analysis. To adhere to this, a custom algorithm was developed in `app/utils.py`. It's a multi-layered heuristic engine:

* **Pre-flight Validation:** It first performs a lightweight `requests` check to ensure the URL is a valid, accessible HTML page before committing to a full download and parse.
* **Semantic-First Approach:** It prioritizes modern HTML5 tags (`<main>`, `<article>`) for high-confidence extraction.
* **Custom "Voting" System:** If semantic tags are not found, it falls back to a custom scoring algorithm. This system evaluates potential content containers (`<div>`, `<section>`) and scores them based on text length, paragraph count, and link density. This allows it to programmatically separate the "signal" (main content) from the "noise" (menus, footers, ads).


### 2. AI-Powered Analysis over Statistical Methods

While a simpler approach like NLTK's frequency counting could provide basic keywords, I chose to use the Google Gemini model for a significant leap in **quality**. The AI doesn't just count words; it understands context, semantics, and nuance. This results in a far more accurate and human-like summary and a more relevant list of key topics, moving beyond simple keywords to actual concepts.

---

## 📈 Future Enhancements (Production Architecture)

The current prototype is excellent for demonstration but would be evolved for a production environment. The full design plan is detailed in `design_documentation.md`, but the key improvements would be:

* **Asynchronous Architecture:** Re-architect the system using a task queue (Celery & Redis) to decouple the API from the slow analysis process. This would provide immediate API responses and allow the system to scale massively.
* **Intelligent AI Agent:** Upgrade the worker logic to an AI Agent (using LangChain Agents) equipped with a toolkit (e.g., the current scraper, a headless browser like Playwright). This would allow the agent to reason about failures and self-correct, for example, by using the headless browser to defeat anti-scraping on JavaScript-heavy sites.
