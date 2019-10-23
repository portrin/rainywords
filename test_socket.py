from networkutil import Agent
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = "0.0.0.0"
port = 5000
agent = Agent(mysocket, addr, port)
print(agent.connect())
print(agent.send("test"))
agent.own_socket.close()
