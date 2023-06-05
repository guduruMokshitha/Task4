import random

# List of common questions and their answers
questions = {
    "what is your name?": "My name is Chatbot.",
    "how are you?": "I am doing well, thank you.",
    "what can you do?": "I can answer some common questions.",
    "who created you?": "I was created by [your name].",
    "what is the meaning of life?": "I'm not sure, but some say it's 42."
}

# Function to generate a random greeting
def greeting():
    responses = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
    return random.choice(responses)

# Function to answer a question
def answer_question(question):
    # Convert question to lowercase
    question = question.lower()

    # Check if the question is in the list of known questions
    if question in questions:
        return questions[question]
    else:
        return "I'm sorry, I don't know the answer to that question."

# Main function to start the chatbot
def main():
    print("Welcome to the Chatbot! Ask me a question or say hello.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        elif user_input.lower() in ["hi", "hello", "hey"]:
            print("Chatbot:", greeting())
        else:
            print("Chatbot:", answer_question(user_input))

if __name__ == "__main__":
    main()