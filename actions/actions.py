# actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from transformers import pipeline

class ActionChatGPT(Action):
    def name(self):
        return "action_chatgpt"

    def run(self, dispatcher, tracker, domain):
        # Obtenir le dernier message utilisateur
        user_input = tracker.latest_message.get('text')
        
        # Initialiser le générateur de texte Hugging Face GPT-2
        generator = pipeline('text-generation', model='gpt2')

        try:
            # Générer une réponse basée sur l'input utilisateur
            response = generator(user_input, max_length=50)
            generated_text = response[0]['generated_text'].strip()
            
            # Envoyer la réponse générée au dispatcher
            dispatcher.utter_message(generated_text)
        except Exception as e:
            # Envoyer un message d'erreur si quelque chose ne va pas
            dispatcher.utter_message(f"Une erreur est survenue: {str(e)}")

        return []
