# Simple chatbot using Python

# Step 1: Define a dictionary of questions and answers
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bunch of Python code, but I'm doing great!",
    "what is your name": "I'm a simple chatbot built with Python.",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "who created you": "I was created by a Python enthusiast!"
}

# Step 2: Start a loop to keep the conversation going
print("Type 'exit' to end the chat.\n")

while True:
    # Step 3: Get user input
    user_input = input("You: ").lower().strip()

    # Step 4: Check for exit condition
    if user_input == "exit":
        print("Bot: Chat ended. See you next time!")
        break

    # Step 5: Respond if input matches known questions
    elif user_input in responses:
        print("Bot:", responses[user_input])

    # Step 6: Default response for unknown input
    else:
        print("Bot: I'm not sure how to respond to that.")
