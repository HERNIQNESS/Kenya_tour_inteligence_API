# Kenya_tour_inteligence_API

A Retrieval-Augmented Generation (RAG) API that enables users to ask travel-related questions and receive context-aware answers grounded in curated Kenyan tourism data. This system combines semantic search (ChromaDB + embeddings) with large language models (Groq LLM) to provide accurate, engaging, and source-backed responses.

## Overview

Instead of generating answers from general knowledge, this system:
-	Embeds curated tourism documents.
-	Stores them in a vector database.
- Retrieves the most relevant documents for a user query.
- Uses an LLM to generate answers strictly from retrieved context.
- Returns both the answer and the source references.

  ##### This ensures grounded, explainable responses.

## Architecture

- ### User Query

     ↓
- ### SentenceTransformer Embedding (BAAI/bge)
  
   ↓
- ### ChromaDB Similarity Search
  
   ↓
- ### Context Assembly
 
   ↓
- ### Groq LLM (Llama Model)
 
    ↓
- ### Structured JSON Response (Answer + Sources)



## Tech Stack

- FastAPI — API framework
- ChromaDB — Vector database
- SentenceTransformers (BAAI/bge) — Embedding model
-	Groq API — LLM inference
- Python 3.10+

## 📂 Project Structure
                                                                                                                                
- ├── app.py                # FastAPI application
- ├── rag_service.py        # Retrieval + generation pipeline
- ├── chroma_db/            # Persistent vector database
- ├── .env                  # Environment variables
- └── requirements.txt


## API Endpoints

GET /
Health check endpoint.
- Returns:
         
      {"message": "TOUR API is running"}

POST /ask

Submit a tourism-related question.

- Request:

       { "question": "Best wildlife experiences near Nairobi?"}

- Response

      {"answer": "...",
      "sources": ["nairobi_national_park.pdf"]}


## 🔍 Retrieval Process
  1. User query is embedded using BGE model.
   
  2.	Embedding is normalized for cosine similarity.

  3.	ChromaDB retrieves top-k similar documents.
  
  4.	Retrieved content forms structured context.
  
  5.	LLM generates answer constrained to that context.
  

- This prevents hallucination and ensures grounded outputs.

⸻

## 🎯 Key Features
 
  •	Persistent vector storage 
  
  •	Context-grounded LLM responses
  
  •	Source attribution
  
  •	Structured JSON API
  
  •	Easily extensible document ingestion pipeline

⸻

## 📈 Future Improvements

 •	Cross-encoder reranking for improved retrieval precision
  
 •	Query expansion for better recall
  
 •	Redis caching for frequent queries
  
 •	Metadata filtering by location/category
  
 •	Async streaming responses

⸻

## 🧩 Use Cases

 •	Tourism chatbots
  
 •	Travel discovery assistants
  
 •	Government tourism portals
  
 •	Hotel and attraction discovery systems












  
