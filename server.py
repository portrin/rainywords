import sys
import socket 
import _thread
from networkutil import Agent

server_ip = "0.0.0.0" #change to server ip later!
port = 5000

number_of_player = 0
player_id = 0
score = [0,0] #storing players score

#define socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, port))
server_socket.listen(1)
print('server is waiting for connection')

def thread_player(player_socket):
    agent = Agent('', 5000, own_socket = player_socket)
    global number_of_player 
    print(player_socket) # for debugging
    print(number_of_player)
    player_id = number_of_player
    while True:
        agent.send({'player_id' : player_id,
                    'number_of_player' : number_of_player,
                    'score' : score})
        print(agent.receive())

while True: #main server handler
    print("before accept")
    player_socket, addr = server_socket.accept()
    print("connected to ", addr)
    number_of_player += 1
    _thread.start_new_thread(thread_player, (player_socket, )) #thread func, func(args)



