import requests
from utils.logger import get_logger

logger = get_logger("web_search")

def web_search(query: str, num_results: int = 5) -> str:
    """Mock web search (in production, integrate Serper, Tavily, etc.)"""
    logger.info(f"Searching: {query}")
    # Real implementation would call an API
    return f"Search results for '{query}':\n1. Relevant article 1\n2. Relevant article 2\n..."
