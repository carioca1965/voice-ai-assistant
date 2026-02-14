import streamlit as st
from services.openai_service import perguntar_chatgpt
from services.tts_service import gerar_audio
from services.history_service import salvar_conversa

st.title("ðŸŽ™ Voice AI Assistant")

user_input = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    messages = [
        {"role": "system", "content": "Responda no mesmo idioma da pergunta."},
        {"role": "user", "content": user_input}
    ]

    resposta = perguntar_chatgpt(messages)
    salvar_conversa(user_input, resposta)

    audio_path = gerar_audio(resposta)

    st.write("ðŸ¤– Resposta:", resposta)
    st.audio(audio_path)
