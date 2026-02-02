# --- Core Functions (from your original script) ---


def classify_issue(message: str) -> str:
    """
    Classify a support message into one of the categories based on keywords.
    """
    message = message.lower()
    if "refund" in message or "money" in message:
        return "Billing/Refund Issue"
    elif "login" in message or "password" in message:
        return "Account/Authentication Issue"
    elif "delivery" in message or "shipment" in message or "arrived" in message:
        return "Delivery/Logistics Issue"
    elif "error" in message or "not working" in message or "doesn't work" in message:
        return "Technical Issue"
    else:
        return "General Inquiry"


def analyze_sentiment(message: str) -> str:
    """
    Simple rule-based sentiment analysis to determine if a message is
    Positive, Negative, or Neutral.
    """
    negative_words = [
        "angry",
        "bad",
        "terrible",
        "not happy",
        "upset",
        "horrible",
        "frustrated",
    ]
    positive_words = ["good", "great", "happy", "love", "excellent", "awesome"]
    text = message.lower()

    if any(w in text for w in negative_words):
        return "Negative"
    elif any(w in text for w in positive_words):
        return "Positive"
    else:
        return "Neutral"


# --- Tool Definitions for the Ollama Model ---

tools = [
    {
        "type": "function",
        "function": {
            "name": "classify_issue",
            "description": "Classify a customer support message into predefined issue categories like Billing, Account, Delivery, or Technical.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The customer's message text",
                    },
                },
                "required": ["message"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "analyze_sentiment",
            "description": "Analyze the sentiment of a customer message to determine if it is Positive, Neutral, or Negative.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The customer's message text",
                    },
                },
                "required": ["message"],
            },
        },
    },
]
