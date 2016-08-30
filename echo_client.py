from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost',12000))

sentence = raw_input('Input lowercase sentence:')
client_socket.send(sentence)

modified_sentence = client_socket.recv(1024)
print 'From Server:', modified_sentence

client_socket.close()