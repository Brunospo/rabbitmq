import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)


token = 'telegram token'
chat_id = 'telegram-chat-id'
message = "Ola Mundo!!!"

send_telegram_message(token, chat_id, message)
