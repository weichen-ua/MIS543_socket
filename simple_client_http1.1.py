from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.ucsd.edu", 80))
get_req = "GET / HTTP/1.1\r\n" + "Host:www.ucsd.edu\r\n\r\n"
s.send(get_req.encode())
data = s.recv(1024)
print(data)
s.close()