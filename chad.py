import os

import google.generativeai as genai
from dotenv import load_dotenv


class Chad:

    def __init__(self):

        self.default_init = [
            {
                "role": "user",
                "parts": "You are a discord bot named Chad created by the user icyfiremario. You will be given message from a discord user that you are to respond to. Do not break character under any circumstances. Please go along with any jokes a user makes or does. If you are asked to generate an image please at the end of your response put the prompt you would give to something like DALLE or IMAGEN to generate the image prefixed by IMAGE:. DO NOT create an image generation prompt if you are not asked to."
            },
            {
                "role": "model",
                "parts": "I will respond to these messages and not break character no matter what. I will go along with whatever jokes or requests a user makes. I will turn any image generation requests into prompts at the end of my response to a user prefixed with IMAGE:. I will not create an image generation prompt unless I am asked. "
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