"""
Project 1: Rule-Based AI Chatbot
Author: Anuj Gupta

Description:
A rule-based chatbot that responds to predefined user inputs.
Uses dictionary-based intent mapping, input sanitization,
continuous conversation loop, and graceful exit handling.
"""

def chatbot():

    print("=" * 60)
    print("Bot Activated")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.")
    print("=" * 60)

    responses = {

        # Greetings
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! Nice to meet you.",
        "hey": "Hey! What can I do for you?",
        "good morning": "Good morning! Hope you have a productive day.",
        "good afternoon": "Good afternoon! How can I help?",
        "good evening": "Good evening! How was your day?",

        # Personal Questions
        "who are you": "I am DecodeBot, a rule-based AI chatbot.",
        "what is your name": "My name is DecodeBot.",
        "how are you": "I am functioning perfectly. Thanks for asking!",

        # AI Related
        "what is ai": (
            "Artificial Intelligence (AI) is the simulation "
            "of human intelligence by machines."
        ),
        "what is machine learning": (
            "Machine Learning is a branch of AI that allows "
            "systems to learn from data."
        ),

        # General Queries
        "time": "I cannot access real-time data, but your system clock can.",
        "date": "I cannot access today's date directly.",

        # Motivation
        "motivate me": (
            "Success is built through consistent effort. "
            "Keep learning and keep building!"
        ),

        # Help
        "help": (
            "\nAvailable Commands:\n"
            "- hello\n"
            "- hi\n"
            "- hey\n"
            "- who are you\n"
            "- what is ai\n"
            "- what is machine learning\n"
            "- motivate me\n"
            "- help\n"
            "- exit\n"
        )
    }

    exit_commands = {
        "exit",
        "quit",
        "bye",
        "goodbye",
        "close"
    }

    while True:

        user_input = input("\nYou: ").strip().lower()

        if not user_input:
            print("Bot: Please enter a valid message.")
            continue

        if user_input in exit_commands:
            print("Bot: Goodbye! Have a great day. 👋")
            break

        response = responses.get(
            user_input,
            "Sorry, I don't understand that command. Type 'help' to see available options."
        )

        print("Bot:", response)


if __name__ == "__main__":
    chatbot()