import json
import os

FILE_PATH = "data/conversations.json"

def salvar_conversa(user_text, bot_text):
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)

    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    data.append({
        "user": user_text,
        "assistant": bot_text
    })

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
