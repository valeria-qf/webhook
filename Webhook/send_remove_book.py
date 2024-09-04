import requests
import json

def send_book(title):
    url = "http://localhost:5000"
    headers = {"Content-Type": "application/json"}
    payload = {
        "title": title,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    else:
        print("Erro:", response.status_code, response.text)

if __name__ == "__main__":
    send_book("O Senhor dos Anéis")