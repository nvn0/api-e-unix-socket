import smtplib
import os
from dotenv import load_dotenv, dotenv_values

#load from .env
load_dotenv('.env')
password: str = os.getenv('PASSWORD')


def Send_email(email):
    
    sender_email = "a036785@ipmaia.pt"

    
    
    receiver_email = email
    
    subject = "Pedido de porta"
    mensagem = "O seu pedido foi aceite"
    
    text = f"Subject: {subject} \n\n{mensagem}"
    
    #server = smtplib.SMTP("smtp.gmail.com", 587)
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    
    server.login(sender_email, password)
    
    server.sendmail(sender_email, receiver_email, text)
    
    
