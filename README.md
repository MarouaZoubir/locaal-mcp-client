# Local MCP Client

This project is a 100% local MCP (Modular Component Protocol) client implementation using:
- 🦙 [LlamaIndex](https://github.com/jerryjliu/llama_index) to build an agent
- 🧠 [Ollama](https://ollama.com/) to run the LLM locally (e.g., Deepseek or Llama 2)
- ⚡ [Lightning AI](https://lightning.ai/) for development and orchestration

## 🔧 Tech Stack

- Python 3.10+
- LlamaIndex
- Ollama (LLM runner)
- LightningAI (optional dev server)
- NestAsyncio / asyncio for async event loop
- [BasicMCPClient](https://github.com/jerryjliu/llama_index/tree/main/llama-index-integrations/tools/mcp)

## 🧠 Features

- Fully local AI agent
- Connects to local tools via MCP protocol
- Executes tool calls based on user input
- Supports function agents and tool-chaining

## 🚀 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/MarouaZoubir/locaal-mcp-client.git
   cd locaal-mcp-client
Set up your environment

bash
Copy
Edit
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
Start Ollama with your model

bash
Copy
Edit
ollama run llama2
Run the agent

bash
Copy
Edit
python main.py
🛠 Structure

### 📁 Project Structure

```bash
local-mcp-client/
├── agent/             # Agent builder and prompts
│   ├── __init__.py
│   ├── agent.py
│   └── prompts.py
├── mcp_server/        # SQLite & Tool logic
│   ├── __init__.py
│   ├── server.py
│   └── tools.py
├── llm/               # Ollama integration setup
│   ├── __init__.py
│   └── setup.py
├── tests/             # Unit tests
├── main.py            # App entry point
└── requirements.txt   # Dependencies
```


The agent will:

Recognize intent

Call a temperature tool via MCP

Return a thoughtful response using LLM reasoning

📌 Notes
Make sure Ollama is running before starting the agent

The MCP tools must be discoverable at runtime
