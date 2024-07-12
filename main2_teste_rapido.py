from flask import Flask, request, jsonify
import re
#from flask_httpauth import HTTPBasicAuth
import json
#import os
from unixSocketConn import *
from pass_hash import *




app = Flask(__name__)




#######################################  Sec de RE  ###################################################


re_ip = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'


def is_valid_ip(ip):
    if re.match(re_ip, ip):
        return True
    else:
        return False


##############################################################################################





############################ Sec de autenticação ########################################

#auth = HTTPBasicAuth()
#
#
#
#USER_FILE = 'users.txt'
#
#users = {}
#
#def read_users():
#    #users = {}
#    try:
#        with open(USER_FILE, 'r') as f:
#            for line in f:
#                username, password_hash = line.strip().split(':')
#                users[username] = password_hash
#    except FileNotFoundError:
#        pass  # Arquivo ainda não existe, sem problema
#    return users
#
#users = read_users()
##print(users)
#
#@auth.verify_password
#def verify_password(username, password):
#    try:
#        #users = read_users()
#        ph = phash(password)
#        if username in users and ph == users[username]:
#            return username
#        return None
#    except:
#        print("erro ao verificar user")
#


# adicionar decorator -> @auth.login_required

####################################################################





# ---------------------------- path ----------------------

@app.route('/')
def homepage():
    #print(request.remote_addr)
    
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print(request.environ['REMOTE_ADDR'])
    else:
        print(request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        
    return 'The API is running...', 200
    


@app.route("/get_ip_ports", methods=["POST"]) # executar no host
def host_get_nat_ip_ports():
    

#    {
#        "Action":
#        "External_ip":
#    }

    action = ""
    external_ip = ""


    try:
        data = request.get_json()

        
        action = data['Action']
        external_ip = data['External_ip']
        
    except:
        print("Erro ao receber dados!")
        return "Error ao receber os dados", 500
    else:

   
        print(action)
        print(external_ip)


        response = host_nat_ip_ports(action, external_ip)

        
        return jsonify(response, "Solicitacao bem sucedida!"), 201 



 
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

        
        return jsonify(data, "Solicitacao bem sucedida!"), 201  


@app.route("/host_nat", methods=["POST"]) # executar no host
def host_nat():
    

#    {
#        "Action":
#        "Fw":
#        "Protocol":
#        "Port":
#        "External_ip":
#        "Container_internal_ip":
#        "Container_internal_port":
#    }

    action = ""
    firewall = ""
    protocol = ""
    porta = ""
    external_ip = ""
    cont_ip = ""
    cont_port = ""

    try:
        data = request.get_json()
        print(data)
        
        action = data['Action']
        firewall = data['Fw']
        protocol = data['Protocol']
        porta = data['Port']
        external_ip = data['External_ip']
        cont_ip = data['Container_internal_ip']
        cont_port = data['Container_internal_port']
        
    except Exception as error:
        return error, 400
    else:

       
        print(action)
        print(firewall)
        print(protocol)
        print(porta)
        print(external_ip)
        print(cont_ip)
        print(cont_port)

        if is_valid_ip(cont_ip) == True:
            hostnat(action, firewall, protocol, porta, external_ip, cont_ip, cont_port)
            print("IP do container validado!")
            return jsonify(data, "WORKING!!!"), 201
        else:
            print("Formato do IP incorreto!")
            return jsonify(data, "Erro no formato do IP"), 400


########################## containers ###################################    
    
@app.route("/cont_port", methods=["POST"])
def cont_port():
    

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


        contPort(container, tipo, action, firewall, protocol, porta)

        
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




