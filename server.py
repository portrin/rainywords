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

server_socket.bind((server_ip, port))
server_socket.listen(1)
print('server is waiting for connection')

def thread_player(player_socket):
    agent = Agent(player_socket)
    global number_of_player 
    agent.send({"player_id": number_of_player})
    print(player_socket) # for debugging
    print(number_of_player)
    while True:
        while number_of_player < 2:
            agent.send(number_of_player)
        agent.receive()
        agnet.send(score)
    pass

while True: #main server handler
    player_socket, addr = server_socket.accept()
    print("connected to ", addr)
    number_of_player += 1
    _thread.start_new_thread(thread_player, (player_socket, )) #thread func, func(args)



