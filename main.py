from mcp_server.server import SQLiteMCPServer
from mcp_server.tools import create_mcp_tools
from llm.setup import setup_llm
from agent.prompts import get_system_prompt
from agent.agents import create_agent
import sys  # Add thi
def main():
    print("Application starting...")  # Debug point 1
    
    try:
        print("Initializing SQLite server...")  # Debug point 2
        mcp_server = SQLiteMCPServer()
        
        print("Setting up LLM...")  # Debug point 3
        llm = setup_llm()
        if llm is None:
            print("LLM setup failed!")
            return
            
        print("Creating tools...")  # Debug point 4
        tools = create_mcp_tools(mcp_server)
        system_prompt = get_system_prompt()
        
        print("Creating agent...")  # Debug point 5
        agent = create_agent(llm, tools, system_prompt)
        
        print("\nLocal MCP Client initialized. Type 'exit' to quit.")  # Debug point 6
        while True:
            try:
                user_input = input("User: ").strip()
                if not user_input:
                    continue
                if user_input.lower() == 'exit':
                    break
                
                print(f"Processing: {user_input}")  # Debug point 7
                response = agent.chat(user_input)
                print(f"Agent: {response}")
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                continue
                
    except Exception as e:
        print(f"Fatal error during initialization: {str(e)}")
    finally:
        print("Cleaning up...")  # Debug point 8
        mcp_server.close()
        print("Application shutdown complete.")

if __name__ == "__main__":
    print("Script entry point")  # Debug point 0
    main()