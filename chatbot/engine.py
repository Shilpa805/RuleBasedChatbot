# chatbot/engine.py

import re
import random
from chatbot.patterns import patterns

def analyze(user_input):
    for pattern, responses in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            response = random.choice(responses)
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                return response % match.groups() if '%' in response else response
    return "I'm not sure I understand. Can you rephrase?"
