import socket
from threading import Thread


class Client:

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((HOST, PORT))
        self.name = input("Enter your name: ")

        self.talk_to_server()

    def talk_to_server(self):
        self.socket.send(self.name.encode())
        Thread(target=self.receive_message).start()
        self.send_message()

    def send_message(self):
        while True:
            client_input = input("")
            client_message = f"{self.name}: {client_input}"
            self.socket.send(client_message.encode())
            if client_input.lower() == "bye":
                print("You left the chat.")
                self.socket.close()
                break

    def receive_message(self):
        while True:
            try:
                server_message = self.socket.recv(1024).decode()
                if not server_message:
                    print("Server disconnected.")
                    self.socket.close()
                    break
                print("\033[1;31;40m" + server_message + "\033[0m")
            except:
                break


if __name__ == "__main__":
    HOST = 'server'
    PORT = 1234
    Client(HOST, PORT)
