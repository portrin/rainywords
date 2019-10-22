from networkutil import Agent
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = "172.20.10.2"
port = 5000
agent = Agent(mysocket, addr, port)
agent.connect()
print(agent.send("test"))
agent.own_socket.close()
