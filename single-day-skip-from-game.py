import socket
import time
import binascii
from config import switchIP

def sendCommand(s, content):
    content += '\r\n' #important for the parser on the switch side
    s.sendall(content.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((switchIP, 6000))
dSpeed = 0.07

print("Starting")
time.sleep(1)
while True:
    sendCommand(s, "click HOME")
    time.sleep(2)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click DDOWN")
    time.sleep(dSpeed)
    sendCommand(s, "click A")
    time.sleep(1)
    print('setting day')
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DUP")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click DRIGHT")
    time.sleep(dSpeed)
    sendCommand(s, "click A")
    time.sleep(1)
    sendCommand(s, "click HOME")
    time.sleep(2)
    sendCommand(s, "click HOME")
    print("Finished")
    time.sleep(2)
    break

    