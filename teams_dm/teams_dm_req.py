import requests

def Send_dm_teams(user_id):


    payload = {
        "user_id": user_id,
        "message": "O seu pedido foi conluido"
    }
    
    header = {
        'Content-Type': 'application/json'
    }

    url = "http://localhost:3900/api/send-message"
    
    r = requests.post(url, data=payload, headers=header)
    print(r.status_code)