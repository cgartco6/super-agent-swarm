from agents.super_agent import SuperAgent
from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.executor import ExecutorAgent
from agents.critic import CriticAgent

def create_swarm():
    agents = [
        ResearcherAgent(),
        AnalyzerAgent(),
        ExecutorAgent(),
        CriticAgent()
    ]
    return SuperAgent(agents)
