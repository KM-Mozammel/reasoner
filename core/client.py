from google import genai

def create_client():
    """
    Initialize and return Gemini client.
    """
    return genai.Client()