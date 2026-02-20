# Features: Greetings, Time, Date, Jokes, Mood Detection, Exit Command

import datetime
import random

# Function for greeting responses
def greet():
    greetings = [
        "Hello! 👋",
        "Hi there! 😊",
        "Hey! How can I help you today?"
    ]
    return random.choice(greetings)

# Function to tell time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time} ⏰"

# Function to tell date
def get_date():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    return f"Today's date is {today} 📅"

# Function to tell jokes
def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the computer go to the doctor? Because it caught a virus! 💻",
        "Why do Python programmers wear glasses? Because they can't C! 😆"
    ]
    return random.choice(jokes)

# Function for mood detection
def mood_response(user_input):
    if "sad" in user_input:
        return "I'm sorry to hear that. Everything will be okay 💙"
    elif "happy" in user_input:
        return "That's awesome! Keep smiling 😄"
    elif "stressed" in user_input:
        return "Take a deep breath. You’re doing great 🌿"
    return None

# Main chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if user_input in ["hello", "hi", "hey"]:
        return greet()

    # Basic questions
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning perfectly! 🤖"

    elif "your name" in user_input:
        return "I am Level 2 Rule-Based Chatbot."

    # Time and Date
    elif "time" in user_input:
        return get_time()

    elif "date" in user_input:
        return get_date()

    # Joke feature
    elif "joke" in user_input:
        return tell_joke()

    # Mood detection
    mood = mood_response(user_input)
    if mood:
        return mood

    # Exit condition
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a productive day 🚀"

    # Default reply
    else:
        return "I didn't understand that. Try: hello, time, date, joke, or bye."

# Main function to run chatbot
def start_chatbot():
    print("🤖 Level 2 Chatbot Started!")
    print("Type 'bye' to exit.")
    print("You can ask: hello, time, date, joke, mood (sad/happy/stressed)\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

# Run the chatbot
start_chatbot()
