from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# Simple loop to take user input and generate responses
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")
