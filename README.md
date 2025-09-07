# 🤖 FAQ Chatbot - ChatBuddy

A simple Python-based chatbot that answers frequently asked questions (FAQs) using natural language processing. ChatBuddy uses TF-IDF vectorization and cosine similarity to understand user queries and provide the most relevant answer from a predefined dataset. Includes some personality-driven responses to make the chat more interactive!

## Features

- Answers common FAQs from a customizable dataset
- Friendly, personality-driven responses for generic questions
- Vectorizes and matches user input using TF-IDF and cosine similarity
- Runs entirely in the terminal/command line
- Easy to extend with more Q&A pairs

## How it Works

1. The bot uses a dictionary of questions and answers.
2. User input is vectorized and compared to all questions using cosine similarity.
3. The answer with the highest similarity is returned.
4. If no question matches closely (similarity < 0.3), a default response is given.

## Demo

```bash
🤖 ChatBuddy is ready! Type 'exit' to quit.
You: How do I reset my password?
ChatBuddy: To reset your password, click on 'Forgot Password' and follow the instructions.
You: Tell me a joke
ChatBuddy: Why don’t robots ever panic? Because they’ve got nerves of steel!
You: exit
ChatBuddy: Catch you later! 👋
```

## Requirements

- Python 3.6 or higher
- Packages: `nltk`, `numpy`, `scikit-learn`

## Setup & Usage

1. **Clone the repository or copy the code.**
2. **Install dependencies:**
   ```bash
   pip install nltk numpy scikit-learn
   ```
3. **Run the script:**
   ```bash
   python chatbot.py
   ```
   *(Replace `chatbot.py` with your file name if different)*

4. **First run will download NLTK data automatically.**

## Customization

- Add or edit question-answer pairs in the `faq_data` dictionary to suit your needs.
- Adjust the similarity threshold in `get_response()` if needed.

## Credits

- Built by [Arjun Trivedi]
- Uses [NLTK](https://www.nltk.org/) for tokenization
- Vectorization and similarity by [scikit-learn](https://scikit-learn.org/)

---

Feel free to contribute or raise issues!
