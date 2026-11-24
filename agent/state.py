from google.genai import types
import json

class ConversationState:
    def __init__(self, user_prompt: str):
        self.history = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=user_prompt
                    )
                ]
            )
        ]
        
    def add_message(self, message):
        self.history.append(message)
        
    def get_history(self):
        return self.history
        