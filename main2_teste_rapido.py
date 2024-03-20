from flask import Flask, request, jsonify
import re

from unixSocket import *


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'The API is running...', 200
    
    
    
    
@app.route("/send_port", methods=["POST"])
def send_port():
    data = request.get_json()

#    {
#        "Container":
#        "Type":
#        "Port":
#    }

    data = request.get_json()

    container = data['Container']
    tipo = data['Type']
    porta = data['Port']
    

    print(container)
    print(tipo)
    print(porta)
    
    sendPort(container, tipo, porta)

    
    return jsonify(data, "WORKING!!!"), 201
    return 'Sucesso', 201





if __name__ == "__main__":
    app.run(debug = True)




