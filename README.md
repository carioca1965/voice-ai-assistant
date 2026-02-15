
## Rodar Streamlit
streamlit run app_streamlit.py
🎙 Voice AI Assistant

Assistente de Voz Multilíngue utilizando OpenAI (GPT + Whisper), FastAPI, Streamlit e gTTS.

O sistema é capaz de:

🎤 Converter voz em texto (Speech-to-Text)

🤖 Processar a pergunta com modelo de IA (ChatGPT)

🔊 Converter resposta em áudio (Text-to-Speech)

🌍 Trabalhar com múltiplos idiomas

🚀 Demonstração da Arquitetura
Usuário (voz)
      ↓
Whisper (Speech-to-Text)
      ↓
GPT (Processamento da pergunta)
      ↓
gTTS (Text-to-Speech)
      ↓
Resposta em áudio

🛠 Tecnologias Utilizadas

Python 3.11+

FastAPI

Uvicorn

OpenAI API (GPT + Whisper)

gTTS

Streamlit

Docker

Git

📂 Estrutura do Projeto
voice-ai-assistant/
│
├── main_api.py
├── app_streamlit.py
├── services/
│   ├── openai_service.py
│   ├── speech_to_text.py
│   └── text_to_speech.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md

⚙️ Como Executar Localmente
1️⃣ Clonar o repositório
git clone https://github.com/carioca1965/voice-ai-assistant.git
cd voice-ai-assistant

2️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar arquivo .env

Crie um arquivo .env na raiz do projeto:

OPENAI_API_KEY=sua_chave_aqui

5️⃣ Rodar API
python -m uvicorn main_api:app --reload


Acesse:

http://127.0.0.1:8000/docs

🐳 Executar com Docker
docker-compose up --build

🧠 Conceitos Aplicados

Integração com APIs REST

Arquitetura modular

Separação de responsabilidades (services layer)

Variáveis de ambiente seguras

Containerização com Docker

Versionamento com Git

💡 Possíveis Melhorias Futuras

Histórico de conversas

Autenticação de usuários

Deploy em nuvem (Render, Railway, AWS)

Detecção automática de idioma

Cache de respostas

👨‍💻 Autor

Eduardo
GitHub: https://github.com/carioca1965
