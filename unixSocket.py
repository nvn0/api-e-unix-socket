import socket
import os

# Caminho do arquivo do socket
socket_path = "/tmp/meu_socket"

def socketPath():
    return "/tmp/meu_socket"

# Verificando se o arquivo do socket existe
if not os.path.exists(socket_path):
    print("O arquivo do socket não existe.")
    exit()


def sendPort(container, tipo, porta):

    socket_path = socketPath()

    try:
        # Criando um socket Unix
        client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Conectando ao servidor Unix socket
        client_socket.connect(socket_path)

        # Enviando uma mensagem para o servidor
        message = container+tipo+porta
        client_socket.sendall(message.encode())

        # Recebendo a resposta do servidor
        response = client_socket.recv(1024)
        print("Resposta do servidor:", response.decode())

        # Fechando o socket do cliente
        client_socket.close()

    except Exception as e:
        print("Ocorreu um erro:", e)
