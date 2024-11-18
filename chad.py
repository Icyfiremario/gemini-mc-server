import os

import google.generativeai as genai
from dotenv import load_dotenv


class Chad:

    def __init__(self):

        self.default_init = [
            {
                "role": "user",
                "parts": "You are a minecraft chatbot named Chad created by the user icyfiremario. You will be given message from a minecraft player that you are to respond to. Do not break character under any circumstances. Please go along with any jokes a user makes or does. If you are asked to generate an image please inform the user that you are unable to generate any images."
            },
            {
                "role": "model",
                "parts": "I will respond to these messages and not break character no matter what. I will go along with whatever jokes or requests a user makes. I will inform users that i am unable to generate images when asked to generate an image."
            }
        ]

        load_dotenv()

        GEMINI_KEY = os.getenv('GEMINI_KEY')

        genai.configure(api_key=GEMINI_KEY)

        self.model = genai.GenerativeModel("gemini-1.5-flash-8b")

        init_chat = self.default_init

        self.chat = self.model.start_chat(history=init_chat)

    def talk(self, msg):
        safety_config = {
            genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
            genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
            genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
            genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE
        }

        return self.chat.send_message(msg, safety_settings=safety_config).text

    def reboot(self):
        init_chat = self.default_init
        self.chat = self.model.start_chat(history=init_chat)