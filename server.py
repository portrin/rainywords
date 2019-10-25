import sys
import socket 
import _thread
import pygame
from networkutil import Agent

server_ip = "0.0.0.0" #change to server ip later!
port = 5000

width = 600
height = 600
pygame.font.init()
pygame.display.init()
font = pygame.font.SysFont("comicsansmsttf", 32)
number_of_player = 0
player_id = 0
score = [0,0] #storing players score
username = ['', '']
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainy Words Server")

#define socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((server_ip, port))
server_socket.listen(3)
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
                    'score' : score,
                    'username' : username,
                    'status' : '',
                    'reset' : False})
        message = agent.receive()
        print(message)
        print(score)
        try:
            if message['player_id'] == 1:
                score[0] = message['score']
                username[0] = message['username']
            elif message['player_id'] == 2:
                score[1] = message['score']
                username[1] = message['username']
            if message['status'] == 'exit':
                break
        except:
            pass
    while True:
        print('exit')
        # agent.send({'player_id' : player_id,
        #             'number_of_player' : number_of_player,
        #             'score' : score,
        #             'username' : username,
        #             'status' : '',
        #             'reset' : False})
        
while True: #main server handler
    window.fill((255,255,255))
    text = font.render('number of player ' + str(number_of_player) + ' username ' + str(username), True, (0,255,0))
    window.blit(text, (200,200))
    pygame.display.update()
    player_socket, addr = server_socket.accept()
    print("connected to ", addr)
    number_of_player += 1
    _thread.start_new_thread(thread_player, (player_socket, )) #thread func, func(args)



