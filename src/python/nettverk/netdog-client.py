#!/usr/bin/env python3

import socket
from random import randint
import os
import sys


def printdog():
    doglist = []
    doglist.append(r"    /^ ^\ \n   / 0 0 \ \n   V\ Y /V\n    / - \ \n    |    \ \n    || (__V\n")
    doglist.append(r"   __\no-''|\_____/)\n \_/|_)     )\n    \  __  /\n    (_/ (_/    hjw\n")
    doglist.append(r"    _____^_\n   |    |    \\\n    \   /  ^ |\n   / \_/   0  \\\n  /            \\\n /    ____      0\n/      /  \___ _/\n")
    doglist.append(r"     |\_/|\n     | @ @   Woof!\n     |   <>              _\n     |  _/\------____ ((| |))\n     |               `--\' |\n  ___|_        __|   |___.\'\n /_/_____/____/_______|	\n")
    doglist.append("         .--.             .---.\n        /:.  \'.         .\' ..  \'._.---. \n       /:::-.  \.-\"\"\"-;` .-:::.     .::\\ \n      /::\'|  `\/  _ _  \'    `\:\'   ::::| \n  __.\'    |   /  (o|o)  \     `\'.   \':/ \n /    .:. /   |   ___   |        \'---\' \n|    ::::\'   /:  (._.) .:\\ \n\    .=\'    |:\'        :::| \n `\"\"`       \     .-.   \':/ \n       jgs   \'---`|I|`---\' \n                  \'-\' \n")
    print(doglist[randint(0,len(doglist)-1)])
    print("Starter netdog-client\n\n")


def connect():
    try:
        #navn = raw_input("Hva heter du?\n")
        navn = "Andre"
        #remote_ip = raw_input("Hvilken ip adresse vil du koble deg til?\n")
        remote_ip = "127.0.0.1"
        #remote_port = int(raw_input("Hvilken port vil du koble deg til?\n"))
        remote_port = 10000
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((remote_ip, remote_port))
        print("Skriv melding\n")
        while True:
            melding = input("")
            if melding == "":
                client.send(navn+":")
                break

            client.send((navn+":"+melding).encode())
            svar = client.recv(2048).decode()
            print(svar)
    finally:
        client.close()
    print('Avslutter netdog-client\n')


if __name__ == '__main__':
    printdog()
    connect()
