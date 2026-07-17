from .base_agent import BaseAgent
from tools.web_search import web_search

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher", "Gathers information and facts")

    def process(self, task: str) -> str:
        self.logger.info(f"Researching: {task}")
        results = web_search(task)
        self.add_memory(f"Research on {task}: {results}")
        return results
