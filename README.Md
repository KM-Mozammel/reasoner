# Reasoner AI

## **An Extensible AI Reasoning Platform with Function Calling, React UI, and Future-Ready Support for RAG, MCP, and Databases**

![alt text](image.png)

# Reasoner AI

Reasoner AI is an intelligent AI assistant developed by Mozammel Khandakar. The project combines a Python backend with a React.js frontend to create a modular and extensible reasoning system capable of using tools and function calling.

## Features

- AI-powered reasoning engine
- Function Calling support
- Modular agent architecture
- REST API backend
- React.js frontend
- Environment-based configuration
- Extensible tools system

## Planned Features

- Retrieval-Augmented Generation (RAG)
- MCP (Model Context Protocol) integration
- Database connectivity
- Memory management
- Multi-agent collaboration
- Authentication and user management

## Project Structure

```text
reasoner-ai/
│
├── agent/
├── api/
├── core/
├── tools/
├── frontend/
├── .env
├── main.py
├── requirements.txt
└── README.md
```

## Technology Stack

### Backend
- Python
- FastAPI
- AI Function Calling
- REST APIs

### Frontend
- React.js
- Modern JavaScript

## Installation

Clone the repository:

git clone https://github.com/KM-Mozammel/reasoner.git

Navigate to project directory: cd reasoner-ai
Install backend dependencies : pip install -r requirements.txt
Install frontend dependencies: cd frontend
                               npm install

Run backend : uvicorn api.main:app --reload
Run frontend: npm start

## Vision

Reasoner AI aims to become a complete AI platform capable of reasoning, tool usage, knowledge retrieval, database interaction, and MCP-based integrations.

## Author

Mozammel Khandakar

## License

MIT License
