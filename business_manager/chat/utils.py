import requests

def ask_deepseek(message, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": message}]
    }
    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",  # Verifique a URL atualizada
            headers=headers,
            json=data
        )
        response.raise_for_status()  # Levanta erro para respostas HTTP falhas
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Erro ao processar.")
    except Exception as e:
        return f"Desculpe, ocorreu um erro: {str(e)}"