import os
from dotenv import load_dotenv
from google import genai
import argparse

def get_user_prompt():
    parser = argparse.ArgumentParser(description="LLM Prompt")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    args = parser.parse_args()
    return args.user_prompt

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API Key found!")
    client = genai.Client(api_key=api_key)
    prompt = get_user_prompt()
    response = client.models.generate_content(
        model = 'gemini-2.5-flash', 
        contents = prompt 
    )
    if response.usage_metadata is None:
        raise RuntimeError("Something went wrong with Gemini API")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
