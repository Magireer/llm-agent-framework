import asyncio
import json
from typing import List, Dict, Any, Optional, Callable
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all LLM agents."""
    def __init__(self, name: str, role: str, model: str = "gpt-4"):
        self.name = name
        self.role = role
        self.model = model
        self.memory: List[Dict[str, str]] = []
        self.tools: Dict[str, Callable] = {}

    def register_tool(self, name: str, func: Callable):
        self.tools[name] = func

    @abstractmethod
    async def process(self, input_text: str) -> str:
        pass

class ConversationalAgent(BaseAgent):
    """An agent designed for multi-turn conversations."""
    async def process(self, input_text: str) -> str:
        self.memory.append({"role": "user", "content": input_text})
        # Simulated LLM interaction
        response = f"Agent {self.name} ({self.role}) processed: {input_text}"
        self.memory.append({"role": "assistant", "content": response})
        return response

class AgentOrchestrator:
    """Manages communication and task delegation between multiple agents."""
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}

    def add_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent

    async def execute_workflow(self, task: str, sequence: List[str]) -> Dict[str, str]:
        results = {}
        current_input = task
        for agent_name in sequence:
            if agent_name in self.agents:
                result = await self.agents[agent_name].process(current_input)
                results[agent_name] = result
                current_input = result
        return results
