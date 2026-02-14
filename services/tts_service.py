from gtts import gTTS
import uuid
import os

def gerar_audio(texto, idioma="pt"):
    filename = f"response_{uuid.uuid4()}.mp3"
    path = os.path.join("data", filename)

    tts = gTTS(text=texto, lang=idioma)
    tts.save(path)

    return path
