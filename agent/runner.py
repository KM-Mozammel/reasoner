from google.genai import types
from agent.config import get_agent_config
from agent.state import ConversationState
from tools.registry import TOOL_REGISTRY

def run_agent(client, user_prompt: str, max_turns: int = 5):
    state = ConversationState(user_prompt)
    config = get_agent_config()

    for turn in range(max_turns):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=state.get_history(),
            config=config,
        )

        model_content = response.candidates[0].content
        state.add_message(model_content)

        # Detect function calls
        tool_calls = [
            part.function_call
            for part in model_content.parts
            if part.function_call
        ]
        
        print(tool_calls)

        if not tool_calls:
            print("Final Answer Reached:")
            return response.text

        # Execute requested tools
        tool_response_parts = []

        for tool_call in tool_calls:
            func_name = tool_call.name
            func_args = dict(tool_call.args)

            print(f"Executing Tool: {func_name}({func_args})")

            if func_name in TOOL_REGISTRY:
                try:
                    result = TOOL_REGISTRY[func_name](
                        **func_args
                    )

                except Exception as e:
                    result = f"Error executing {func_name}: {str(e)}"
            else:
                result = f"Error: Tool '{func_name}' not found."
                
            print(f"Tool Output: {result}")

            # Create function response
            tool_response_parts.append(
                types.Part.from_function_response(
                    name=func_name,
                    response={
                        "result": result
                    },
                )
            )

        # Send tool outputs back to Gemini
        state.add_message(
            types.Content(
                role="user",
                parts=tool_response_parts
            )
        )

    return "Max turns reached without a final answer."
