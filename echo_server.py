from socket import *

server_socket = socket(AF_INET,SOCK_STREAM)

server_socket.bind(('',12000))
server_socket.listen(1)

while 1:
    print '##### Server is ready to receive messages #####'
    conn_socket, addr = server_socket.accept()
    sentence = conn_socket.recv(1024)
    cap_sentence = sentence.upper()
    print 'message converted: ', cap_sentence
    conn_socket.send(cap_sentence)
    conn_socket.close()