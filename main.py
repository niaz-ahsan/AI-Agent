import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt

def get_user_prompt():
    parser = argparse.ArgumentParser(description="LLM Prompt")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args.user_prompt, args.verbose

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API Key found!")
    client = genai.Client(api_key=api_key)
    llm_model = 'gemini-2.5-flash'
    prompt, is_detail = get_user_prompt()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = client.models.generate_content(
        model=llm_model, 
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0
        ), 
    )
    if response.usage_metadata is None:
        raise RuntimeError("Something went wrong with Gemini API")
    if is_detail:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()
