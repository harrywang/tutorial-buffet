import os
import sys
from dotenv import load_dotenv
from litellm import completion

# Load environment variables from .env file
load_dotenv()

# Configure the API endpoint and key
api_key = os.environ.get("API_KEY")
api_base = "https://litellmud.takin.ai"  # Hardcoded API base URL
model = "litellm_proxy/ollama/deepseek-r1:7b"  # Hardcoded model name

# Verify API key is set
if not api_key:
    print("Error: API_KEY must be set in .env file")
    sys.exit(1)

def generate_response(prompt, stream=False):
    try:
        # Set up the request parameters
        params = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "api_key": api_key,
            "api_base": api_base,
            "stream": stream,
            # Optional parameters
            "temperature": 0.6,
            "max_tokens": 500,
        }
        
        # Send the request
        if stream:
            # Return the streaming response generator
            return completion(**params)
        else:
            # Get the complete response
            response = completion(**params)
            return response.choices[0].message.content
            
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"An error occurred: {str(e)}"

def stream_response(prompt):
    """
    Stream a response from the model and print it to the console.
    
    Args:
        prompt (str): The user prompt to send to the model
    """
    try:
        print(f"\nPrompt: {prompt}")
        print("\nResponse: ", end="")
        
        # Get the streaming response
        response_stream = generate_response(prompt, stream=True)
        
        # Process and print each chunk
        for chunk in response_stream:
            content = chunk.choices[0].delta.content
            if content:
                sys.stdout.write(content)
                sys.stdout.flush()
                
        print("\n")
    except Exception as e:
        print(f"\nError streaming response: {e}")

def main():
    prompt1 = "write a short poem about artificial intelligence"
    print(f"Prompt: {prompt1}")
    response1 = generate_response(prompt1)
    print(f"Response: {response1}")

if __name__ == "__main__":
    main()
