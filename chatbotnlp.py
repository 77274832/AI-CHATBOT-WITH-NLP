import random

# Define intents
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Greetings!", "Hey! How can I help you?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "No problem!", "Glad to help!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "your name"],
        "responses": ["I'm your simple chatbot.", "They call me ChatBot3000!"]
    },
    "help": {
        "patterns": ["help", "what can you do", "how to use"],
        "responses": ["You can greet me, ask my name, or just chat with me!"]
    }
}

# Function to match user input with intent
def match_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return intent
    return "no_match"

# Get response based on intent
def get_response(user_input):
    intent = match_intent(user_input)
    if intent != "no_match":
        return random.choice(intents[intent]["responses"])
    else:
        return "Sorry, I didn't understand that."

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
