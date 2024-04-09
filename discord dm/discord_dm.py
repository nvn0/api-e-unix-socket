import os
from dotenv import load_dotenv, dotenv_values
import requests


##################################################################
# Não é um bot usa uma conta normal para enviar mensagens
##################################################################


#load from .env
load_dotenv('.env')
key: str = os.getenv('KEY')

#print(key)


def createDm(user_id):
    payload = {
        'recipient_id': user_id
    }
    
    header = {
        'Content-Type': 'application/json',
        'authorization': key
    }

    url = "https://discord.com/api/v9/users/@me/channels"
    
    r = requests.post(url, json=payload, headers=header)
    print(r.status_code)
    #print(r.json())

    channel_id = r.json()['id']
    
    return channel_id
    
    
    

def send_dm(user_id):

    #id = int(input("user ID: "))
    
    channel_id = createDm(user_id)
    
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    
    header = {  
        'authorization': key
    }


    payload = {
        'content': "O seu pedido foi conluido"
    }

    

    r = requests.post(url, data=payload, headers=header)
    print(r.status_code)
    
    
    
    
    