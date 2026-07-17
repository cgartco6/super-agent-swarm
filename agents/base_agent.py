from abc import ABC, abstractmethod
from typing import Dict, Any
from utils.logger import get_logger

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory: list[Dict[str, Any]] = []
        self.logger = get_logger(name)

    def add_memory(self, message: str):
        self.memory.append({"role": "system", "content": message})

    @abstractmethod
    def process(self, task: str) -> str:
        pass
