# chatbot.py
# A simple rule-based chatbot using Python

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello!  How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm ChatBuddy — your friendly Python chatbot "
    elif "time" in user_input:
        from datetime import datetime
        return "The current time is " + datetime.now().strftime("%H:%M:%S")
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye!  Have a great day!"
    elif "thank" in user_input:
        return "You're welcome! "
    else:
        return "Hmm... I’m not sure about that. Can you rephrase?"

def main():
    print(" ChatBuddy: Hi there! Type 'bye' or 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBuddy:", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main() 