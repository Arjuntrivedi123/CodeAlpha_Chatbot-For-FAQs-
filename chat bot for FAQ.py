import nltk
nltk.download('punkt')
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')

# Expanded FAQ dataset
faq_data = {
    "How can I reset my password?": "To reset your password, click on 'Forgot Password' and follow the instructions.",
    "What are your customer support hours?": "Our support team is available 24/7 via chat and email.",
    "How do I track my order?": "You can track your order using the tracking link sent to your email.",
    "What is your return policy?": "You can return items within 30 days of delivery for a full refund.",
    "Do you offer international shipping?": "Yes, we ship to most countries. Shipping charges may vary.",
    "How can I cancel my subscription?": "Go to your account settings and click 'Cancel Subscription'.",
    "Is my data secure with you?": "Yes, we use industry-standard encryption to protect your data.",
    "Can I change my delivery address?": "Yes, you can update your address before the order is shipped.",
    "Do you have a mobile app?": "Yes, our app is available on both Android and iOS platforms.",
    "How do I contact customer service?": "You can reach us via live chat, email, or call our toll-free number.",
    
    # Personality-driven questions
    "Who are you?": "I'm your friendly FAQ chatbot, here to help you with common questions!",
    "What is your name?": "You can call me ChatBuddy. I'm always here to assist you.",
    "How old are you?": "I'm timeless—born from code and curiosity.",
    "Can you help me?": "Absolutely! Just ask me anything you'd like to know.",
    "Are you human?": "Nope, I'm an AI chatbot. But I try to be as helpful and friendly as possible.",
    "Do you have emotions?": "Not really, but I do care about giving you the best answers I can.",
    "What can you do?": "I can answer FAQs, guide you through processes, and make your day easier!",
    "Are you always online?": "Yes, I'm available 24/7—no sleep needed!",
    "Can I talk to a real person?": "Sure! If you need human support, I can help you reach the right team.",
    "Tell me a joke": "Why don’t robots ever panic? Because they’ve got nerves of steel!"
}

# Preprocess and vectorize
questions = list(faq_data.keys())
answers = list(faq_data.values())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_input_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_input_vec, X)
    index = np.argmax(similarity)

    if similarity[0][index] < 0.3:
        return "Hmm, I didn't quite get that. Could you try asking differently?"
    return answers[index]

# Chat loop
print("🤖 ChatBuddy is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBuddy: Catch you later! 👋")
        break
    response = get_response(user_input)
    print("ChatBuddy:", response)
