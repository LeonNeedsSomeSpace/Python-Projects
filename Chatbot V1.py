import random

# Make a chatbot that can answer questions for you. It is a form of very basic artificial intelligence

print("Hey, what's up? Let's talk a little, shall we?\n")

# Create a set of stored answers that the chatbot can access during operation
replies = {
    "Greetings": ["What's up? How's your day?", "Hi! Nice to meet you!", "Hey! How can I help you?"],
    "Name": ["I don't really have a name. Just call me your 'Chatbot'. What do you wanna talk about?"],
    "Band": ["My favourite band? Well, LIMIT INFINITY has got some serious hits in their playlist ;)"],
    "Cooking": ["Don't know what to cook? Stir fry pak-choi with shiitake and garlic. Add soy sauce, salt and sugar:)"],
    "Fun Facts": ["Did you know? Birds bones are hollow for weight reduction but have struds that adds durability."],
    "Goodbye": ["Bye! See you next time!", "See you! Have a great day!"]
}
# These are the keywords that the chatbot will be looking for in the input and find the best fitting answer
keywords = {
    "Greetings": ["hey", "hello", "hi", "greetings", "hi there", "yo", "how are you"],
    "Name": ["what is your name?", "what's your name", "your name", "name", "can you introduce yourself", "introduce"],
    "Band": ["band", "favourite Band", "favourite", "what is your favourite band"],
    "Cooking": ["I want to cook something", "cook", "Dish", "Dishes", "Eat", "Eating"],
    "Fun Facts": ["something", "tell me", "fun fact", "interesting", "random"],
    "Goodbye": ["bye", "goodbye", "see you", "i have to go", "go", "leave", "leaving"]

}

# Define a function that will accept a user input
# Define a variable 'user_input' that will store data of the user input

# This function tries to find the best possible response to the user's input and returns it to the calling function
def receive_reply(user_input):
    """Checking input. Finding correct response"""
    user_input = user_input.lower()
    best_match = None
    best_keyword_length = 0
# Convert keywords into lowercase. That way it responds correctly no matter how the user capitalizes the words
    for category, keys in keywords.items(): # Loop over each category in the keywords dictionary. Category is the key.
        for key in keys: # Loops through each keyword in the current category's keyword list. 'keys' is keywords
            key_lower = key.lower() # Converts the keyword into lower case.
            if key_lower in user_input: # Checks whether the keyword it is at is in the user's input
                if len(key_lower) > best_keyword_length:  # Checks if multiple keywords match
                    best_keyword_length = len(key_lower)  # Update keyword length, only replace if next one is longer
                    best_match = category # Store category of the best keyword found so far

    if best_match: # If the best keyword found, give a reply from the category as output
        return random.choice(replies[best_match])

        # Should the chatbot not recognize any of the keywords or not find anything that matches a category
    return "Sorry, I don't understand. Can you repeat?"

def main(): # Main function controls chatbot conversation loop and prints the response 'receive_reply' returns
    """Chatbot's main output"""
    print("You are in a conversation. Enter 'exit' to leave. Type in lowercase.")

    while True: # This will start an infinite loop to keep the convo going until the user decides to quit
        user_input = input("You: ") # 'You' header for the user
        # If the user enters 'exit', the conversation will stop
        if user_input.lower() == "exit": # Create the if-condition
            print("Bye! See you next time!") # Give an output when the user decides to exit
            break  # Conversation ends here as soon as user enters 'exit'
        reply = receive_reply(user_input) # Otherwise, the reply gets passed on to 'receive_reply'
        print("Chatbot: ", reply) # Prints the returned chosen response

# Check how the python script is being run
# It prevents the file from running automatically
if __name__ == "__main__":
    main()