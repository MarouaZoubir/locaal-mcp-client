from llama_index.core.tools import FunctionTool
from typing import Dict
import json
from llama_index.core.tools import FunctionTool
from mcp_server.server import SQLiteMCPServer
from typing import List


def add_data(name: str, description: str, value: float) -> Dict:
    """Add data with strict parameter validation"""
    if not isinstance(name, str) or not isinstance(description, str) or not isinstance(value, (int, float)):
        return {"error": "Invalid parameters"}
    return {"status": "success", "id": 1}  # Simplified for example

def fetch_data(limit: int = 10) -> Dict:
    """Fetch data with parameter validation"""
    if not isinstance(limit, int):
        return {"error": "Limit must be integer"}
    return [{"id": 1, "name": "Sample", "description": "Test", "value": 1.0}]

def create_mcp_tools(server: SQLiteMCPServer):
    """Create tools with enhanced validation"""
    
    def add_data_checked(name: str, description: str, value: float):
        """Wrapper to prevent duplicates"""
        existing = server.fetch_data(limit=100)
        if any(d['name'] == name for d in existing):
            return {"status": "error", "message": "Entry already exists"}
        return server.add_data(name, description, value)
    
    return [
        FunctionTool.from_defaults(
            fn=add_data_checked,
            name="add_data",
            description="Add data if not exists. Format: {'name':'str','description':'str','value':float}"
        ),
        FunctionTool.from_defaults(
            fn=server.fetch_data,
            name="fetch_data",
            description="Fetch data. Format: {'limit':int}"
        )
    ]