# Rule based chatbot!
 
import random
import re

intents = {
    "greetings":{
        "patterns": ["hello", "hi", "hey", "Howdy", "hola"],
        "responses": ["Hello!", "Hi there!", "Hey!", "howdy!"]
    }, 
    "goodbyes": {
        "patterns": ["bye", "goodbye", "see you", "later"],
        "responses": ["Goodbye!", "See you later!", "Take Care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!", "Anytime!"]
    },
    "questions": {
        "how are you": ["I am fine, thank you!", "Doing great, what about you?"],
        "what's your name ": ["I'm ChatBuddy . what's your name?"],
        "what can you do": ["I can chat with you, help answer questions, and even sole math problems!"]
    }  
}

def match_intent(user_input):
    for intent, intent_data in intents.items():
        if isinstance(intent_data, dict) and "patterns" in intent_data:
            for pattern in intent_data["patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    return random.choice(intent_data["responses"])
    for question, responses in  intents["questions"].items():
        if question in user_input.lower():
            return random.choice(responses)
        
    return None           


def get_response(user_input):
    matched_intent = match_intent(user_input)
    
    if matched_intent:
        return matched_intent
    else:
        return "I didn't quite understand that. could you please try asking something else?"
    
def chatbot():
    print("Chatbot: Hi!, I'm Chatbuddy. How can i assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:" , response)
           
chatbot()