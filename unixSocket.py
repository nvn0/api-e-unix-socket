import socket
import os
import json
import time

# Caminho do ficheiro do socket
socket_path = "/tmp/socket_proj"

def socketPath():
    return "/tmp/meu_socket"

# Verificar se o ficheiro do socket existe
if not os.path.exists(socket_path):
    print("O ficheiro do socket não existe.")
    exit()


def sendPort(container, tipo, action, firewall, protocol, porta):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Container": container,
            "Type": tipo,
            "Action": action,
            "Fw": firewall,
            "protocol": protocol,
            "Port": porta
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.5)
        # Receber a resposta do servidor
        #response_json = client_socket.recv(1024).decode()))
        #response = json.loads(response_json)

        # mosrar a resposta do servidor
        #print("Status:", response["Status"])
        #print("Mensagem:", response["Mensagem"])

        # Fechar o socket do cliente
        client_socket.close()

    except Exception as e:
        print("Ocorreu um erro:", e)




def GetInfo(container, tipo):

    socket_path = socketPath()

    try:
        # Criar um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectar ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviar uma mensagem para o servidor
        
        json_data = {
            "Container": container,
            "Type": tipo,
            "Action": "GetInfo"
        }
        
        client_socket.send(json.dumps(json_data).encode())


        time.sleep(1.5)
        # Receber a resposta do servidor
        response_json = client_socket.recv(1024).decode()
        response = json.loads(response_json)

        # mostrar a resposta do servidor
        print("Status:", response["Status"])
        print("Estado:", response["Estado"])
        print("Ports:", response["Ports"])
        
        
        
        # Fechar o socket do cliente
        client_socket.close()
        
        return response

    except Exception as e:
        print("Ocorreu um erro:", e)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
