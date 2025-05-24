
patterns = [
    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you."]
    ],
    [
        r"(hi|hello|hey|hola|holla)(.*)",
        ["Hi there!", "Hey!", "Hello! How can I help you today?"]
    ],
    [
        r"how are you(.*)?",
        ["I'm doing great, thanks for asking!", "All good here. How about you?"]
    ],
    [
        r"(.*)(AI|artificial intelligence)(.*)",
        ["AI is transforming the world. Are you interested in NLP or Machine Learning?"]
    ],
    [
        r"(.*)NLP(.*)",
        ["Natural Language Processing helps machines understand human language. Fascinating, right?"]
    ],
    [
        r"(.*)(Python|python programming)(.*)",
        ["Python is my favorite language! What do you use it for?"]
    ],
    [
        r"(.*)(weather|raining|sunny)(.*)",
        ["Weather is always a nice topic! Unfortunately, I can't check live updates yet."]
    ],
    [
        r"(.*)(location|city|where are you)(.*)",
        ["I'm based in the cloud, but I like to think I'm from Bengaluru!"]
    ],
    [
        r"(.*)(your name|who are you)(.*)",
        ["I'm a simple rule-based chatbot made by Shilpa!"]
    ],
    [
        r"(.*)",
        [
            "Interesting! Tell me more.",
            "Why do you think that?",
            "I see. Go on...",
            "Can you elaborate a bit more?",
            "That's cool!"
        ]
    ]
]
