import yaml
from genflow.LLM import LLMAgent  # Assicurati che questo agente supporti conversazioni a lungo termine
from genflow.utils.audio_ import (
    record_audio_from_microphone,
    speech_to_text_openai,
    text_to_speech_openai,
    play_audio_file,
)

class PsychologistOrchestrator:
    def __init__(self, config_path):
        with open(config_path, "r", encoding="latin1") as f:
            self.config = yaml.safe_load(f)

        self.prompt = self.config.get("description", "You are a helpful and empathetic psychologist.")
        self.agent = LLMAgent(prompt=self.prompt)
        self.chat_history = [{"role": "system", "content": self.prompt}]

    def run_session(self):
        print("🎙️ Inizia la sessione con lo psicologo virtuale. Dì 'esci' per terminare.\n")

        while True:
            if not self.config.get("chat_only", True):
                audio_path = record_audio_from_microphone()
                user_input = speech_to_text_openai(audio_path)
            else:
                user_input = input("🧠 Parlami dei tuoi problemi: ")

            if user_input.lower() in ["exit", "quit", "esci"]:
                print("🧠 Sessione terminata.")
                break

            self.chat_history.append({"role": "user", "content": user_input})

            response = self.agent.run(self.chat_history)
            self.chat_history.append({"role": "assistant", "content": response})

            print(f"🧠 Psicologo: {response}")

            if not self.config.get("chat_only", True):
                summary_audio_path = text_to_speech_openai(response)
                play_audio_file(summary_audio_path)

