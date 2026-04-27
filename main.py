import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def get_user_prompt():
    parser = argparse.ArgumentParser(description="LLM Prompt")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args.user_prompt, args.verbose

def build_response(response, verbose):
    function_calls = response.function_calls
    if function_calls is not None:
        output = []
        for fc in function_calls:
            function_call_result = call_function(fc, verbose)
            if len(function_call_result.parts) < 1:
                raise Exception("Parts not found in types.Content")
            if function_call_result.parts[0].function_response is None:
                raise Exception("function_response not found in parts[0]")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("response not found in parts[0].function_response")
            output.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        return output
    print(response.text)
    return "break"

def call_model(client, model, user_prompt, verbose, messages):
    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            temperature=0
        ), 
    )
    candidates = response.candidates
    if candidates:
            for cand in candidates:
                messages.append(cand.content)
    if response.usage_metadata is None:
        raise RuntimeError("Something went wrong with Gemini API")
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response:
        function_responses = build_response(response, verbose)
        if type(function_responses) == str and function_responses == "break":
            return 1
        to_append = types.Content(role="user", parts=function_responses)
        messages.append(to_append)
        return 0

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API Key found!")
    client = genai.Client(api_key=api_key)
    llm_model = 'gemini-2.5-flash'
    prompt, is_detail = get_user_prompt()
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    should_exit = 0
    for _ in range(20):
        should_exit = call_model(client, llm_model, prompt, is_detail, messages)
        if should_exit:
            break
    if should_exit == 0:
        print("Max limit of iteration reached.")
        exit(1)


if __name__ == "__main__":
    main()
