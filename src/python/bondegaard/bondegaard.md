---
title: Bondegården
level: 4
author: Vegard Bjerkli Bugge
---

# Introduksjon til ordlister i Python {.intro}

I denne oppgaven skal vi se nærmere på ordister, eller **dictionaries**, som de kalles på engelsk.
Ordlister kjennetegnes ved at hvert element er et par av to stykker data, kalt *ting* (**items** på engelsk). Ordlista kan inneholde mange forskjellige ting. Hvert element i en ordliste ser slik ut:

```python
min_ordliste = {'nøkkel': 'verdi'}
```

Det som står på venstre side av kolonet kalles for nøkkelen. En nøkkel som finnes i ordlista har en assosiert verdi vi får tak ved å "slå opp" i ordlista på den nøkkelen.
En nøkkel i ordlista kan være for eksempel tekst eller tall. Når nøkkelen først er lagret i ordlista er det viktig at den ikke endres. På høyre side av kolonet står verdien nøkkelen peker på når vi slår opp på den.
Verdien man finner i ordlistens "oppslagsord", kan være både heltall, desimaltall, strenger, lister, Sant (`True`) eller Usant (`False`). Hvert oppslagsord kan også være en variabel som peker på en immutabel verdi.

Ordlister er kjekke å ha. Vi bruker ordlister når vi vil kategorisere ting eller navn eller strenger eller tall eller variabler eller hva det måtte være.
For å finne ut verdien en spesifikk nøkkel *key* assossieres med i ordlista *dict*, "slår vi opp på ordet" ved å skrive

```python
dict.get(key)
# eller
dict[key]
```

Hvis vi vil lage en ordliste i Python, skriver vi først navnet på variabelen som skal peke på ordlista vi oppretter.
Så skriver vi er lik ( `=` ), og deretter en høyrevendt krøllparantes ( `{` ) for å markere starten av ordlista. Så skriver vi inn alle nøklene sammen med de assosierte verdiene.
Hvert par av nøkkel og verdi adskilles med et komma. Når vi er ferdige med å definere alle nøklene og oppslagsverdiene må vi huske på å skrive en venstrevendt krøllparantes ( `}` ) for å markere at ordlista er ferdig.

# Oppgave {.activity}

Budeie-Barbi og Bottolf Bonde driver en bondegård på Hofstad i Roan kommune. Til tross for at de har drevet gård helt siden de flyttet hit fra Trondheim i 1997 har de ENNÅ ikke bestemt seg for om de vil drive sauedrift eller melkeproduksjon, så de holder både kyr, sauer, og til og med et par griser i en og samme store innhegning. Det lokale bondelaget har sett seg lei av denne dårlige måten å holde husdyr på, og har derfor forlanget av Bottolf og Budeie-Barbi at de skiller dyra sine inn i forskjellige innhegninger, og for å gjøre vondt verre krever de at alle kyr og sauer skal skilles inn i totalt seks forskjellige innhegninger, to for hanndyra (vær og okser), to for hodyra (kyr og søyer) og to for barna (kalver og lam). De har ikke sagt om å skille mellom kjønna på grisene, men så er det ingen i bondelaget som vet at Bonde - paret holder griser også, så grisene kan være igjen i den store innhegningen. Kan du hjelpe Bottolf og Budeie-Barbi med å sortere ut sauene og krøttera?

I denne oppgaven får du oppgitt en ordliste (på engelsk "dictionary") med alle dyra til bøndene. Ordlista heter for -innhegning-, og finnes i ei fil som du kan laste ned [her](./bondegaard.py). Lagre den der du pleier å lagre Python-koden din. I denne ordlista kan man gjøre oppslag på dyrets navn, som er en streng. Som verdi angis hva slags dyr det er, som også er en streng. Samtlige navn i ordlista er unike. Når du lager en ordliste i Python 3 vil Python til enhver tid sørge for at alle nøklene (variabler eller strenger du slår opp på i ordlista) har unike navn, for å unngå forvirring. I den importerte ordlista ser hvert enkelt element slik ut:

```python
{ "navn" : "dyretype" }
```

Du skal skrive en funksjon som tar inn en streng som sier hvilket dyr vi skal telle opp. Funksjonen skal ta inn enten "Ku", "Okse", "Kalv", "Søye", "Vær", eller "Lam". Skriv der vi har kommentert #SKRIV KODE HER. Ikke endre på kode som omkranses av kommentaren # IKKE ENDRE PÅ DENNE KODEN.

```python
# IKKE ENDRE PÅ DENNE KODEN 
innhegning = { "Shaun" : "Lam", "Toralf" : "Kalv", "Oskar" : "Vær", "Stella" : "Søye",
               "Bobo" : "Lam", "Per" : "Søye", "Baba" : "Vær", "Kjell" : "Okse",
               "Staur" : "Okse", "Sune" : "Lam", "Rune" : "Lam", "Tune" : "Lam",
               "Scar" : "Søye", "Petra" : "Søye", "Litago" : "Ku", "Kakao" : "Ku",
               "Dauingen" : "Gris", "Gris" : "Gris", "Frøya" : "Søye", "Egon" : "Vær",
               "Kevin" : "Vær", "Tora" : "Søye", "Ralf" : "Kalv", "Enga" : "Ku", "Kjell" : "Vær",
               "Kjell" : "Gris", "Benedikte" : "Ku", "Agnethe" : "Søye", "Grisskjit" : "Søye",
               "Bjarne" : "Søye", "Hoppsideisi" : "Søye", "Koskos" : "Lam", "Boms" : "Lam",
               "Mulle" : "Lam", "Queen of England" : "Søye", "Dronningen av Sverige" : "Søye",
               "Rosenborg" : "Søye", "Lyn" : "Kalv", "Stråmann" : "Vær", "Blåmann" : "Okse",
               "Grynte" : "Gris", "Pål" : "Kalv", "Askguri" : "Ku", "Hansen" : "Lam", "Du" : "Søye",
               "Bente" : "Søye", "Marit" : "Søye", "Martin" : "Lam", "Pelle" : "Lam", "Anita" : "Lam",
               "Bernt" : "Vær", "Jompa" : "Lam", "Grislam" : "Lam", "Ku" : "Vær", "OK" : "Søye", "ArveLarve" : "Lam",
               "Sigurd" : "Lam", "Janne" : "Søye", "Nikita" : "Søye", "Saul" : "Søye", "Bonde" : "Søye",
               "Thor" : "Vær", "FandenIhelsike" : "Okse", "Mathis" : "Kalv", "Kalle" : "Kalv", "VonKarme" : "Søye",
               "Vegard" : "Okse", "Sindre" : "Lam", "Toffe" : "Søye", "Dennis" : "Søye", "Prebz" : "Vær",
               "Theodore" : "Ku", "Turbine" : "Søye", "Guri" : "Søye", "Karl" : "Ku", "Karianne" : "Lam", "Grisveitj" : "Søye",
               "Grismainn" : "Okse", "Gress" : "Søye", "Esben" : "Lam", "Prut" : "Søye", "Kola" : "Søye", "Peter" : "Søye", "Lom" : "Vær" }
# IKKE ENDRE PÅ DENNE KODEN

def dyretelling(dyr):
    antall_dyr = 0
    #SKRIV KODE HER
    return antall_dyr

# IKKE ENDRE PÅ DENNE KODEN
def main():
    dyreliste = [ "Ku", "Okse", "Kalv", "Søye", "Vær", "Lam" ]
    dyr = input("Skriv inn hvilket dyr som skal telles opp: ")
    while dyr not in dyreliste:
        print("Ugyldig dyr.")
            dyr = input("Skriv inn hvilket dyr som skal telles opp: ")
        print(dyretelling(dyr))
# IKKE ENDRE PÅ DENNE KODEN

main() # IKKE ENDRE PÅ DENNE KODEN
```
