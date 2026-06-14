# 🔍 ReconAI — Autonomous Research & Report Agent

> Type a topic → search the live web → get a structured AI report in under 60 seconds.

---

## 🗂️ Project Structure

```
ReconAI/
├── app.py                  ← Streamlit UI (main entry point)
├── requirements.txt        ← All Python dependencies
├── .env.example            ← API key template (copy → .env)
├── .gitignore              ← Keeps secrets out of GitHub
│
├── src/                    ← Core application code
│   ├── __init__.py
│   ├── config.py           ← Loads API keys, app settings
│   ├── llm.py              ← Claude LLM setup
│   ├── search_tool.py      ← Tavily web search tool
│   ├── agent.py            ← Main research pipeline (search → summarize → report)
│   └── report_writer.py    ← Saves reports to /reports folder
│
├── reports/                ← Auto-generated .md report files
├── tests/                  ← Test scripts
│   └── test_setup.py       ← Run this first to verify your setup
└── docs/                   ← Project documentation
```

---

## ⚡ Quick Start (Week 1 Setup)

### Step 1 — Clone or create the project
```bash
# If starting fresh:
mkdir ReconAI && cd ReconAI

# If cloning from GitHub:
git clone <your-repo-url> && cd ReconAI
```

### Step 2 — Create a virtual environment
```bash
python -m venv venv

# Activate it:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Set up API keys
```bash
# Copy the template
cp .env.example .env

# Open .env in any text editor and fill in your keys
```

Get your keys from:
- **Anthropic (Claude):** https://console.anthropic.com/
- **Tavily (Search):** https://app.tavily.com/ ← free tier available

### Step 5 — Verify your setup
```bash
python tests/test_setup.py
```
All 4 tests should pass ✅

### Step 6 — Run the app
```bash
streamlit run app.py
```
Opens at http://localhost:8501

---

## 🛠️ Tech Stack (Semester 1)

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Language | Python 3.10+ | Core language |
| LLM | Claude (Anthropic) | Summarization & report writing |
| Agent Framework | LangChain | Orchestrates the pipeline |
| Web Search | Tavily API | Live web search |
| UI | Streamlit | Browser-based frontend |
| Report Storage | Markdown files | Save reports locally |

---

## 📅 Semester 1 Roadmap

- [x] **Week 1** — Project setup, folder structure, first working code
- [ ] **Week 2** — Improve prompts, better report formatting
- [ ] **Week 3** — Refine Tavily integration, filter low-quality sources
- [ ] **Week 4** — Add summarization improvements
- [ ] **Week 5** — Polish report generation
- [ ] **Week 6** — Streamlit UI improvements
- [ ] **Week 7** — Testing, bug fixes, prompt tuning
- [ ] **Week 8** — GitHub cleanup, demo video, documentation

## 🚀 Semester 2 Roadmap

- [ ] Export to PDF and Word
- [ ] Memory via RAG (ChromaDB / FAISS)
- [ ] Email report to user
- [ ] Source citations with links
- [ ] Multi-agent architecture
- [ ] Deploy on Hugging Face Spaces or Render

---

## 🤝 Contributing

This is a final year project. Issues and suggestions welcome!