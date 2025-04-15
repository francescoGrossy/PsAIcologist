import os
from openai import OpenAI

class LLMAgent:
    def __init__(self, prompt, model="gpt-3.5-turbo", temperature=0.7):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.temperature = temperature
        self.system_prompt = prompt  # Questo è il ruolo iniziale dell'assistente (es. psicologo)

    def run(self, chat_history):
        """
        chat_history deve essere una lista di messaggi nel formato:
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

