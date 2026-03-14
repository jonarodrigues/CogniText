# 🧠 CogniText
### *Enterprise AI Orchestration Layer*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)](https://langchain.com/)

**CogniText** is a production-ready AI orchestration layer designed to integrate Large Language Models (LLMs) into modern software ecosystems. It provides a modular, schema-driven approach to text analysis, ensuring that AI responses are reliable, structured, and easily consumable by frontend applications (Mobile/Web).

## 🌟 Key Features
- **Provider Agnostic**: Seamlessly switch between OpenAI, Anthropic, or Local models (Ollama).
- **Structured Output**: Uses Pydantic for strict schema validation, ensuring your mobile app never receives malformed AI data.
- **Asynchronous Workflows**: Built on FastAPI for high-performance, non-blocking AI operations.
- **Context-Aware Reasoning**: Implements advanced prompting techniques for classification, summarization, and entity extraction.
- **Mobile-First Design**: Optimized JSON payloads and error handling tailored for mobile network constraints.

## 🏗️ Architecture
`mermaid
graph TD
    A[Mobile/Web Client] -->|JSON Request| B(CogniText API)
    B --> C{Orchestration Engine}
    C -->|Schema Validation| D[Pydantic Models]
    C -->|Select Provider| E[OpenAI / Anthropic / Local]
    E -->|Raw Response| C
    C -->|Structured JSON| B
    B -->|Verified Payload| A
`

## 🚀 Quick Start
1. **Clone the Repo**
   `ash
   git clone https://github.com/jonarodrigues/CogniText.git
   cd CogniText
   `

2. **Install Dependencies**
   `ash
   pip install -r requirements.txt
   `

3. **Configure Environment**
   Create a .env file:
   `env
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   `

4. **Run the API**
   `ash
   python main.py
   `

---

## 🛠️ Tech Stack
- **Core**: Python 3.9+
- **Orchestration**: LangChain
- **API Framework**: FastAPI
- **Validation**: Pydantic v2
- **Environment**: Dotenv

## 🧑‍💻 About the Author
**Jonathan Rodrigues** is a Mobile Software Engineer at **PicPay** with a focus on building scalable systems and exploring the intersection of Mobile Engineering and Artificial Intelligence.

---
*Developed for the next generation of intelligent software.*