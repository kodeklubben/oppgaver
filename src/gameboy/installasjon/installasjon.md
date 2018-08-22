---
title: Installering av GBDK og Bgb
indexed: False
language: nb
---

# Vis filtyper (Kun Windows) {.activity}

Dette er et steg du kan hoppe over hvis du har gjordt dette tidligere.

For å endre filtypene til de forskjellige filene, er det lettest å endre dem
med å gi dem et nytt navn.

Under står instruksjoner for å vise filtyper.

## Sjekkliste {.check}

- [ ] Åpne et filutforsker-vindu

- [ ] I raden på toppen velger du "Vis"

- [ ] I seksjonen "Vis/Sjul" Aktiver "Vis Filtyper"

Du har nå aktivert visning av filtyper!





# Installasjon av GBDK og Bgb {.intro}

21. April slapp Nintendo konsollen "Gameboy" ut på markedet. Denne konsollen
var revolusjonerende, dette var den første bærbare konsollen, der du kunne
bytte spillet med å bytte kasseten.

Når man programmerer generelt, er det lurt å ha en arbeidsplass. Vi anbefaler
deg å ha alt av koding i en egen mappe.

Under, kan du lese om hvordan du setter opp arbeidsplassen din.



# Installering av GBDK {.activity}

__GBDK__ er en "__Compiler__". Compilerens jobb er å oversette koden din til et språk
som __prossesoren__ kan lese, og derreter gjøre ting.

## Windows {.check}

I tilleg til å installere __GBDK__ får du også en "__Bat__" -fil. Kjører du
denne filen vil den ta koden din (som ligger hovedsaklig i  filen__main.c__),
og gir den til GBDK. GBDK vil da ta koden din og oversette den. Etterpå vil den
legge oversatt kode i filen __game.gb__.

- [ ] Gå til [GBDK lastest release side på sourceforge-nettsiden](https://sourceforge.net/projects/gbdk/files/gbdk-win32/2.95-3/)

- [ ] Last ned gbdk-x.xx.x-win32.zip

[![](GBDK-Download.png)](https://sourceforge.net/projects/gbdk/files/gbdk-win32/2.95-3/)

- [ ] Pakk ut til en plass på datamarskinen (Husk hvor du legger den!)

- [ ] Last ned [ByggKode.bat](ByggKode.bat)

- [ ] Legg filen `ByggKode.bat` inn i bin-mappen, i GBDK-mappen.

Du har nå installert GBDK!

# Installering av Bgb {.activity}

Ved å bruke __GBDK__, får du kode som en ekte Gameboy kan lese. Men det er en liten
sjanse for at du har en Gameboy og et flashkort liggende. Derfor bruker vi __BGB__,
en __emulator__.

Dette programmet, later som om den er en ekte Gameboy, slik at du får
testet ut koden din. Programmet er også 100% lovlig.

## Windows {.check}

Vi gir deg også en annen "__bat__" fil her. Kjører du denne filen vil den ta koden
som ligger i __game.gb__ og gi den til __BGB__,

- [ ] Gå til [Bgb -hovednettsiden](http://bgb.bircd.org/)

- [ ] Trykk på [download below](http://bgb.bircd.org/#downloads)

[![](BGB-Download1.png)](http://bgb.bircd.org/#downloads)

- [ ] Last ned BGB x.x.x (zip, x kB)

[![](BGB-Download2.png)](http://bgb.bircd.org/bgb.zip)

- [ ] Åpne Zip -filen

- [ ] Kopier bgb.exe til bin -mappen, i gbdk -mappen din.

- [ ] Last ned [KjorKode.bat](KjorKode.bat)

- [ ] Flytt filen til bin -mappen også

Du har nå installert Bgb!
