import asyncio
import json
from typing import List, Dict, Any, Callable

class Tool:
    def __init__(self, name: str, func: Callable, description: str):
        self.name = name
        self.func = func
        self.description = description

class Agent:
    def __init__(self, name: str, role: str, model: str = "gpt-4"):
        self.name = name
        self.role = role
        self.model = model
        self.tools: Dict[str, Tool] = {}
        self.history: List[Dict[str, str]] = []

    def add_tool(self, tool: Tool):
        self.tools[tool.name] = tool

    async def run(self, prompt: str) -> str:
        print(f"[{self.name}] Processing: {prompt}")
        self.history.append({"role": "user", "content": prompt})
        # Simulated LLM call
        await asyncio.sleep(1)
        response = f"Response from {self.name} ({self.role}) to: {prompt}"
        self.history.append({"role": "assistant", "content": response})
        return response

class Orchestrator:
    def __init__(self):
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    async def broadcast(self, message: str) -> List[str]:
        tasks = [agent.run(message) for agent in self.agents]
        return await asyncio.gather(*tasks)

async def main():
    orchestrator = Orchestrator()
    researcher = Agent("Researcher", "Data Gathering")
    writer = Agent("Writer", "Content Creation")
    orchestrator.add_agent(researcher)
    orchestrator.add_agent(writer)
    
    results = await orchestrator.broadcast("Analyze the impact of Generative AI on software engineering.")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())
