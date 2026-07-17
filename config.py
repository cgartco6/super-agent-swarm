import os
from dotenv import load_dotenv

load_dotenv()

LLM_MODEL = "gpt-4o-mini"  # or "claude-3-5-sonnet" etc. via compatible client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Mock mode for testing without API
MOCK_MODE = False
