from llama_index.core.agent import ReActAgent
from llama_index.core.base.llms.types import ChatMessage, MessageRole
from typing import List
from llama_index.core.tools import FunctionTool

def create_agent(llm, tools: List[FunctionTool], system_prompt: str):
    """Create agent with proper configuration"""
    chat_history = [
        ChatMessage(role=MessageRole.SYSTEM, content=system_prompt),
        ChatMessage(
            role=MessageRole.USER,
            content="""Always use the EXACT tool calling format:
            Action: tool_name
            Action Input: {"param1":"value1","param2":"value2"}"""
        )
    ]
    
    agent = ReActAgent.from_tools(
        tools=tools,
        llm=llm,
        chat_history=chat_history,
        verbose=True,
        max_iterations=10,  # Increased from default
        early_stopping=False,
        handle_parsing_errors=True
    )
    return agent