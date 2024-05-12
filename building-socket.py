import socket

import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.AF_INET = refers to the address family ipv4

#socket.SOCK_STREAM = refers to TCP protocol //checks connection is established or not
import socket

hostname = 'www.github.com'
ip = socket.gethostbyname(hostname)
print(f"The IP address of {hostname} is {ip}")




