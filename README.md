# 📄 Smart Document Search (Django + HuggingFace + FAISS)

An intelligent web application that lets you **upload PDF, Word, or scanned image documents**, and **ask questions** using **semantic search + OCR + AI embeddings**.


---


## 🚀 Features

- 📤 Upload PDF, Word, or Image files
- 🔍 Extract text using OCR (pytesseract for image/PDF scans)
- 🧠 Semantic search using HuggingFace Sentence Embeddings
- ⚡ FAISS vector similarity search
- ⚙️ Background processing with Celery + Redis
- 🎨 Clean UI using Bootstrap
- 🔎 (Optional) LangChain-based RAG for improved Q&A


---

## 🧠 Tech Stack

| Feature | Tool |
|--------|------|
| Backend | Django |
| AI Embeddings | HuggingFace Transformers (e.g., `sentence-transformers/all-MiniLM-L6-v2`) |
| OCR | pytesseract |
| Vector Search | FAISS |
| Async Tasks | Celery + Redis |
| Frontend | Bootstrap |
| Bonus | LangChain (for RAG-style QA) |

---

## 📂 Folder Structure
```
DOCSEARCH/
│
├── docsearch/                  # Django core project
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py               # Celery app definition
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── search/                     # Core app for document handling
│   ├── models.py
│   ├── views.py
│   ├── tasks.py                # Celery background jobs
│   ├── utils.py                # OCR, embedding logic
│   └── ...
│
├── templates/
│   └── search/
│       └── base.html           # HTML UI
│
├── static/                     # Bootstrap or custom CSS/JS
├── faiss_index/                # Stores FAISS vector indexes
├── media/                      # Uploaded user documents
├── .env                        # Environment variables
├── db.sqlite3                  # Local development DB
├── manage.py
├── README.md
└── requirements.txt



---

## 🔁 Example Flow

1. **User Uploads Document**
   - Upload PDF, Word, or Image file via web form.

2. **OCR + Text Extraction**
   - If the document is an image or scanned PDF, text is extracted using `pytesseract`.

3. **Embedding Generation**
   - Extracted text is split into chunks and converted into vector embeddings using HuggingFace's `all-MiniLM-L6-v2` model.

4. **FAISS Indexing**
   - Embeddings are stored in a FAISS index for fast similarity search.

5. **User Asks a Question**
   - The user types a natural-language question on the frontend.

6. **Semantic Search**
   - The system searches the FAISS index to find the most relevant document chunks.

7. **Answer Generation**
   - The best matching content is returned as a response.
   - (Optional) Use LangChain or GPT-based model to generate more refined answers (RAG-style).

8. **Result Display**
   - The answer is shown on the web interface with a reference to the source document.

---

## 🙌 Credits

This project wouldn't be possible without the amazing open-source tools and libraries:

- 🤗 [HuggingFace Transformers](https://huggingface.co/transformers) – for sentence embeddings and NLP models
- 🧠 [FAISS](https://github.com/facebookresearch/faiss) – for efficient similarity search on large vectors
- 🔍 [pytesseract](https://github.com/madmaze/pytesseract) – Python wrapper for Google's Tesseract OCR
- 🔄 [Celery](https://docs.celeryq.dev/) – for background task processing
- 💽 [Redis](https://redis.io/) – message broker for Celery
- 🧱 [Django](https://www.djangoproject.com/) – web framework used to build the core backend
- 🧰 [Bootstrap](https://getbootstrap.com/) – for clean, responsive frontend UI
- 🧠 [LangChain](https://www.langchain.com/) (optional) – for retrieval-augmented generation (RAG) using LLMs

---

## 📬 Contact

**Author:** Dharmendra Yadav  
📧 Email: dkydevops@gmail.com  
🌐 Website: [https://www.dydevops.com](https://www.dydevops.com)  
📱 WhatsApp: [+91 9452428546](https://wa.me/919452428546)


