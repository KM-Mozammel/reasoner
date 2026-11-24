from google.genai import types
from tools.registry import TOOL_REGISTRY

def get_agent_config():
    return types.GenerateContentConfig(
        system_instruction=(
            "You are a precise assistant. "
            "Use tools when needed."
        ),
        
        tools = list(TOOL_REGISTRY.values()),
        
        automatic_function_calling=(
            types.AutomaticFunctionCallingConfig(disable=True)
        ),
        
        temperature=0.0,
    )