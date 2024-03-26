
import openai

# Set up OpenAI API key
openai.api_key = 'api_key'

# Define function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can use other engines like "davinci-codex" for code-related tasks
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Example of handling user input and getting response
def handle_user_input(user_input):
    # Process user input
    prompt = f"User: {user_input}\nBot:"
    
    # Get response from ChatGPT
    bot_response = chat_with_gpt(prompt)
    
    # Return bot response
    return bot_response
