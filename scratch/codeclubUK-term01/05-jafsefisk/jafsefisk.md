---
title: JafseFisk
level: 1.5
language: nb-NO
embeds: ["*.png", "../../bilder/*.png"]
...

#JafseFisk

#Introduksjon { .intro}
Vi skal nå lage et JafseFisk-spill! Målet i spillet er å hjelpe JafseFisk med å spise alle byttedyrene som svømmer rundt i havet.

![skjermbilde](jafsefisk.png)

# Steg 1: JafseFisk følger musepekeren { .activity}
__Først skal vi lage JafseFisk som svømmer rundt i havet!__

## Sjekkliste { .check}

+ __Start et nytt Scratch prosjekt__.
+ __Riktig bakgrunn__ får du ved å velge Scene og så Bakgrunn-fanen. Importer bakgrunnen __Natur/underwater3__ ved å velge `Velg en ferdig bakgrunn`{.blocklightgrey}. Slett så den andre bakgrunnen __backdrop1__.
+ Endre Sprite1's navn til `JafseFisk` ved å trykke på det blå '__i__' symbolet.
+ Gi figuren en haidrakt ved å velge `Velg drakt fra biblioteket`. Velg drakt __Dyr/shark-b.png__. Kall drakten `åpen munn`. Slett så figurens andre drakt (__costume1__ og __costume2__).
+ Klikk på det blå '__i__' symbolet igjen, og pass på at figuren bare kan bevege seg fra side til side ved å velge rotasjonsmåte `<-->`.
+ Få fisken til å følge musepekeren rundt i sjøen ved å lage dette skriptet:

```blocks
    når grønt flagg klikkes
    for alltid    	
        pek mot [musepeker v]
        gå (3) steg
```

## Test Prosjektet { .flag}

__Klikk det grønne flagget.__
Flytt musepekeren rundt i sjøen. Følger fisken med?
Hva skjer hvis du ikke flytter musepekeren, og fisken når den igjen?
Hvordan ser den ut? Hvorfor gjør den dette?

+ Du kan stoppe JafseFisks maniske flipping hvis du sørger for at den bare flytter seg når den ikke er for nær musepekeren
(`avstand til`{.blocklightblue} blokken ligger under `Sansning`{.blocklightgrey} paletten).

    ```blocks
    når grønt flagg klikkes
	for alltid
		hvis <(avstand til [musepeker v]) > (10)>
            pek mot [musepeker v]
            gå (3) steg
    ```

## Lagre prosjektet { .save}

## Ting å prøve { .try}

Hvis du vil kan du forandre tallene i skriptet, og se hvordan det forandrer bevegelsene:?
Sett avstandensgrensen til et stort tall (f.eks. 100), eller et lite tall (f.eks. 1).
Sett antall steg fisken flytter seg til et stort tall (f.eks. 20) eller et lite tall (f.eks. 1, eller 0).


# Steg 2: Legg til byttedyr { .activity}
__Det er på tide å gi JafseFisk noe å spise!__

## Sjekkliste { .check}

+ Lag en ny figur fra biblioteket ved å bruke **Dyr/Fish2**. 
+ Gjør figuren mindre med `krympeknappen`{.blocklightgrey} som ligger over den røde stopp-knappen.
+ Få byttedyrene til å bevege seg i tilfeldige retninger. Først skal vi la dem bevege seg litt framover, og så snu en tilfeldig valgt vinkel med eller mot klokka, og deretter gjenta. 

    ```blocks
    når grønt flagg klikkes
    for alltid		
		gå (2) steg
		vend til høyre (tilfeldig tall fra (-20) to (20)) grader
		sprett tilbake ved kanten  
    ```

## Test prosjektet { .flag}

__Klikk på det grønne flagget__ og se hvordan byttedyret svømmer rundt. Svømmer det slik du forventet? Ser bevegelsene naturlige ut?

__For øyeblikket samspiller ikke JafseFisk og byttedyret med hverandre. Det skal vi gjøre noe med i neste steg.__

## Lagre prosjektet { .save}

## Ting å prøve{ .try}

* Prøv å forandre tallene for steg og `tilfeldig tall`{.blockgreen}. Hvordan forandrer det byttedyrenes bevegelser?

* Hva gjør`sprett tilbake ved kanten`{.blockblue} blokken? Fjern blokken og se hva som skjer.

#Steg 3: JafseFisk spiser byttet { .activity}

__Nå skal vi la JafseFisk spise byttet!__ Når den har fanget byttet i munnen skal to ting skje:
* Den må lukke munnen og lage en gomlelyd.
* Byttet må forsvinne, og så komme igjen en liten stund senere.

## Sjekkliste { .check}

+ Vi starter med å la byttet forsvinne hvis den berører JafseFisk, og så komme tilbake etter 3 sekunder. Bruk `berører`{.blocklightblue}-blokken for å sjekke om byttet kommer borti JafseFisk.

    ```blocks
    når grønt flagg klikkes
    for alltid		
		gå (2) steg
		vend til høyre (tilfeldig tall fra (-20) to (20)) grader
		sprett tilbake ved kanten
		hvis <berører [JafseFisk v]?>
			skjul
			vent (3) sekunder
			vis
    ```

## Test prosjektet { .flag}
__Prøv spillet ditt igjen. Ser du noen problemer?__ ? Legg merke til at byttet forsvinner uansett hvor det berører JafseFisk. Dessuten kan fisken bare vente 3 sekunder og så spise byttet i samme øyeblikk som det dukker opp igjen, det er ikke særlig rettferdig!


+ Hvordan kan vi sikre at byttet bare forsvinner hvis det berører JafseFisks munn? Tja, vi kunne bruke `berører farge`{.blocklightblue} blokken og se om den berører fiskens tenner. For å gjøre dette, bytt ut `berører`{.blocklightblue} blokken med en `berører farge`{.blocklightblue} blokk i skriptet ditt, klikk på fargen i blokken og klikk så på fiskens tenner. 
+ Nå kan vi la byttet flytte seg til et tilfeldig punkt på skjermen før den dukker opp igjen ved å bruke en `gå til`{.blockblue} blokk, og gi den en tilfeldig verdig for __x__ og __y__.

    ```blocks
    når grønt flagg klikkes
    for alltid
		gå (2) steg
		vend til høyre (tilfeldig tall fra (-20) to (20)) grader
		sprett tilbake ved kanten
		hvis <berører fargen [#FFFFFF]?>
			skjul
			vent (3) sekunder
			gå til x:(tilfeldig tall fra (-200) til (220)) y: (tilfeldig tall fra (-170) til 170))
			vis
    ```
    
## Test prosjektet { .flag}

Prøv spillet igjen. Forsvinner byttet bare når det berører fiskens tenner? Og kommer det igjen i et tilfeldig punkt på skjermen – altså ikke samme sted som det ble spist?

+ JafseFisk må vite når den har spist noe slik at den kan gi fra seg en lyd og bytte drakt. For å gjøre dette kan vi la byttet `send melding`{.blockyellow} om at det er spist, før det forsvinner.

    ```blocks
	når grønt flagg klikkes
    for alltid
		gå (2) steg
		vend til høyre (tilfeldig tall fra (-20) to (20)) grader
		sprett tilbake ved kanten
		hvis <berører fargen [#FFFFFF]?>
			send melding [Du tok meg!]
			skjul
			vent (3) sekunder
			gå til x:(tilfeldig tall fra (-200) til (220)) y: (tilfeldig tall fra (-170) til 170))
			vis
    ```
    __Nå vil vi at fiskens respons på denne meldingen er å lage en gomlelyd og klikke med kjevene.__

+ Legg til drakten __Dyr/shark-a__ og lyden  __Effekter/bubbles__ til JafseFisk. Kall drakten `lukket munn`.
+ Legg så til et nytt skript til JafseFisk slik at han kan svare på meldingen `send melding`{.blockyellow} fra byttedyret. Dette skriptet gjør at fisken spiller av boblelyden og `bytter drakt til`{.blockpurple} of lukket-munn drakten, venter litt og så bytter tilbake.

    ```blocks
    når jeg mottar [Du tok meg! v]
    spill lyden [bubbles v]
    gjenta (2) ganger
		bytt drakt til [lukket munn v]
		vent (0.5) sekunder
		bytt drakt til [åpen munn v]
    ```

__Nå er JafseFisk klar til å spise, så la oss fylle havet med byttedyr. Høyreklikk på byttefiguren og velg `lag kopi` til du føler du har fått nok fisk.__

## Test prosjektet { .flag}
Klikk på det grønne flagget. Spiser JafseFisk byttet? Spiser den alle byttedyrene?

## Lagre prosjektet { .save}

## Noe å tenke på
Hvorfor må vi legge til en `vis`{.blockblue} blokk på starten av byttedyrets skript? Tenk på hva som ville skje om byttet blir spist og spillet stoppes før det dukker opp igjen. Og hva ville skje om spillet ble startet igjen?


__Godt gjort! Du har igrunn fullført spillet! Men fins flere muligheter for utvidelse av spillet. Er du klar for en utfordring?__


## Utfordring 1: Forandre bevegelsene til byttedyrene { .challenge}

For øyeblikket beveger alle byttedyrene seg likt. __Kan du få ett av dem til å bevegeseg annerledes?__ 
__Hint:__ Ikke bruke for lang tid på denne oppgaven uten å se på de andre aktivitene i dette prosjektet.

__Velg deg ut et byttedyr å eksperimentere med.__ Hvis de har samme drakt, bytt farge me `sett farge effekt`{.blockpurple} blokken. Slik kan du se forskjell fra resten av byttedyrene. Prøv nå å få dette byttedyret til å bevege seg saktere enn de andre.

Få byttedyret til å bevege seg saktere enn de andre. __Hint:__ Se på blokken `gå (2) steg`{.blockblue}.


## Test prosjektet{ .flag}
Beveger byttet seg saktere? Gjør dette spillet bedre?
Hvis du klarte dette, __, prøv å gjøre et av byttedyrene kjappere enn de andre.__


Beveger byttedyrene seg på en fornuftig måte?  Gjør disse forandringene spillet bedre?
__Hint:__ Hvis byttet ditt svømmer rundt i sirkler, sjekk verdiene i `tilfeldig tall`{.blockgreen} blokken i `vend`{.blockblue} blokken.

Hva om du lar alle byttedyrene bevege seg forskjellig, ved å bruke forskjellige kombinasjoner av disse bevegelsene?

Gjør noen av disse forandringene spillet bedre? Gjør de spillet med interessant, morsommere, vanskeligere eller lettere? Er noe av dette bedre, syns du?

## Lagre prosjektet { .save}

## Utfordring 2: Hjelp byttet å unngå JafseFisk { .challenge}

Byttedyrene i dette spillet er skikkelig dumme! De svømmer bare tilfeldig rundt til de blir spist. Ekte fisk svømmer vekk fra rovfisker. Nå vil vi __la ett av byttedyrene svømme vekk fra JafseFisk.__

Det fins ingen blokk i Scratch som kan gi oss retningen til en annen figur. Men du kan få en figur til å snu seg i retningen av en annen, og deretter la den snu seg i motsatt retning. Blokkene du trenger er i `Bevegelse`{.blocklightgrey} paletten.

Prøv nå å hjelpe et av byttedyrene med å __snu seg vekk fra JafseFisk__. Du vil kanskje også la den virre mens den svømmer bort?
Du vil kanskje oppdage at byttet setter seg fast i et hjørne? Du  ønsker kanskje at byttet bare ønsker å flykte dersom JafseFisk kommer for nære?
__Hint:__ Se tilbake på hvordan vi brukte `avstand til`{.blocklightblue} blokken tidligere i spillet. 

## Test prosjektet { .flag}
Gjør dette at fisken er vanskeligere å ta? Gjør det spillet bedre?

## Lagre prosjektet{ .save}

## Utfordring 3: Legg til poeng { .challenge}
Det er ikke nok bare å spise fisk. Hvordan vet du at du er en bedre spiller enn vennene dine? __Du må kunne samle poeng, så la oss legge til en poengtavle.__ Se på __Keep Score scratch card__ for å få noen hint om hvordan det kan gjøres. 
Pass på at poengene går tilbake til null ved begynnelsen av spillet. Hvor skal du legge inn denne blokken?

## Test prosjektet { .flag}
Går poengsummen tilbake til null når spillet starter? Går den opp hver gang du spiser byttedyr?

## Lagre prosjektet { .save}

## Utfordring 4: Legg til en nedtelling { .challenge}

__Gi deg selv en tidsfrist.__ Hvor mange fisk kan du spise på 30 sekunder?

Se på __Timer scratch card__  for å se hvordan man legger til en tidtaker til et spill. Begynn med 30 sekunders-spill.

## Test prosjektet { .flag}
Begynner tidtakeren på 30?
Teller den ned med rett hastighet? 
Kan du fange fisk mens tiden telles ned? Stopper spillet når telleren når null?

## Lagre prosjektet { .save}

## Utfordring 5: Legg til bonuspoeng { .challenge}
Legg til en belønning med høy bonus poeng om du kan spise alle tre fiskene samtidig. Hvordan kan du vite hvor mange som er spist?

__Hint:__ En måte å gjøre dette på er å bruke en variabel for å __telle hvor mange byttedyr som svømmer i havet.__

## Lagre prosjektet { .save}

## Utfordring 6: Forandre spillet: Hold byttedyrene i live! { .challenge}
Av og til kan man få glimrende nye idèer ved å gjøre det motsatte av det man allerede har gjort.

__Endre spillet slik at du isteden kontrollerer et byttedyr i et hav av mange JafseFisk.__ Hvor lenge kan du holde det gående før du blir spist? Istedet for å bruke poeng, hva med å  gi byttedyret 3 liv og avslutte spillet når de er brukt opp?

## Lagre prosjektet { .save}

__Godt gjort, du er ferdig! Nå kan du nyte spillet ditt!__
Ikke glem at du kan dele spillet med alle vennene og familien din ved å klikke på __Legg ut__ i topp-menyen!

