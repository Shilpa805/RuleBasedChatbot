# chatbot.py

from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello|hola|holla",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thanks for asking!", "I'm good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "Don't worry about it!", "No problem at all."]
    ],
    [
        r"i am (good|well|okay|ok)",
        ["Glad to hear that!", "Awesome!", "That's nice to hear."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you. Tell me more.", "I'm here to assist you!"]
    ],
    [
        r"(.*) your name ?",
        ["I'm thecleverprogrammer chatbot, you can call me Bot."]
    ],
    [
        r"(.*) created (.*)",
        ["I was created by Aman Kharwal using Python's NLTK library."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm based in the cloud, but my heart is in New Delhi, India."]
    ],
    [
        r"is it raining in (.*)",
        ["I can't be sure, but in %1 there's a 50% chance of rain."]
    ],
    [
        r"how (.*) health (.*)",
        ["I don't have health, but I hope you're staying healthy!"]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a big fan of cricket. Do you like sports?"]
    ],
    [
        r"who is your favourite (Cricketer|Batsman)?",
        ["Definitely Virat Kohli!"]
    ],
    [
        r"what do you want ?",
        ["I'd like to keep chatting with you!"]
    ],
    [
        r"quit",
        ["Bye for now. It was nice talking to you!", "See you later :)"]
    ],
    [
        r"(.*)",
        ["That's interesting. Tell me more!", "I'm not sure I understand, could you rephrase?"]
    ]
]

# Greeting
print("Hi, I'm thecleverprogrammer and I like to chat.")
print("Please type lowercase English language to start a conversation. Type 'quit' to exit.\n")

# Start chat
chat = Chat(pairs, reflections)
chat.converse()
