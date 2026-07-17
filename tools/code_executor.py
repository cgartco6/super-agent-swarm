from utils.logger import get_logger

logger = get_logger("code_executor")

def execute_code(code: str) -> str:
    """Safe code execution (use restricted env in production)"""
    logger.info("Executing code snippet")
    try:
        # For demo only - NEVER use eval in production without sandbox
        local = {}
        exec(code, {"__builtins__": {}}, local)
        return str(local.get("result", "Code executed successfully"))
    except Exception as e:
        return f"Error: {str(e)}"
