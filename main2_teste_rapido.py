from flask import Flask, request, jsonify
import re
from flask_httpauth import HTTPBasicAuth
#from werkzeug.security import generate_password_hash, check_password_hash
#import os
#from unixSocket import *
from pass_hash import *




app = Flask(__name__)

auth = HTTPBasicAuth()



USER_FILE = 'users.txt'

users = {}

def read_users():
    #users = {}
    try:
        with open(USER_FILE, 'r') as f:
            for line in f:
                username, password_hash = line.strip().split(':')
                users[username] = password_hash
    except FileNotFoundError:
        pass  # Arquivo ainda não existe, sem problema
    return users

users = read_users()
#print(users)

@auth.verify_password
def verify_password(username, password):
    try:
        #users = read_users()
        ph = phash(password)
        if username in users and ph == users[username]:
            return username
        return None
    except:
        print("erro ao verificar user")











# adicionar decorator -> @auth.login_required



# ---------------------------- path ----------------------

@app.route('/')
def homepage():
    return 'The API is running...', 200
    


 
@app.route("/host_fw", methods=["POST"]) # executar no host
def host_fw():
    

#    {
#        "Action":
#        "Fw":
#        "protocol":
#        "Port":
#    }

    try:
        data = request.get_json()

        
        action = data['Action']
        firewall = data['Fw']
        protocol = data['Protocol']
        porta = data['Port']
    except:
        print("Erro ao receber dados!")
        return "Error ao receber os dados", 500
    else:

   
        print(action)
        print(firewall)
        print(protocol)
        print(porta)


        hostfw(action, firewall, protocol, porta)

        
        return jsonify(data, "WORKING!!!"), 201  


@app.route("/host_nat", methods=["POST"]) # executar no host
def host_nat():
    

#    {
#        "Action":
#        "Fw":
#        "Protocol":
#        "Port":
#        "Container_internal_ip":
#        "Container_internal_port":
#    }

    action = ""
    firewall = ""
    protocol = ""
    porta = ""
    cont_ip = ""
    cont_port = ""

    try:
        data = request.get_json()

        
        action = data['Action']
        firewall = data['Fw']
        protocol = data['Protocol']
        porta = data['Port']
        cont_ip = data['Container_internal_ip']
        cont_port = data['Container_internal_port']
        
    except:
        print("Erro ao receber dados!")
        return "Error ao receber os dados", 500
    else:

       
        print(action)
        print(firewall)
        print(protocol)
        print(porta)
        print(cont_ip)
        print(cont_port)


        hostnat(action, firewall, protocol, porta, cont_ip, cont_port)

    
        return jsonify(data, "WORKING!!!"), 201


########################## containers ###################################    
    
@app.route("/send_port", methods=["POST"])
def send_port():
    

#    {
#        "Container":
#        "Type":
#        "Action":
#        "Fw":
#        "protocol":
#        "Port":
#    }

    



    
    try:
        data = request.get_json()

        container = data['Container']
        tipo = data['Type']
        action = data['Action']
        firewall = data['Fw']
        protocol = data['Protocol']
        porta = data['Port']
        
    except:
        print("Erro ao receber dados!")
        return "Error ao receber os dados", 500
    else:

        print(container)
        print(tipo)
        print(action)
        print(firewall)
        print(protocol)
        print(porta)


        sendPort(container, tipo, action, firewall, protocol, porta)

        
        return jsonify(data, "WORKING!!!"), 201
   


@app.route("/get_info", methods=["POST"])
def get_info():
    

#    {
#        "Container":
#        "Type":
#    }

    try:
        data = request.get_json()

        container = data['Container']
        tipo = data['Type']
        #action = data['Action']
    except:
        print("Erro ao receber dados!")
        return "Error ao receber os dados", 500
    else:
    

        print(container)
        print(tipo)
        #print(action)
       
        
        resposta = GetInfo(container, tipo)

        
        return jsonify(data, "Resposta: ",resposta, "WORKING!!!"), 201
   


if __name__ == "__main__":
    app.run(debug = True)




