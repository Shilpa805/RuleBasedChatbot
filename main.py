from chatbot.engine import analyze

def chat():
    print("Hi! I'm a simple rule-based chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = analyze(user_input)
        print(response)

if __name__ == "__main__":
    chat()
