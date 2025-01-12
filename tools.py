from typing import Any, Dict, Callable

class ToolRegistry:
    """A registry for tools that agents can use."""
    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, func: Callable, description: str):
        self._tools[name] = {
            "func": func,
            "description": description
        }

    def get_tool(self, name: str) -> Optional[Callable]:
        return self._tools.get(name, {}).get("func")

    def list_tools(self) -> List[str]:
        return [f"{name}: {data['description']}" for name, data in self._tools.items()]

# Example Tool
def search_web(query: str) -> str:
    return f"Search results for: {query}"
