---
title: "Nettverk: finn din IP"
level: 3
author: André Mruz
language: nb
tags:
  topic: [network]
  subject: [programming]
  grade: [secondary]
---

# Introduksjon {.intro}

I denne oppgaven skal du få koble deg til en annen datamaskin. Den andre
datamaskinen må være på samme nettverk som din egen.

Til denne oppgaven trenger du to datamaskiner. På din egen datamaskin gjør du
oppgaven. Vi kaller din datamaskin for _klienten_. Den andre datamaskinen tester
om du skriver inn rett svar på oppgaven. Den andre datamaskinen kaller vi
_serveren_.

Er du på kodeklubb, er serveren allerede satt opp. Du skriver kun kode som skal
på klienten. Hvis du vil gjøre oppgaven selv utenfor kodeklubb, kan du sette opp
serveren selv. Sjekk da [lærerveiledningen](./README.html)!

# Steg 0: Koble til IP

Du skal kunne se denne siden på din egen PC. Gå til adressen du ser i
adressefeltet.

# Steg 1: Laste ned kode

I denne oppgaven skal du bruke kode som allerede finnes.

Start med
[netdog-client](./netdog-client.py).

# Steg 2: TODO DEL INN I STEG

- Nå skal vi lære litt om hvordan man kan bruke python til å sende meldinger over
  et nettverk. Altså hvordan man kan sende en melding fra en datamaskin til en
  annen.

- Vi skal bruke programmet «netdog-client.py» til å koble oss til en annen
  maskin på samme nettverk som din maskin. Du kan starte programmet ved å
  skrive: python netdog-client.py.

- Først må du skrive inn navnet ditt.

- Så må du skrive in ip-adressen til lærerens(finn bedre ord) maskin. En
  ip-adresse forteller hvor meldinger skal sendes. Den er litt som gateadressen
  der du bor, men er bare et tall. Den kan se slik ut: 168.10.100.2

- Så må du skrive inn porten programmet på den andre datamaskinen kjører på.
  Hvis flere programmer på samme maskin sender meldinger, får de hver sin port.
  Hvis ip-adressen sammenlignes med en gateadresse, så er porten litt som et
  leilighetsnummer. Det kan være flere leiligheter på samme gateadresse.

- Nå kan du sende meldinger til den andre maskinen. Bare skriv meldingen og
  trykk enter. Hvis du sender meldingen oppgave vil du få tilbake en beskrivelse
  av oppgaven. I denne oppgaven må du sende inn din datamaskin sin ip-adresse.
  På en windows-maskin kan du finne den ved å åpne programmet cmd og skrive
  ipconfig. På en MAC-maskin må du åpne programmet terminal og skrive ifconfig.
