def simple_chatbot():
    print("ChatBot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if any(greet in user_input for greet in ["hello", "hi", "hey", "good morning", "good evening"]):
            print("ChatBot: Hello there! Lovely to see you!")
        elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you", "later"]):
            print("ChatBot: Farewell! May your day be bright!")
            break
        elif "how are you" in user_input or "how are you doing" in user_input:
            print("ChatBot: I'm functioning well, thank you! How about you?")
        elif "what is your name" in user_input or "who are you" in user_input:
            print("ChatBot: I'm ChatBot, a simple assistant created to talk with you!")
        elif "help" in user_input or "what can you do" in user_input or "commands" in user_input:
            print("ChatBot: I can greet you, answer questions, and wish you well. Try saying hello!")
        elif "what is the time" in user_input:
            print("ChatBot: I can't check the time, but your system clock surely can!")
        elif "what is the date" in user_input:
            print("ChatBot: Check your calendar—I'm timeless, but you’re not!")
        elif "tell me a joke" in user_input or "make me laugh" in user_input:
            print("ChatBot: Why don’t programmers like nature? It has too many bugs!")
        elif "thanks" in user_input or "thank you" in user_input:
            print("ChatBot: You're welcome, dear friend!")
        elif "you are awesome" in user_input or "i like you" in user_input:
            print("ChatBot: Aww, you’re making me blush—digitally, of course!")
        else:
            print("ChatBot: Hmm, I don't quite understand that. Can you try asking differently?")

# Run the chatbot
simple_chatbot()
