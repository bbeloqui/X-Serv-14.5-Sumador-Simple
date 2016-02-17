#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
estado = True
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        barra_num = recvSocket.recv(1031)
        numero = barra_num.split()[1][1:]
        print 'Answering back...'
        print numero
        if estado == True : 
            numero1 = int(numero)   
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Primer sumando: " + str(numero1) +
                        "</body></html>" + "\r\n")
            estado = False
        else :

            resultado = numero1 + int(numero)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Primer sumando: " + str(numero1) +
                        "</h1></body></html>" + "\r\n")
            recvSocket.send("<html><body><h1>Segundo sumando: " + str(numero) +
                        "</h1></body></html>" + "\r\n")
            recvSocket.send("<html><body><h1>La suma es: " + str(resultado) +
                        "</h1></body></html>" + "\r\n")
            estado = True
            print  resultado
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
