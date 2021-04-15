import socket
hostname= socket.gethostname()
ip=socket.gethostbyname(hostname)
print("nombre del ordenador:"+hostname)
print("ip:"+ip)

