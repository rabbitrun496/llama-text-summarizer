# Text Summarizer AI Project Using LLaMA via Ollama

## 🧠 Overview

**Goal**: Build a local AI-powered text summarization app using the LLaMA model via Ollama.

## 🛠️ Tech Stack

- **[Ollama](https://ollama.com/)** — Run LLaMA models locally  
- **FastAPI** — Backend API to interact with the model  
- **Streamlit** — Frontend UI for user interaction  

---

## 🧪 Step 1: Set Up Your Environment

1. **Install Python** and set up a virtual environment:

```bash
python -m venv venv
```

2. **Activate the environment**:

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

3. **Install project dependencies**:

```bash
pip install fastapi uvicorn streamlit requests python-multipart
```

4. **Install and run Ollama**:
   - Download Ollama from: [https://ollama.com](https://ollama.com)
   - Start Ollama and pull the LLaMA model:

```bash
ollama run llama2
```

---

## 🚀 Step 2: Backend with FastAPI

1. Create the file: `backend/main.py`

2. Run the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

---

## 💻 Step 3: Frontend with Streamlit

1. Create the file: `frontend/app.py`

2. Run the Streamlit app:

```bash
streamlit run frontend/app.py
```

---

 Structure

```
text-summarizer-llama/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── venv/
├── requirements.txt
└── README.md
```

---

## ✅ Notes

- Make sure Ollama is running in the background before using the app.
- `venv/` is excluded from version control (not uploaded to GitHub).
- Use `requirements.txt` to install dependencies on other machines.

