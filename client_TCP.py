#!/usr/bin/python
# -*- coding: utf-8 -*-
###################################################################
######################   CLIENT TCP  ##############################
###################################################################

## import module socket
import socket

## DÃ©finition de la cible

target_host = "127.0.0.1"
target_port = 8080

## creation d'un objet

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## connexion au serveur

client.connect((target_host, target_port))

## Envoyer des donnees au serveur

request = raw_input("what you want to say?\n")
client.send(request)

## Recevoir des donnees du serveur

response = client.recv(4096)
print response
