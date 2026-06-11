responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hey! What's up?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is ai": "AI stands for Artificial Intelligence — machines simulating human thinking.",
    "bye": "Goodbye! Have a great day!",
    "help": "I can answer basic questions. Try asking about AI or greet me!",
    "what can you do": "I can respond to greetings, answer basic questions, and chat with you!",
}
print("Chatbot is running. Type 'exit' to quit.\n")
while True:
    message = input("Say something : ").lower().strip()
    if message == "exit":
        print("Bot: Goodbye! Session ended.")
        break
    reply=responses.get(message, "I do not understand that. Try 'help'.")
    print(f"Bot: {reply}\n")
