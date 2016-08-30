from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("www.ucsd.edu", 80))
s.send("GET / HTTP/1.0\r\n\r\n")
data = s.recv(1024)
print data
s.close()