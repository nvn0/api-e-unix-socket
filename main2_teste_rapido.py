from flask import Flask, request, jsonify
import re

from unixSocket import *


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'The API is running...', 200
    
@app.route("/host_fw", methods=["POST"]) # executar no host
def host_fw():
    data = request.get_json()

#    {
#        "Action":
#        "Fw":
#        "protocol":
#        "Port":
#    }

    data = request.get_json()

    
    action = data['Action']
    firewall = data['Fw']
    protocol = data['Protocol']
    porta = data['Port']
    

   
    print(action)
    print(firewall)
    print(protocol)
    print(porta)


    hostfw(action, firewall, protocol, porta)

    
    return jsonify(data, "WORKING!!!"), 201
    return 'Sucesso', 201    


@app.route("/host_nat", methods=["POST"]) # executar no host
def host_nat():
    data = request.get_json()

#    {
#        "Action":
#        "Fw":
#        "Protocol":
#        "Port":
#        "Container_internal_ip":
#        "Container_internal_port":
#    }

    data = request.get_json()

    
    action = data['Action']
    firewall = data['Fw']
    protocol = data['Protocol']
    porta = data['Port']
    cont_ip = data['Container_internal_ip']
    cont_port = data['Container_internal_port']
    

   
    print(action)
    print(firewall)
    print(protocol)
    print(porta)
    print(cont_ip)
    print(cont_port)


    host_nat(action, firewall, protocol, porta, cont_ip, cont_port)

    
    return jsonify(data, "WORKING!!!"), 201
    return 'Sucesso', 201   


########################## containers ###################################    
    
@app.route("/send_port", methods=["POST"])
def send_port():
    data = request.get_json()

#    {
#        "Container":
#        "Type":
#        "Action":
#        "Fw":
#        "protocol":
#        "Port":
#    }

    data = request.get_json()

    container = data['Container']
    tipo = data['Type']
    action = data['Action']
    firewall = data['Fw']
    protocol = data['Protocol']
    porta = data['Port']
    

    print(container)
    print(tipo)
    print(action)
    print(firewall)
    print(protocol)
    print(porta)


    sendPort(container, tipo, action, firewall, protocol, porta)

    
    return jsonify(data, "WORKING!!!"), 201
    return 'Sucesso', 201


@app.route("/get_info", methods=["POST"])
def get_info():
    data = request.get_json()

#    {
#        "Container":
#        "Type":
#    }

    data = request.get_json()

    container = data['Container']
    tipo = data['Type']
    #action = data['Action']
    
    

    print(container)
    print(tipo)
    #print(action)
   
    
    resposta = GetInfo(container, tipo)

    
    return jsonify(data, "Resposta: ",resposta, "WORKING!!!"), 201
    return 'Sucesso', 201


if __name__ == "__main__":
    app.run(debug = True)




