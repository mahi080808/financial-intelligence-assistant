# 🤖 Financial Intelligence Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions in natural language.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic PDF parsing
- ✂️ Text chunking
- 🧠 OpenAI Embeddings
- 📦 Pinecone Vector Database
- 🔍 Semantic Search
- 🤖 GPT-powered Question Answering
- 💻 React Frontend
- ⚡ FastAPI Backend

---

## 🛠️ Tech Stack

### Frontend
- React
- Bootstrap
- JavaScript

### Backend
- FastAPI
- Python

### AI & Database
- OpenAI API
- Pinecone
- Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```text
multi-agent-financial-intelligence/
│
├── app/
│   ├── main.py
│   └── rag/
│       ├── chunking.py
│       ├── embeddings.py
│       ├── pinecone_db.py
│       └── generator.py
│
├── frontend/
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 How It Works

```
User Uploads PDF
        │
        ▼
Extract Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate OpenAI Embeddings
        │
        ▼
Store in Pinecone
        │
        ▼
User Asks Question
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Send Context + Question to GPT
        │
        ▼
Generate Answer
```

---

## 🎯 Future Improvements

- 💬 ChatGPT-style conversation history
- 📚 Display retrieved source chunks
- 🌙 Dark mode
- ☁️ Cloud deployment
- 📄 Multiple PDF support

---

## 👩‍💻 Developed By

**Mahendra Kondapalli**