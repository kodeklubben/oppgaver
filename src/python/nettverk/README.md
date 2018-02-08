---
title: "Nettverk: finn din IP"
level: 3
language: nb
---

# Om oppgaven {.activity}

I denne oppgaven bruker vi Python til å snakke over nettverk. Veilederen starter
en server som de som løser oppgaven programmerer mot.

## Hvor er du på nettverket? {.check}

**IP-adresser** identifiserer datamaskinen vår på et nettverk. Hvis jeg vet din
IP-adresse, kan jeg sende en melding til deg. For å finne din IP-adresse på
nettverket, kan du prøve `ipconfig` på Windows og `ip addr` eller `ifconfig` på
Linux/Mac.

- [ ] Finn din IP-adresse. Denne trenger du for at andre skal finne deg!

## Kjør _netdog_ {.check}

- [ ] Last ned og kjør [netdog-server.py](./netdog-server.py). Hvilken port
      startet _netdog_ på?.

**Porter** lar flere applikasjoner bruke nettverket på samme datamaskin
samtidig. Jeg kan be om å reservere port 3000 på min datamaskin. Hvis
operativsystemet ikke allerede har gitt denne til en annen prosess, får jeg lov.
Porter er tall mellom 0 og 65536 (2^16-1). Port 0-1023 er ofte reservert til
operativsystemet, så vi velger typisk høyere portnumre.

