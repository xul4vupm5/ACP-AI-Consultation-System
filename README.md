# ACP AI Consultation Platform

AI-powered healthcare consultation platform for Advance Care Planning (ACP).

🎓 Master's Research Project, National Chung Cheng University

📄 Accepted by IEEE COMPSAC 2024 Fast Abstracts

🤖 Built with OpenAI API, LangChain, ChromaDB and Retrieval-Augmented Generation (RAG)

## System Architecture

The ACP AI Consultation Platform adopts a Retrieval-Augmented Generation (RAG) architecture integrating healthcare knowledge retrieval, large language models, response evaluation, and user feedback mechanisms.

![architecture](/acp_system_architecture.png)


## Key AI Components

### Retrieval-Augmented Generation (RAG)

The platform retrieves ACP-related knowledge from a ChromaDB vector database using LangChain before sending contextual information to OpenAI GPT.

### Response Evaluation

Generated responses are evaluated through:

- Relevance Evaluation
- Toxicity Evaluation
- User Rating Feedback

Evaluation results are stored for future analysis and model improvement.

### Interaction Record Database

All user interactions, generated responses, and evaluation results are stored to support system monitoring and research purposes.

## Overview

ACP AI Consultation Platform is a Retrieval-Augmented Generation (RAG) based healthcare consultation system designed to support Advance Care Planning (ACP) education and information access.

The system combines:

- Flask web application
- LangChain retrieval pipeline
- ChromaDB vector database
- OpenAI GPT models
- Response quality evaluation
- User feedback collection

to provide reliable and context-aware healthcare consultation services.

The platform also records interaction history and evaluation results for future system improvement and research analysis.

## Features

- AI-powered healthcare consultation
- Retrieval-Augmented Generation (RAG)
- Healthcare knowledge retrieval
- Question & Answer database
- Course video learning module
- Conversation history recording
- Response quality evaluation
- User feedback collection

## Tech Stack

### Backend

- Python
- Flask
- SQLAlchemy
- SQLite

### AI

- OpenAI API
- LangChain
- ChromaDB
- HuggingFace Embeddings
- RAG Architecture

### Frontend

- HTML
- CSS
- JavaScript

### Evaluation
- Relevance Evaluation
- Toxicity Evaluation
- Human Feedback Collection

## Screenshots

### Home Page

![Home](ACP-AI-Consultation-System/images/home.png)

### AI Consultation

![QA](ACP-AI-Consultation-System/images/qa_demo.png)

### Database Search

![Database](ACP-AI-Consultation-System/images/database_demo.png)

### Course Learning Module

![Video](ACP-AI-Consultation-System/images/video_demo.png)

## My Contributions

- Designed and developed the complete system architecture
- Built a Flask-based healthcare consultation platform
- Integrated OpenAI GPT and Retrieval-Augmented Generation (RAG)
- Developed healthcare knowledge retrieval workflow
- Implemented response quality evaluation and feedback collection
- Designed database schema and conversation record management

## Technical Challenges

- Managing hallucination risks in healthcare consultation scenarios
- Improving retrieval relevance for ACP knowledge
- Evaluating response quality using relevance and toxicity metrics
- Designing a user-friendly consultation workflow for older adults

## Research Outcome

### Research Topic:

The Impact of a ChatGPT-Based Interactive System on Improving Older Adults’ Knowledge and Attitudes Toward Advance Care Planning

### Publication:

IEEE COMPSAC 2024 Fast Abstracts (Accepted)

## Future Improvements

- Docker Containerization
- Cloud Deployment
- Authentication & User Management
- Citation-based RAG
- Multi-LLM Support
- RESTful API Service
- Monitoring & Logging
