#!/usr/bin/python
# -*- coding: utf-8 -*-
##################################################
##################  SERVEUR TCP ##################
##################################################

## Import des sockets

import socket
import threading

## Adresse et port d'ecoute

bind_ip = "0.0.0.0"
bind_port = 8080

## Mettre la console en ecoute

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

## Activer nombre d'Ã©coute et affiche un message

server.listen(5)
print "[*] listening on %s:%d" %(bind_ip,bind_port)

## Fonction pour recevoir et envoyer des paquets

def handle_client(client_socket):
	request = client.recv(2048)
	print ("[*] Received: %s" % request)
	response = raw_input("what you want to say ?\n")
	client_socket.send(response)
	client_socket.close()

## Serveur en ecoute en boucle
	
i = 0
while i < 100:
        client,addr = server.accept()   
        print ("[*] Accepted connection from %s:%d" %(addr[0],addr[1]))
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

