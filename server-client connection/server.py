# 1.bind() method which can bind particular IP's and Ports
# 2. listen() method which allows servers to listen incoming connections
# 3. accept() accepts connection with a client
# 4. close() closes connection with a client


import socket

s=socket.socket()
print("socket created successfully")

port=56785

s.bind(('', port))
print(f'socket binded with port {port}')

s.listen(5)
print('socket is listening')

while True:
    c, addr = s.accept()
    print('got connection from', addr)
    message = ('Thank you for connecting')

    c.send(message.encode())
    c.close()
