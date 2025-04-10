import socket
from threading import Thread


class Server:
    Clients = []

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', PORT))
        self.socket.listen(5)
        print('Server waiting for connections....')

    def listen(self):
        while True:
            client_socket, address = self.socket.accept()
            print(f"New connection from {address}")

            client_name = client_socket.recv(1024).decode()
            client = {'client_name': client_name, 'client_socket': client_socket}

            self.broadcast_message(client_name, f"{client_name} has joined the chat")

            Server.Clients.append(client)
            Thread(target=self.handle_new_client, args=(client,)).start()

    def handle_new_client(self, client):
        client_name = client['client_name']
        client_socket = client['client_socket']
        while True:
            try:
                client_message = client_socket.recv(1024).decode()
                if not client_message or client_message.strip() == f"{client_name}: bye":
                    self.broadcast_message(client_name, f"{client_name} has left the chat!")
                    Server.Clients.remove(client)
                    client_socket.close()
                    break
                else:
                    self.broadcast_message(client_name, client_message)
            except:
                Server.Clients.remove(client)
                client_socket.close()
                break

    def broadcast_message(self, sender_name, message):
        for client in Server.Clients:
            try:
                client['client_socket'].sendall(f"{sender_name}: {message}".encode())
            except:
                client['client_socket'].close()
                Server.Clients.remove(client)


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 1234
    server = Server(HOST, PORT)
    server.listen()
