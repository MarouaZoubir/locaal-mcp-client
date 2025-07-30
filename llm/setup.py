from llama_index.llms.ollama import Ollama

def setup_llm() -> Ollama:
    """Initialize the Ollama LLM with Llama 3"""
    return Ollama(
        model="llama2",
        base_url="http://localhost:11435",  # Changed from deepseek-r1 to llama2
        request_timeout=300.0,
        temperature=0.3,
        top_p=0.9,
        system="You are a helpful AI assistant with strong tool-using capabilities."
    )