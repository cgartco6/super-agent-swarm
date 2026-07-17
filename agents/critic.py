from .base_agent import BaseAgent

class CriticAgent(BaseAgent):
    def __init__(self):
        super().__init__("Critic", "Reviews and improves outputs")

    def process(self, task: str) -> str:
        self.logger.info(f"Critiquing: {task}")
        critique = f"Critique: {task} is solid but could improve on metrics and risks."
        self.add_memory(critique)
        return critique
