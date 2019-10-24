from networkutil import Agent
import socket


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = "0.0.0.0"
port = 5000
agent = Agent(addr, port)
print(agent.own_socket)
agent.connect()
while True:
    print(agent.receive())
    print(agent.send(''))

