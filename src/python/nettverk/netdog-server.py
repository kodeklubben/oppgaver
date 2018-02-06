#!/usr/bin/env python3

import socket
import threading
from random import randint
from multiprocessing import Process
import os
import hashlib
import time


def printdog():
    doglist = []
    doglist.append(r"    /^ ^\ \n   / 0 0 \ \n   V\ Y /V\n    / - \ \n    |    \ \n    || (__V\n")
    doglist.append(r"   __\no-''|\_____/)\n \_/|_)     )\n    \  __  /\n    (_/ (_/    hjw\n")
    doglist.append(r"    _____^_\n   |    |    \\\n    \   /  ^ |\n   / \_/   0  \\\n  /            \\\n /    ____      0\n/      /  \___ _/\n")
    doglist.append(r"     |\_/|\n     | @ @   Woof!\n     |   <>              _\n     |  _/\------____ ((| |))\n     |               `--\' |\n  ___|_        __|   |___.\'\n /_/_____/____/_______|	\n")
    doglist.append(r"         .--.             .---.\n        /:.  \'.         .\' ..  \'._.---. \n       /:::-.  \.-\"\"\"-;` .-:::.     .::\\ \n      /::\'|  `\/  _ _  \'    `\:\'   ::::| \n  __.\'    |   /  (o|o)  \     `\'.   \':/ \n /    .:. /   |   ___   |        \'---\' \n|    ::::\'   /:  (._.) .:\\ \n\    .=\'    |:\'        :::| \n `\"\"`       \     .-.   \':/ \n       jgs   \'---`|I|`---\' \n                  \'-\' \n")
    print(doglist[randint(0, len(doglist)-1)])
    print("Starter netdog-server\n\n")


def info(title):
    print(title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def get_navn_melding(foresporsel):
    separator = foresporsel.find(':')
    navn = foresporsel[:separator]
    melding = foresporsel[separator+1:]
    return navn, melding


def brute_force_thread():
    print("brute force thread")


def brute_force_main(bind_port):
    print("Starter brute force pa port: ", port)
    bind_ip = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(10)

    while True:
        client,addr = server.accept()


def din_ip_thread(client_socket, faktisk_ip):
    while True:
        foresporsel = client_socket.recv(2048).decode()
        navn, melding = get_navn_melding(foresporsel)

        if melding == "":
            client_socket.close()
            return
        elif melding == "oppgave":
            svar = "I denne oppgaven maa du sende meg din IP-adresse. Hint: ipconfig eller ifconfig"
        elif melding == faktisk_ip:
            svar = 'Suksess! Du fant IP-adressen din'
        else:
            svar = melding +' er ikke IP-adressen din'
        client_socket.send(svar.encode())

    client_socket.close()


def din_ip_main(bind_port):
    print("Oppgaven DIN IP kjorer paa port ", bind_port)
    bind_ip = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(10)

    while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=din_ip_thread,args=(client, str(addr[0])))
        client_handler.start()


def passordhash_thread(client_socket,faktisk_digest):
    while True:
        foresporsel = client_socket.recv(2048).decode()
        navn, melding = get_navn_melding(foresporsel)

        if melding == "":
            client_socket.close()
            return
        elif melding == "oppgave":
            # svar = "I denne oppgaven maa du sende in riktig passord.\nHint: Passordet er et tall mellom 0 og 1 000 000.\nEtter aa ha kjort passordet funksjonen SHA1 er passordet "+ faktisk_digest +"\nFor aa kjore et passord gjennom SHA1 i python bruker du folgende kode:\nimport hashlib\nhashobject = hashlib.sha1(str(passord))\ndigest = hashobject.hexdigest()"
            svar = """I denne oppgaven maa du sende in riktig passord.
Hint: Passordet er et tall mellom 0 og 1 000 000.
Etter aa ha kjort passordet funksjonen SHA1 er passordet "+ {} +"
For aa kjore et passord gjennom SHA1 i python bruker du folgende kode:
import hashlib
hashobject = hashlib.sha1(str(passord).encode())
digest = hashobject.hexdigest()
""".format(faktisk_digest)
        else:
            hashobject = hashlib.sha1(melding.encode("utf-8"))
            bruker_digest = hashobject.hexdigest()
            if faktisk_digest == bruker_digest:
                svar = 'Suksess! Du fant passordet'
            else:
                svar = melding +' er ikke passordet'
        client_socket.send(svar.encode())

    client_socket.close()


def passordhash_main(bind_port):
    print("Oppgaven PASSORDHASH kjorer paa port ", bind_port)
    bind_ip = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip,bind_port))
    server.listen(10)
    passord = randint(0,1000000)
    #print("passordet er ", passord)
    hashobject = hashlib.sha1(str(passord).encode())
    digest = hashobject.hexdigest()

    while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=passordhash_thread,args=(client,digest))
        client_handler.start()


if __name__=='__main__':
    func_list=[din_ip_main, passordhash_main]
    port = 10000
    for func in func_list:
        p = Process(target=func,args=(port,))
        p.start()
        port += 1
    exit()
