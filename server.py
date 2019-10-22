import sys
import socket 
import _thread
from networkutil import Agent

server_ip = "0.0.0.0" #change to server ip later!
port = 5000

number_of_player = 0
score = [0,0] #storing players score

#define socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(), port))
server_socket.listen(1)
print('server is waiting for connection')

def thread_player(player_socket):
    print(player_socket) # for debugging
    agent = Agent(player_socket) #create handler for each player
    pass

while True: #main server handler
    player_socket, addr = server_socket.accept()
    print("connected to ", addr)
    _thread.start_new_thread(thread_player, (player_socket,)) #thread func, func(args)



