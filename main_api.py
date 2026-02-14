from fastapi import FastAPI
from pydantic import BaseModel
from services.openai_service import perguntar_chatgpt
from services.tts_service import gerar_audio
from services.history_service import salvar_conversa

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    messages = [
        {"role": "system", "content": "Responda no mesmo idioma da pergunta."},
        {"role": "user", "content": request.message}
    ]

    resposta = perguntar_chatgpt(messages)
    salvar_conversa(request.message, resposta)

    audio_path = gerar_audio(resposta)

    return {
        "response": resposta,
        "audio_file": audio_path
    }
