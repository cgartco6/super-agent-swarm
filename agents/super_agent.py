from .base_agent import BaseAgent
from typing import List

class SuperAgent(BaseAgent):
    def __init__(self, swarm_agents: List[BaseAgent]):
        super().__init__("SuperAgent", "Orchestrates the entire swarm")
        self.swarm_agents = swarm_agents

    def process(self, goal: str) -> str:
        self.logger.info(f"Orchestrating goal: {goal}")
        
        plan = f"Plan for '{goal}':\n1. Research\n2. Analyze\n3. Execute\n4. Critique"
        self.add_memory(plan)
        
        results = []
        for agent in self.swarm_agents:
            result = agent.process(goal)
            results.append(f"{agent.name}: {result}")
        
        final = f"Super Agent Final Output for '{goal}':\n" + "\n".join(results)
        return final
