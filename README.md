# the_youtuber_Andreas_Reinholdsson_DE24

A **Retrieval-Augmented Generation (RAG) chatbot** built from the transcriptions of our teachers learning videos.  
Transcripts are embedded, stored in a vector database, and retrieved at query time to provide accurate, context-grounded answers.

---

## 🚀 Features

- RAG pipeline using video transcripts  
- Vector database for embedding and retrieval  
- Local API support with **Uvicorn**  
- Azure Functions deployment  
- Modern dependency + environment management with **`uv init`** and **`uv sync`**

---

## 🧠 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/REAndreas/the_youtuber_Andreas_Reinholdsson_DE24.git
cd the_youtuber_Andreas_Reinholdsson_DE24
```

---

## 🔑 Environment Variables (.env)

Create a `.env` file in the project root.

### Required for **local development** and ingestion:

```
GOOGLE_API_KEY=your_google_api_key_here
```

### Additional variable required when running the **Azure Function App**:

```
API_KEY=your_function_app_api_key_here
```

This protects the deployed function endpoint.

> If hosting locally with Uvicorn, you only need `GOOGLE_API_KEY`.  
> If deploying to Azure Functions, you need both.

---

## 🛠 Environment Setup with uv

### 1. Create a virtual environment

```bash
uv init
```

### 2. Sync dependencies

```bash
uv sync
```

This uses `uv.lock` to create a reproducible environment.

---

## 🧪 Running the API Locally (Uvicorn)

```bash
uvicorn api:app --reload
```

Open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs` (if enabled)

---

## ☁️ Deploying as an Azure Function

This project includes Azure Functions configuration files.

### 1. Install Azure Functions Core Tools  
Follow Microsoft’s installation guide.

### 2. Initialize your local function environment

```bash
func init
```

Choose **Python** as the language.

### 3. Ensure `.env` contains:

```
GOOGLE_API_KEY=...
API_KEY=...
```

### 4. Deploy

```bash
func azure functionapp publish <YOUR_FUNCTION_APP_NAME>
```

---

## 📚 RAG System Overview

The ingestion pipeline:

1. Reads transcripts from `transcripts/`  
2. Splits text into chunks  
3. Embeds each chunk  
4. Stores embeddings in a vector database  

When queried, the API:

- Retrieves relevant transcript chunks  
- Sends them as context to the model  
- Returns answers grounded in the YouTuber’s content  

---

## 📁 Project Structure

```
backend/                  # API and ingestion logic
frontend/                 # Optional UI
transcripts/              # Transcript data
api.py                    # Entry for Uvicorn
ingestion.py              # Builds vector DB
function_app.py           # Azure Function handler
pyproject.toml            # Managed by uv
uv.lock                   # Locked dependencies
.env.example              # (Optional file showing required variables)
```

---

## 💬 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Use `uv sync` for consistent environments  
4. Submit a pull request  

---

If you want, I can also create an `.env.example`, add badges, or generate an architecture diagram.