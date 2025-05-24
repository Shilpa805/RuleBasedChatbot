import random
import re
import nltk
from chatbot.patterns import patterns

def analyze(user_input):
    user_input = user_input.lower()

    for pattern, responses in patterns.items():
        match = re.match(pattern, user_input)
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())

    # Basic NLP fallback
    tokens = nltk.word_tokenize(user_input)
    tags = nltk.pos_tag(tokens)

    if any(tag.startswith("VB") for _, tag in tags):
        return "Hmm, that's interesting. Tell me more."

    return "I'm not sure I understand, but I'm learning!"
