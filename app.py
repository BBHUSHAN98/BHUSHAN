import spacy

class SimpleChatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_input(self, user_input):
        doc = self.nlp(user_input)
        return doc

    def generate_response(self, doc):
        # Simple rule-based responses
        if "hello" in [token.text.lower() for token in doc]:
            return "Hi there! How can I help you?"

        if "how are you" in [token.text.lower() for token in doc]:
            return "I'm just a computer program, but thanks for asking!"

        # Add more rules for other questions or engage in conversation

        return "I'm not sure how to respond to that. Ask me something else."

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    print("Chatbot: Hi! Ask me anything or say hello.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        processed_input = chatbot.process_input(user_input)
        response = chatbot.generate_response(processed_input)

        print("Chatbot:", response)
