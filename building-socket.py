import socket

import sys


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print(f"socket creation failed with error {err}")

# socket.AF_INET = refers to the address family ipv4

#socket.SOCK_STREAM = refers to TCP protocol //checks connection is established or not
 
# hostname = 'www.github.com'
# ip = socket.gethostbyname(hostname)
# print(f"The IP address of {hostname} is {ip}")

port = 80
try:
    host_ip = socket.gethostbyname("www.github.com")
except socket.gaierror:
#gaierror = error with DNS server
    print("there was an error resolving the host")
    sys.exit()
s.connect((host_ip, port))
print(f"the socket has successfully connected to github on port = {host_ip}")