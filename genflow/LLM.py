import os
from openai import OpenAI

class LLMAgent:
    def __init__(self, prompt, model="gpt-3.5-turbo", temperature=0.7):
        self.client = OpenAI("...insert your OPENAI KEY...")
        self.model = model
        self.temperature = temperature
        self.system_prompt = prompt 

    def run(self, chat_history):
        """
        chat_history must be a list as the following:
        [{"role": "system", "content": "..."},
         {"role": "user", "content": "..."},
         {"role": "assistant", "content": "..."},
         ...]
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=chat_history,
            temperature=self.temperature
        )
        return response.choices[0].message.content

