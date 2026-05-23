# PDF Q&A Chatbot

A Streamlit chatbot that lets you ask questions about PDF documents. It uses OpenAI embeddings and GPT-4o-mini to retrieve relevant content from your PDFs and generate concise answers.

## How it works

1. A PDF is loaded and split into chunks
2. Chunks are embedded with OpenAI and stored in a local FAISS vector store
3. When you ask a question, the most relevant chunks are retrieved and passed to GPT-4o-mini to generate an answer

## Project structure

```
app/main/
├── Chatbot.py                  # Streamlit UI
└── Business/
    ├── PDFDocumentProcessor.py # Loads and chunks PDFs
    ├── RetrievalSystem.py      # FAISS vector store + similarity search
    ├── QAGenerator.py          # GPT-4o-mini answer generation
    └── QABot.py                # Orchestrates the pipeline
```

## Setup

**1. Clone the repo and create a virtual environment**

```bash
git clone https://github.com/ayawaelll/QA_Chatbot.git
cd QA_Chatbot
python -m venv .venv
.venv\Scripts\activate   # Windows
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Add your OpenAI API key**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-api-key-here
```

**4. Run the app**

```bash
streamlit run app/main/Chatbot.py
```

## Tech stack

- [Streamlit](https://streamlit.io) — UI
- [LangChain](https://python.langchain.com) — PDF loading, text splitting, chains
- [OpenAI](https://platform.openai.com) — embeddings (`text-embedding-ada-002`) + chat (`gpt-4o-mini`)
- [FAISS](https://github.com/facebookresearch/faiss) — local vector store
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management
