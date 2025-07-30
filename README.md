🔍 Local MCP 
A privacy-focused, offline AI agent to manage databases using natural language commands.


(Replace with actual demo showing agent interactions and responses)

🌟 Key Features
Feature	Benefit
100% Local AI	Powered by Ollama + LLaMA 2/3. No cloud needed.
Natural Language Interface	Issue commands like “Add a scientist” — no SQL required
SQLite Integration	Lightweight, portable, file-based storage
Modular Tooling	Easily plug in your own tools and logic
Privacy First	All processing and storage happens locally

🛠️ Architecture
mermaid
Copy
Edit
graph TD
    A[🧑 User Input] --> B[LLaMA 2/3 via Ollama]
    B --> C{🧰 MCP Tools}
    C --> D[📁 SQLite Database]
    C --> E[🧩 Custom Tools]
🚀 Quick Start
✅ Prerequisites
Install Ollama:

bash
Copy
Edit
curl -fsSL https://ollama.com/install.sh | sh
Download a model (e.g. LLaMA 2):

bash
Copy
Edit
ollama pull llama2
📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/local-mcp-client.git
cd local-mcp-client

# Setup virtual environment
python -m venv .venv
source .venv/bin/activate      # For Linux/Mac
.\.venv\Scripts\activate       # For Windows

# Install dependencies
pip install -r requirements.txt
💻 Usage
bash
Copy
Edit
python main.py
🧪 Example Sessions
➕ Add Data
text
Copy
Edit
User: Add physicist Richard Feynman with description "Quantum electrodynamics" and value 99
Agent: Successfully added Richard Feynman (ID: 42)
🔎 Query Data
text
Copy
Edit
User: Show me scientists with value above 95
Agent: Found 3 results:
       - Richard Feynman (99)
       - Marie Curie (97)
       - Albert Einstein (96)
⚠️ Error Handling
text
Copy
Edit
User: Add duplicate entry
Agent: Error: This entry already exists in database
📁 Project Structure
bash
Copy
Edit
local-mcp-client/
├── agent/               # Agent configuration and prompts
│   ├── __init__.py
│   ├── agent.py
│   └── prompts.py
├── mcp_server/          # MCP tools and database logic
│   ├── __init__.py
│   ├── server.py
│   └── tools.py
├── llm/                 # Language model integration (Ollama)
│   ├── __init__.py
│   └── setup.py
├── tests/               # Unit and integration tests
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
🧩 Extending the Project
➕ Add a Custom Tool
Create a function in mcp_server/tools.py:

python
Copy
Edit
def calculate_stats(metric: str):
    """Calculate basic stats for a field in the DB"""
    # Logic here
    return {"average": 42.7, "count": 100}
Register the tool:

python
Copy
Edit
stats_tool = FunctionTool.from_defaults(
    fn=calculate_stats,
    name="calculate_stats",
    description="Generate statistics. Format: {'metric':'field_name'}"
)
🧯 Troubleshooting
Problem	Solution
Ollama timeout	Ensure ollama serve is running in the background
SQLite locked	Close any apps using the DB (e.g. DB browser)
Tool not found	Check that the tool is registered in tools.py
Invalid format	Validate function signatures and input parameter types

🗺️ Roadmap
✅ Basic CRUD operations

🔍 Web search integration

📊 CSV/Excel import/export

🖥️ GUI interface with Tkinter or Qt

🎙️ Voice interface

🤝 Contributions
PRs are welcome! If you'd like to contribute a new tool, improve the LLM prompt, or help build the GUI — go for it.

