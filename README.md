# Government Policy RAG System
> Full-stack Retrieval-Augmented Generation system for internal policy document Q&A

<div align="center">









</div>

## 📖 Introduction
This project is a RAG question-and-answer platform oriented to internal policy documents.
Users upload policy files to the built-in knowledge base. After document parsing, text chunking, vectorization and keyword indexing, the system can answer policy-related user questions.
All generated answers come with source citations, so users can trace the content back to the original policy documents for verification.

## ✨ Core Capabilities
- Document upload and metadata management
- Automatic parsing and text segmentation of policy files
- Embedding generation and vector storage in Milvus
- Hybrid retrieval combining vector similarity and keyword matching
- Answer generation with original document reference citations
- SSE streaming real-time chat output
- Chat session and conversation history persistence
- RAG answer quality evaluation module

## 🧱 System Architecture
The project adopts a standard separated frontend-backend architecture.

| Layer | Technology Stack | Responsibility |
|-------|------------------|----------------|
| Frontend | Vue 3 | Web UI: document upload, chat panel, system settings, history view |
| Backend API | FastAPI + SQLAlchemy | REST API service, business logic, ORM data operation |
| Business Database | MySQL | Store document metadata, user session, chat records |
| Vector Database | Milvus | Store embedding vectors and perform similarity search |
| Default LLM | DeepSeek | The primary large model used to generate answers |
| Local LLM Runtime | Ollama | Local model runtime, will be integrated in later iterations |

> Note: Java Web remains the dominant technical stack in enterprise backend development.

## 📂 Project Directory Structure
├── backend/
│   ├── app/                # Core business logic, config, database factory
│   ├── scripts/            # Auxiliary inspection and debugging scripts
│   ├── tests/              # Unit test cases
│   └── requirements.txt    # Python dependency list
├── frontend/               # Vue3 single-page application
└── .gitignore              # Git ignore rules



## 🚀 Quick Start
### Prerequisites
- Python >= 3.10
- MySQL service
- Milvus vector database
- Node.js for frontend development

### Backend Service
1. Create and initialize MySQL database
2. Install python dependencies
```bash
pip install -r backend/requirements.txt


3. Configure environment variables according to your local environment
4. Start FastAPI backend service

### Frontend Web

```
cd frontend
npm install
npm run dev
```

## 📌 Current Scope & Future Plan

### Limitations of current version

Only text-format documents are supported in this implementation. Multimodal RAG capability is not included.

### Optimizations & extensions to implement later

1. Refactor the whole RAG pipeline with LangGraph to realize controllable agent workflow, routing and fallback logic
2. Access reranker model to improve retrieval precision
3. Add fine-grained permission control for confidential internal policy materials
4. Expand support for more document formats

## 📄 License

This repository is only for learning and research use.
