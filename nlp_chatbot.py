import nltk
import random
import string
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data (first-time only)
nltk.download('punkt')
nltk.download('wordnet')

# Predefined pattern-response pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm a bot, but I'm doing great. How about you?"]],
    [r"what is your name?", ["I'm your friendly chatbot."]],
    [r"what do you do?", ["I answer your questions using NLP."]],
    [r"bye|goodbye", ["Goodbye!", "See you soon!"]],
    [r"(.*) your creator?", ["I was created by a Python developer using NLTK."]],
    [r"(.*) (weather|temperature) (.*)", ["I'm not connected to real-time weather data, but you can check Google for current weather."]],
    [r"(.*) help (.*)", ["I'm here to assist. Ask me anything!"]],
    [r"(.*)", ["I’m not sure I understand. Can you rephrase that?"]],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Run chatbot
print("Hi, I'm an NLP Chatbot. Type 'bye' to exit.")
chatbot.converse()
