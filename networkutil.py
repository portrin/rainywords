import socket
import pickle

class Agent():
    def __init__(self, end_point_addr, end_point_port, own_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        self.end_point_addr = end_point_addr #for client socket endpoint
        self.end_point_port = end_point_port #for client socket endpoint
        self.own_socket = own_socket #pass own socket obj (both client and server)

    def connect(self):
        try:
            self.own_socket.connect((self.end_point_addr, self.end_point_port)) 
            #return self.receive()
        except:
            print("cannot connect to ", self.end_point_addr)
            pass

    def send(self, data):
        try:
            sent = self.own_socket.send(pickle.dumps(data))
            return sent
        except socket.error as error:
            print(error)

    def receive(self):
        try:
            message = self.own_socket.recv(2048) #return as str 
            return pickle.loads(message)
        except:
            print('could not receive any message')
            pass
