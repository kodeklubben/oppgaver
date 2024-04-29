---
title: Draugaveiðin
level: 1
author: 'Þýtt frá [Code Club UK](//codeclub.org.uk)'
translator: 'Hera Gautadóttir'
language: is
---


# Inngangur {.intro}

Þetta verkefni er innblásið af leiknum __Whack-a-mole__, þar sem moldvörpur 
birtast upp úr holunum sínum og markmiðið er að ná að slá þær aftur ofan í. 
Í þessu spili verða draugar sem hverfa þegar smellt er á þá. Markmið leiksins 
er að ýta á sem flesta drauga á undir 30 sekúndum. 

![Illustrasjon av et ferdig spøkelsejakt spill](spokelsesjakten.png)


# Skref 1: Búðu til fljúgandi draug {.activity}

## Gátlisti {.check}

- [ ] Búðu til nýtt Scratch-verkefni.

- [ ] Eyddu katta teikningunni með því að hægrismella á hana og velja `eyða`

- [ ] Breyttu bakgrunninum í `Woods`.

- [ ] til að bæta við draug ýtir þú á 
  ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png)-takkann.
  Veldu `Ghost`-teikninguna.

- [ ] Nefndu drauginn `draugur1`.

Nú skalt þú  __búa til breytu__ sem stjórnar hversu hratt draugurinn hreyfir
sig. Við getum svo seinna notað þetta til að auka hraða draugsins eftir því 
sem líður á leiknum. 

- [ ] Undir `Kóði`{.blocklightgrey}, smelltu á `Breytur`{.blockdata} og svo
  `Smíða breytu`. Kallaðu breytuna `hraði`. Hakaðu við þar sem stendur
  `Aðeins fyrir þessa teikningu`.

- [ ] Á sviðinu ætti breytan að heita `draugur1: hraði`. Ef hún heitir 
  bara `hraði`, skaltu eyða henni og reyna aftur.

- [ ] Afhakaðu við hliðina á breytunni svo hún sjáist ekki 
- [ ] á skjánum: ![Bilde av hvordan ikke vise hastighet variabelen](hastighet.png)

- [ ] Við viljum að draugurinn hreyfist þegar leikurinn hefst. Við gerum það 
  með því að búa til þennan kóða:

  ```blocks
  þegar smellt er á @greenflag
  láttu [hraði v] verða [3]
  endalaust
      fara (hraði) skref
  end
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Svífur draugurinn yfir skjáinn?

- [ ] Af hverju er draugurinn fastur þegar hann lendir á kantinum?

## Gátlisti {.check}

- [ ] Til að koma í veg fyrir að draugurinn festist í kantinum þurfum við  
  að fá hann til að snúa við þegar hann lendir á kantinum. Þetta gerum við
  með `ef á kanti, snúðu við kubbinum`{.blockmotion}.
  Þá lítur kóðinn okkar svona út:

  ```blocks
  þegar smellt er á @greenflag
  láttu [hraði v] verða [3]
  endalaust
      fara (hraði) skref
      ef á kanti, snúðu við
  end
  ```

- [ ] Til að koma í veg fyrir að draugurinn fari á hvolf skulum við ýta á `Átt`
  kassann fyrir ofan teikninguna.
  Veldu snúninginn í miðjunni ("vinstri/hægri").

  ![venstre/høyre](../bilder/rotasjonsmate-hv.png)

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Flýgur draugurinn fram og aftur?

- [ ] Snýr draugurinn í rétta átt?

## Prófaðu! {.challenge}

- [ ] __Breyttu hraðabreytunni__, þannig að draugurinn fari hraðar eða
   hægar.

- [ ] Hvernig getum við fengið drauginn til að __fljúga hraðar því lengur 
  sem hann flýgur?__ (Þetta getur verið flókið svo ekki örvænta ef þig dettur 
  ekki í hug nein leið. Þú átt eftir að fá fleiri vísbendingar.)


# Skref 2: Fáum drauginn til að birtast og hverfa {.activity}

*Til að gera leikinn skemmtilegri viljum við að draugurinn birtist 
og hverfi.*

## Gátlisti {.check}

- [ ] Við búum til nýan kóða sem á að keyra á sama tíma og kóðinn sem
  hreyfir drauginn.Nýji kóðinn mun láta __drauginn birtast í ákveðinn 
  tíma__ og __fela drauginn í ákveðinn tíma__. DÞetta á að gerast aftur
  og aftur þangað til að leiknum er lokið. Svona gerir þú kóðann:

  ```blocks
  þegar smellt er á @greenflag
  endalaust
      birta
      bíða í (velja tölu á milli (3) og (5) af handahófi) sekúndur
      fela
      bíða í (velja tölu á milli (2) og (4) af handahófi) sekúndur
  end
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Flýgur draugurinn fram og tilbaka?

- [ ] Hverfur hann og birtist til skiptis endalaust?

## Prófaðu! {.challenge}

- [ ] Prófaðu að __breyta tölunum í kóðanum__ þar sem stendur `velja tölu á milli _
  og _ af handahófi`{.blockoperators}. Hvað gerist þegar þú velur mjög stórar
  eða litlar tölur? (Þetta gæti gefið þér nýja vísbendingu um það hvernig 
  við látum drauginn til að fara hraðar því lengur sem leikurinn er í gangi.)


# Steg 3:Látum drauginn hverfa með smelli! {.activity}

*Til að gera þetta almennilega þarf spilarinn að hafa eitthvað að 
 gera – til dæmis að ýta á drauginn. Þegar það gerist viljum við 
 líka að það komi skemmtilegt hljóð!*

## Gátlisti {.check}

- [ ] Smelltu á `Hljóð`{.blocklightgrey}-flipann, bættu við nýju hljóði
  með takkanum sem er niðri og til vinstri. Leitaðu að hljóðinu `Fairydust`
  í leitarstrengnum og bættu því við. Nú er hægt að bæta því við í kóða
  draugsins.Búðu til kóðann sem fær drauginn til að hverfa þegar
  smellt er á hann:

- [ ] Búðu til kóðann sem fær __drauginn til að hverfa__  þegar
  smellt er á hann:

  ```blocks
  þegar smellt er á þennan karakter
  fela
  spila hljóð [fairydust v]
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Hverfur draugurinn með hljóði þegar þú smellir á hann?

## Prófaðu! {.challenge}

- [ ] Spurðu einhvern fullorðinn hvort þú megir taka upp
  þitt eigið hljóð. Þú gætir notað hljóðið í staðinn fyrir `Fairydust`.


# Skref 4: Bættu við tíma og stigum {.activity}

*Við erum með draug sem hverfur á brott og nú viljum við fá stig 
 fyrir það! Við viljum einnig fá takmarkaðan tíma til að fá eins 
 mörg stig og við mögulega getum. Við getum leyst hvoru tveggja með 
 því að nota breytur.*

## Gátlisti {.check}

- [ ] Búðu til nýja breytu sem heitir `Stig`{.blockdata}. Breytan á
  að gilda `Fyrir allar teikningar`. Bættu við nýjum kubbi sem breytir 
  `Stig`{.blockdata}-breytunni um 1 í hvert skipti sem ýtt er á drauginn. 

  ```blocks
  þegar smellt er á þennan karakter
  fela
  spila hljóð [fairydust v]
  breyttu [Stig v] um (1)
  ```

- [ ] Smelltu á `Svið` og búðu til nýja breytu sem heitir `Tími`{.blockdata}. 
  Láttu breytuna sjálst á skjánum.

- [ ] Búðu til nýjan kóða sem setur `Tími`{.blockdata}-breytuna á
  __30__ og `Stig`{.blockdata}-breytuna á __0__ þegar smellt er á
  græna fánann.

- [ ] Notaðu `endurtaka þar til`{.blockcontrol}-kubb til að bíða í __1__
  sekúndu og svo minnka tímann um 1 sekúndu. Skipunin á að keyra
  þar til að tíminn er runninn út. Í lokin stoppar þú allan leikinn
  með `stöðva allt`{.blockcontrol}-kubb.

  ```blocks
  þegar smellt er á @greenflag
  láttu [Tími v] verða [30]
  láttu [Stig v] verða [0]
  endurtaka þar til <(Tími) = [0]>
      bíða (1) sekúndur
      breyttu [Tími v] um (-1)
  end
  stöðva [allt v] :: control
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

## Prófaðu! {.challenge}

- [ ] Hvernig getur þú fengið drauginn til að fara hraðar 
  eftir því sem tímanum líður?

## Vistaðu verkefnið {.save}

- [ ] __Vel gert!__ Leikurinn er tilbúinn en reyndu endilega 
  við næstu skref.


## Auka áskorun: Fleiri draugar! {.challenge}

*Ef einn draugur er skemmtilegur er líklegt að fleiri væri betra! 
Reynum nú að búa til þrjá drauga sem fljúga um!*

- [ ] __Búðu til fleiri drauga__ með því að hægri smella á þann
  sem þú hefur nú þegar og tvöfaldaðu hann.

- [ ] __Láttu draugana vera misstóra__. Þetta getur þú gert með
  því að velja draug og smella á `Stærð`-reitinn og breyta tölunni. 

- [ ] Einnig getur þú __breytt hraða drauganna__. Þetta getur þú gert 
  í `hraði`{.blockdata}-breytunni efst í kóða hvers draugs. 

- [ ] Í lokinn getur þú __dreift úr draugunum__ yfir sviðið. Þú gerir 
  það með því að ýta á draugana og draga þá um sviðið.

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Ertu með þrjá drauga sem fljúga fram og tilbaka?

- [ ] Hverfa draugarnir og birtast aftur?

- [ ] Hverfa þeir þegar þú ýtir á þá?

Til hamingju! Þú hefur náð að búa til leik!

## Prófaðu! {.challenge}

- [ ] Hversu margir draugar finnst þér virka best fyrir leikinn?
   __Bættu við fleirum__ og prófaðu!

- [ ] Nærðu að fá draugana til að __líta mismunandi út__? Smelltu á 
  `Búningar`{.blocklightgrey} og prófaðu þig áfram. Þú getur líka
  valið eitthvern af kubbunum undir `Útlit`{.blocklooks}.

- [ ] Getur þú látið draugana verða __mis mikils stiga virði?__ Hvað 
  með að láta minnsta og hraðasta drauginn verða 10 stiga virði?

## Vistaðu verkefnið {.save}

*Leikurinn er tilbúinn. Vel gert! Nú geturðu spilað!*

Ef þú forritaðir leikinn með Scratch-reikningnum þínum geturðu deilt honum með
öðrum þegar þú smellir á `Deila` efst á skjánum.
