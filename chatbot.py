

import time
import openai
import os

# Set your OpenAI API key (Ensure this is set securely in your environment)
os.environ["OPENAI_API_KEY"] = "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"

# Initialize OpenAI client
client = openai.OpenAI()

def chat_with_ai(prompt):
    """Handles interaction with OpenAI's GPT-4o model and manages errors."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Updated model
            messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    except openai.RateLimitError:
        print("⚠️ Rate limit exceeded. Waiting before retrying...")
        time.sleep(10)  # Wait and retry
        return "I'm currently at my limit. Please try again in a moment."

    except openai.AuthenticationError:
        return "⚠️ Invalid API key. Please check your OpenAI API credentials."

    except openai.APIConnectionError:
        return "⚠️ Network error. Check your internet connection and try again."

    except openai.OpenAIError as e:
        return f"⚠️ OpenAI API error: {e}"

if __name__ == "__main__":
    print("🤖 Chatbot started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("AI: Goodbye! 👋")
            break
        response = chat_with_ai(user_input)
        print("AI:", response)
