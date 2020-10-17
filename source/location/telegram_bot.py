from django.conf import settings
import requests

token=settings.TELEGRAM_BOT_TOKEN

def sendTBotMessage(chat_id,text,reply_to_msg_id="",markup=""):
    send_url=f"https://api.telegram.org/bot{token}/sendMessage"
    if('reply_to_message_id'!=""):
        data={
            'chat_id':chat_id,
            'text':text,
            'reply_to_message_id':reply_to_msg_id
        }
    else:
        data={
            'chat_id':chat_id,
            'text':text,
        }

    response=requests.post(send_url,data)
    return response.json()