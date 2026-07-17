from .base_agent import BaseAgent
from tools.code_executor import execute_code

class ExecutorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Executor", "Implements plans and generates artifacts")

    def process(self, task: str) -> str:
        self.logger.info(f"Executing: {task}")
        # Example: generate code or action
        code = f"result = 'Executed task: {task}'"
        result = execute_code(code)
        self.add_memory(result)
        return result
