import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class FinAIEngine:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        
        # --- DETECTOR AUTOMÁTICO DE MODELO ---
        try:
            # Lista os modelos e pega o primeiro que suporta gerar conteúdo
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # Prioriza o flash, se não tiver, pega o primeiro da lista
            self.selected_model = "models/gemini-1.5-flash" if "models/gemini-1.5-flash" in models else models[0]
        except Exception:
            # Fallback total caso a listagem falhe
            self.selected_model = "gemini-pro"

        self.model = genai.GenerativeModel(
            model_name=self.selected_model,
            system_instruction="Você é o FinAI, um consultor financeiro prático. Use negrito para valores."
        )

    def generate_response(self, user_input, context, calculator=None):
        try:
            # Criamos o chat com o histórico
            chat = self.model.start_chat(history=self._format_history(context[-10:]))
            response = chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Erro: {str(e)}. Modelo usado: {self.selected_model}"

    def _format_history(self, context):
        history = []
        for msg in context:
            if "user" in msg and "assistant" in msg:
                history.append({"role": "user", "parts": [msg["user"]]})
                history.append({"role": "model", "parts": [msg["assistant"]]})
        return history