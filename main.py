from dotenv import load_dotenv
load_dotenv()
from core.client import create_client
from agent.runner import run_agent

def main():

    client = create_client()

    prompt = (
        "What is the current time, "
        "and what is 4 multiplied by 8?"
    )

    final_output = run_agent(
        client=client,
        user_prompt=prompt
    )

    print(f"\nAgent: {final_output}")


if __name__ == "__main__":
    main()
