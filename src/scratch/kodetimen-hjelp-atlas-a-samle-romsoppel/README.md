---
title: 'Kodetimen - Hjelp Atlas å samle romsøppel! '
author: marikisfoss
language: nb
---
**Introduksjon**

Dette er en oppgave for elevene som har kodet en del tidligere, og vil derfor være mer utfordrende. Det er ikke nødvendigvis fordi kodingen er vanskelig, men fordi elevene ikke vil få så mange direkte instruksjoner om hva de skal gjøre. 

Vi har laget en oppgave som er delt ut fra hvilke elementer som må programmeres: Romskipet, meteorregnet, romsøppelet, Game Over, og poeng og liv telleren. 

De får instruksjoner om hva de ulike figurene skal gjøre, når det skal skje, og hvordan det skal se ut. De må selv finne de riktige klossene og tenke seg til hvordan dette skal gjøres. Vi har inkludert en fasit som du som lærer kan basere din hjelp på, og ha i bakhånd dersom noen av elevene syns det er vanskelig. 

![Bildebeskrivelse](./atlas-spill.png)
# Introduksjon {.intro}
  
Hei, jeg heter Atlas og jeg forbereder meg til et veldig viktig rom-oppdrag! Jeg har fått den store oppgaven om å samle sammen og rydde romsøppelet vekk fra romstasjonen. Det som gjør oppdraget så vanskelig er at det er meldt at en meteorstorm er på vei, som kan føre til store problemer med oppdraget. 
Jeg trenger nå deres hjelp! Kan dere lage en simulering på hvordan jeg kan løse oppdraget? 


I denne oppgaven skal dere lage en simulering av romoppdraget til Atlas i Scratch. Gjennom lenken får dere bakgrunnen og figurene dere trenger til å lage simuleringen. Vi har laget en beskrivelse av hva de ulike figurene skal gjøre, og dere må sette sammen de riktige kodene til å matche instruksjonene. 

Dette er en oppgave for dere som har kodet mye før. Det innebærer at oppgaven inneholder instruksjoner om hva de ulike figurene skal gjøre, men ikke fasit på hvordan kodene ser ut. 

## Oppgaven passer til: {.check}

 **Fag**: Matematikk, Programmering, Teknologi

**Anbefalte trinn**: 8. - 10. klasse 1 VGS, 2 VGS, 3 VGS 

**Tema**: Animasjon, Blokkbasert, Lyd, Spill

**Tidsbruk**: 1 - 2 timer

## Kompetansemål {.challenge}

Relevante kompetansemål:


**4. trinn:**

Matte:
lage algoritmer og uttrykke de ved bruk av variabler, vilkår og løkker

**7. trinn:**


Naturfag:
utforske, lage og programmere teknologiske systemer som består av deler som virker sammen
skille mellom observasjoner og slutninger, organisere data, bruke årsak-virkning-argumenter, trekke slutninger, vurdere feilkilder og presentere funn


K&H:
bruke ulike strategier for idéutvikling og problemløsing
bruke programmering til å skape interaktivitet og visuelle uttrykk

**5. trinn**

Matte:
lage og programmere algoritmer med bruk av variabler, vilkår og løkker 


**10. trinn:**



Matte:
utforske hvordan algoritmer kan skapes, testes og forbedres ved hjelp av programmering (8. trinn)


## Forslag til læringsmål {.challenge}

Læringsmålene dekker kompetansemål innen kunst og håndverk og matematikk:

Lage et produkt basert på en bestilling

Bruke blant annet hendelser, løkker, variabler, operatorer og funksjoner for å lage algoritmene i spillet
Teste og feilsøke kode

Reflektere over konsekvensene ved romsøppel, og presentere egne løsninger til hvordan forsøpling av verdensrommet kan unngås



## Forslag til vurderingskriterier {.challenge}

Det er mange ulike måter man kan vurdere et programmeringsprosjekt, og her må en
selv vurdere hva som er den beste måten ut ifra hvilket fag man jobber i,
hvilken aldergruppe og hviklet nivå elevene er på, hva man ønsker å teste og
hvor mye tid man har til rådighet til å jobbe med prosjektet. I vårt
[lærerdokument](https://github.com/kodeklubben/oppgaver/wiki/Hvordan-undervise-i-og-vurdere-programmering){target=_blank} har vi blant
annet beskrevet ulike måter dette kan gjøres på, tillegg til en del andre
nyttige tips til hvordan man underviser i programmering.


#  Hva skal dere gjennom i oppgaven? {.activity}

Kort oversikt over kodekategoriene og begrepene dere skal innom:

Bevegelse

Hendelser

Variabler

Styring

Operatorer

Klone figurer

Sansing

Hvis - så 



# Steg 1: Åpne prosjektet og programmer romskipet {.activity}

**Her finner du prosjektet du skal åpne:**
[https://scratch.mit.edu/projects/915491222](https://scratch.mit.edu/projects/915491222)

- [ ] Romskipet skal styres med alle de fire piltastene. 
- [ ] Vær obs på at alt som er ute i verdensrommet beveger seg sakte - dette må dere ta med i beregningen for hvordan romskipet skal bevege seg. 
- [ ] Dere skal også legge til en liv-teller. Denne skal starte på 3 liv. 

- [ ] Utfordring: Kan dere legge til noe i koden som gjør at romskipet endrer retning mens du kjører til høyre og venstre? 
## Test prosjektet {.flag}

**Klikk på det grønne flagget.** / **Start prosjektet for å teste koden så
langt.**

- [ ] Etter dette steget skal du kunne flytte på romskipet med fire piltaster.  Du skal også se en liv-teller oppe til venstre.

**Fasit:**
```blocks
når grønt flagg klikkes
sett [liv v] til (3) 
gjenta for alltid
hvis <tast (pil opp v ) trykket>? 
endre y med (2.5) 
end
hvis <tast (pil ned v) trykket>? 
endre y med (2.5) 
end
hvis <tast (pil høyre v) trykket>? 
endre y med (2.5) 
end
hvis <tast (pil venstre v) trykket>? 
endre y med (2.5) 
end
```


# Steg 2: Programmer romsøppel {.activity} 
- [ ] Romsøppelet skal dukke opp en etter en, litt etter litt, og dukker ikke opp før om noen sekunder etter spillet starter. Her skal du bruke klone-funksjonen så du slipper å lage mange kopier av romsøppelet. 
- [ ] Det skal dukke opp totalt 20 romsøppel-kloner.
- [ ] Siden romsøppelet flyter i verdensrommet skal det være tilfeldig hvor romsøppelet kommer fra og hvor de flyter til, men husk å definere at søppelet ikke skal flyte utenfor skjermen vår. 
- [ ] Hver gang romskipet kjører på romsøppel for å plukke det opp, får dere ett poeng og romsøppelet dere treffer skal bli borte. 

**Tips: Her trenger dere tre algoritmer:**

- [ ] en som skjuler den originale romsøppel-figuren, setter i gang poengteller og oppretter kloner
- [ ] en som styrer hva som skjer når klonene starter
- [ ] en som styrer hva som skjer når romskipet berører romsøppelet

## Test prosjektet {.flag}
**Klikk på det grønne flagget.** / **Start prosjektet for å teste koden så
langt.**

- [ ] Etter dette steget skal det dukke opp 20 romsøppel-kloner som dukker opp ved jevne mellomrom, fra tilfeldige steder. 
- [ ] Når romskipet berører romsøppelet skal de bli borte og poengtelleren skal telle oppover. 

**Fasit:**
```blocks
Når jeg starter som klon
sett y til (tilfeldig tall fra (-180) til (180)
sett x til (tilfeldig tall fra (-180) til (180)
vis
sett størrelse til (20)%
Gjenta til <berører (romskip v)>
Gli (6) sekunder til x: (tilfeldig tall fra (-180) til (180)) y:(tilfeldig tall fra (-180) til (180))
skjul
```
```blocks
Når grønt flagg klikkes
sett [poeng v] til (0)
skjul
vent (3) sekunder
gjenta (20) ganger
vent (5) sekunder
gjenta (1) ganger
lag klon av (meg v)
```
```blocks
Når jeg starter som klon
gjenta for alltid
hvis <berører (romskip v)>
endre [poeng v] med (1)
skjul
```

# Steg 2: Programmer meteorregnet {.activity} 

- [ ] Meteorregnet skal jevnt skli fra bunnen av skjermen og opp. 
- [ ] Meteorene skal starte utenfor skjermen nede, og forsvinne når de går utenfor skjermen oppe. 
- [ ] De skal dukke opp en og en, på ulike steder. Dere skal bruke klone-funksjonen for å slippe å lage mange kopier av figuren. 
- [ ] Når en meteor treffer romskipet, mister du et av de tre livene dine.
Meteorene skal fortsette å fly, frem til du har mistet alle de tre livene dine. 
- [ ] Da skal det meldingen GAME OVER sendes. 
 Når GAME OVER-meldingen er sendt skal alle figurene stoppes. 

**Tips: Her trenger dere tre algoritmer:**
- [ ] En som skjuler den originale meteor-figuren, og lager kloner som dukker opp ved jevne mellomrom. 
- [ ] En som forteller hvilken retning meteorittene flyr til, og hvor langt de skal fly før de blir skjult.
- [ ] En som forteller hvor lenge meteorregnet skal vare: frem til romskipet har blitt truffet tre ganger og liv-telleren er lik null. 
- [ ] Den skal også slette meteoren romskipet skal krasje med, sende GAME OVER-melding og stoppe alle figurene. 
## Test prosjektet {.flag}
**Klikk på det grønne flagget.** / **Start prosjektet for å teste koden så
langt.**
- [ ] Etter dette steget skal det dukke opp uendelig mange meteoritter fra bunnen av skjermen ved jevne mellomrom. 
- [ ] Dersom romskipet krasjer med meteorregnet skal du miste ett liv. 

**Fasit:**

```blocks
Når grønt flagg klikkes
skjul
gjenta for alltid
vent (3) sekunder
gjenta (1) ganger
lag klon av (meg v)
end
vent (1) sekunder
gjenta (1) ganger
lag klon av (meg v)
```
```blocks
når jeg starter som klon
vis
gå til x: (tilfeldig tall fra (-200) til (200)) y: (-200)
gjenta til <(y-posisjon)>(180)>
endre y med (2)
end
skjul
```
```blocks
når jeg starter som klon
gjenta til <[liv v]=(0)>
hvis <berører (Romskip v)?>
endre [liv v] med (-1)
slett denne klonen
end
end
send melding (GAME OVER)
stopp (alle)
```

# Steg 3: Programmer GAME OVER-bildet {.activity} 
- [ ] Sørg for at denne figuren ikke dukker opp før etter du har mistet alle livene dine. 

**Tips: Her trenger dere to algoritmer:**
- [ ] En som skjuler figuren
- [ ] En som får figuren til å dukke opp når du mottar meldingen GAME OVER. 


## Test prosjektet {.flag}

**Klikk på det grønne flagget.** / **Start prosjektet for å teste koden så
langt.**

- [ ] Dersom du mister alle livene dine skal det dukke opp en GAME OVER-beskjed på skjermen. 

**Fasit:**
```blocks
når jeg mottar (GAME OVER)
vis
```
```blocks
Når grønt flagg klikkes
skjul
```

## Lagre spillet {.save}


Husk å lagre spillet/programmet ditt. Når du er ferdig kan du klikke på "Legg
ut"-knappen. Da vil det bli lagt ut på Scratch-hjemmesiden din slik at du enkelt
kan dele det med familien og vennene dine.
