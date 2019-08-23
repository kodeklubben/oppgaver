---
title: Vítaspyrna
level: 1
author: Erik Kalstad og Geir Arne Hjelle
translator: Stein Olav Romslo
language: is
---


# Kynning {.intro}

Við munum gera einfaldan fótboltaleik, þar sem þú verður að reyna að skora eins
mörg vítaspyrnu og hægt er.

![Mynd af lokuðum vítaspyrnuleiki](straffespark.png)


# Skref 1: Kötturinn og fótboltavöllurinn {.activity}

*Við byrjum með því að búa til kött sem getur hreyft sig á fótboltavelli.*

## Gátlisti {.check}

- [ ] Byrjaðu nýtt verkefni, til dæmis með því að smella á `Smiða` efst á
  síðunni. Ef þú hefur þegar hafið verkefni geturðu byrjað nýja með því að velja
  `Skrá` og síðan `Ný`.

- [ ] Smelltu á köttinn, og kallaðu köttinn `Leo`.

- [ ] Smelltu á ![Velja nýan bakgrunn](../bilder/velg-bakgrunn.png) nedst til
  hægri á skjánum til að sækja nýan bakgrunn. Veldu til dæmis bakgrunninn
  `Soccer 2` til þess að fá fótboltavöll með mark.

- [ ] Nú skulum við skrifa örforrit sem færir köttinn `Leo` þegar við smellum á
  hann. Smelltu á `Leo` í myndglugganum neðst á skjánum til þess að kóða hvað
  hann á að gera. Settu saman eftirfarandi kubba í kóðunarglugganum til
  vinstri:

  ```blocks
  þegar smellt er á þennan karakter
  fara (10) skref
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Fer `Leo` áfram þegar þú smellir á hann?

- [ ] Hvað gerist ef þú smellir á `Leo` mörgum sinnum þannig að hann fer til
  jaðar svæðisins?

## Gátlisti {.check}

- [ ] þú getur flutt `Leo` aftur á skjánum með því að smella á hann og draga
  hann hvar sem þú vilt.

- [ ] Við munum enn forrita auðveldara leið til að fá `Leo` aftur á völlinn.
  Búðu til nýtt atburðarit við hliðina á því sem þú hefur þegar búið til, sem
  lítur svona út:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (-90) og y: (-60)
  ```

- [ ] Nú mun `Leo` koma aftur á völlinn í hvert skipti sem þú smellir á grænan
  fánann.

## Vista verkefnið {.save}

Þú hefur nú skrifað lítið forrit! Scratch vistar allt sem þú gerir reglulega.
Það er engu að síður góð venja að geyma jafnvel á milli.

- [ ] Yfir senunni er textareit þar sem þú getur gefið nafn á leiknum þínum. Til
  dæmis máttu kalla hann `Vitispyrna`.

- [ ] Í valmyndinni `Skrá` er hægt að velja `Vista núna` til að vista verkefnið.


# Skref 2: Leo sparkar boltann {.activity}

*Það nesta sem við þurfum í leik okkar er bolti!*

## Gátlisti {.check}

- [ ] Við munum nú bæta við bolta í leik okkar. Smelltu á ![Veldu mynd úr
  safni](../bilder/hent-fra-bibliotek.png) og veldu fótboltann `Sports/Soccer
  Ball`.

- [ ] Kallaðu boltinn `Bolti`.

- [ ] Gerðu boltann minni með því að ýta fyrst á `Stærð` reitinn og breyta
  númerinu frá 100 til 60.

- [ ] Við munum nú skrifa örlítið lengri atburðarit fyrir boltann. Í þessu
  atburðariti settum við fyrst boltann fyrir framan köttinn. Eftir að boltinn
  snertir `Leo` (þ.e. `Leo` sparkar boltann) byrjar boltinn að hreyfa sig. Sjáðu
  hvort þú þekkir hvar í atburðaritinu mismunandi hlutir eru gerðar:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (0) og y: (-80)
  bíða þangað til <snertir [Leo v] ?>
  endalaust
    fara (6) skref
  end
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Sparkar `Leo` boltanum þegar þú smellir á hann?

- [ ] Get `Leo` sparkað boltanum aftur ef þú smellur á græna fánann aftur?

- [ ] Ef `Leo` snertir á boltann áður en þú smellir á hann (þegar þú smellir á
  græna fánann) þarftu að breyta tölunum í `fara til x: () og y:
  ()`{.b}-kubbanum þannig að boltinn er í hvild fyrir framan `Leo`.

- [ ] Stundum fer boltinn aftur *áður en* `Leo` snýr aftur til hans, þannig að
  hann snertir boltann aftur og byrjar að hreyfa sig. Þá hjálpar það að bæta við
  einu `bíða í (1) sekúndur`{.b}-kubba fyrir `bíða þangað til <snertir [Leo
  v]?>`{.b}-kubbann.


# Skref 3: Við þurfum markvörður! {.activity}

*Við munum nú gera leikinn svolitið erfiðara með því að forrita markvörð.*

## Gátlisti {.check}

- [ ] Bæta við fígúru sem getur verið markvörður. Við höfum notað smokkfiskinn
  `Animals/Octopus`, en þú getur líka notað önnur fígúru ef þú vilt.

- [ ] Settu fíguruna inn í markið. Ef nauðsýnlegt er hægt að snúa fígúruna með
  því að smella á `Búningar` og síðan á táknið til hægri fyrir eyða-takkann.

- [ ] Gefðu fígúruna nafnið `Markvörður`.

- [ ] Gerðu eftirfarandi atburðarit fyrir markvörðinn:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (200) og y: (-50)
  stefna í (0 v) gráður
  endalaust
    fara (15) skref
    ef á kanti snúðu við
  end
  ```

  Það eru nokkrar nýir kubbar í þessu atburðariti. Lestu forritið vandlega.
  Hvað heldurðu nýir kubbarnir gera?

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Byrjar markvörðurinn í markinu?

- [ ] Fer `Markvörður` til hægri og vinstri á skjánum?

## Gátlisti {.check}

- [ ] Þér finnst kannski að markvörðurinn sé svolitið stór? Þú getur breytt
  stærð hans eins og við gerðum áður. Önnur leið til að breyta stærð er með því
  að nota kubba úr flipanum `Útlit`{.blocklooks}.

  Settu inn kubbann `stærð verður (100)%`{.b} í
  `endalaust`{.blockcontrol}-slaufuna. Þú getur prófað að breyta `100%` í önnur
  tölu þar til þú funnir viðaigandi stærð fyrir markvörðinn. Ef þú notar
  smokkfiskinn sem `Markvörður` passar `50%` nokkuð vel. Prófaðu það!

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Hvað gerist þegar `Leo` skýtur á markið? Getur markvörðurinn verjað
  markið?


# Skref 4: Markvörðurinn ver! {.activity}

*Nú er kominn tími fyrir markvörðinn til að verja markið!*

Við munum nú gera nokkrar *prófanir* sem segja okkur þegar markvörðurinn stöðvar
boltann eða þegar boltinn fer í mark.

## Gátlisti {.check}

- [ ] Við byrjum að finna út þegar markvörðurinn stoppar boltann. Smelltu á
  `Bolti`. Bættu við eina `ef annars`{.blockcontrol}-kubba í atburðaritið:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (0) og y: (-50)
  bíða þangað til <snertir [Leo v] ?
  endalaust
  fara (6) skref
    ef <snertir [Markvörður v] ?> þá
      senda [Varið v]
    end
  end
  ```

  Í kubbanum `senda [message1 v]`{.b} verður þú að velja `Ný skilaboð` og síðan
  skrifa `Varið` sem skilaboð.

  Skílaboð eru skilaboð sem fígúrurnar í leiknum geta sent á milli sinna án þess
  að þú sérð það í raun. Þetta gerir það audvelt fyrir margar fígurur að
  bregðast við því sem gerist.

- [ ] Nú viljum við að bæði boltann og markvörðurinn hætta að hreyfa sig ef
  boltinn verður stoppað. Bættu þessu við sem nýtt atburðarit bæði á `Bolti` og
  `Markvörður`:

  ```blocks
  þegar ég fæ sent [Varið v]
  stöðva [önnur forrit á karakter v]
  ```

  Eitt trikk er að fyrst skrifa þenna kóða fyrir boltann. Síðan er hægt að
  afrita það til `Markvörður` með því að draga kóðann í `Markvörður`-fígúruna í
  myndglugganum neðst á skjánum.

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Hættar bæði boltinn og markvörðurinn að hreyfa sig ef markvörðurinn
  stoppar boltann?

## Gátlisti {.check}

Nú munum við einnig athuga hvort boltinn hafi farið í mark. Við gerum þetta með
því að skoða hversu langt til hægri á skjánum boltinn hefur farið. Staða fígúru
í Scratch er lýst með hnitum: `(x hnit)`{.b} segir þar sem fígúra er til hliðar
á skánum, á meðan `(y hnit)`{.b} segir hversu langt upp eða niður á skjánum hún
er. Rétt fyrir neðan senunni eru tvær tölur merktar `x` og `y`. Þetta sýnir hnit
músarbendilsins. Þær breytast sjálfkrafa þegar hann færist.

![Mynd af hvar x og y hnitin birtast í Scratch](koordinater.png)

- [ ] Við segjum að það hafi orðið markmið ef boltinn fer nógu langt til hægri
  án þess að hann sé stoppað. Ef þú reynir að setja músarbendilinn á markið
  sérðu að marklínan er um `x` jafngild 230. Breyttu atburðarit boltans svolitið
  meira þannig að það lítur svona út:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (0) og y: (-50)
  bíða þangað til <snertir [Leo v]?>
  endalaust
      fara (6) skref
      ef <snertir [Markvörður v]?> þá
          senda [Varið v]
      annars
          ef <(x hnit) > [230]> þá
              senda [Mark v]
          end
      end
  end
  ```

- [ ] Eins og þegar boltinn verður stoppað getum við stoppað hreyfingu `Bolti` og
  `Markvörður` með því að setja þetta atburðaritið á báðar fígúrurnar.

  ```blocks
  þegar ég fæ sent [Mark v]
  stöðva [önnur forrit á karakter v]
  ```

- [ ] Við getum líka látið Leo hressa smá þegar hann skorar mörk. Smelltu á
  köttinn og gefðu honum eftirfarandi atburðarit:

  ```blocks
  þegar ég fæ sent [Mark v]
  segðu [Já, ég skoraði!!] í (2) sekúndur
  ```

- [ ] Gerðu svipaða aðburðarit þar sem `Leo` segir eitthvað um að hann veri
  dapur um að markið varðaðist. Prófaðu þetta á eigin spýtur!

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Geturðu skorað mörk?

- [ ] Getur markvörðurinn stoppað einhverjum skotum?

## Breyttu hraða {.protip}

Þú getur gert leikinn auðveldara eða erfiðara með því að breyta hraða boltans og
hversu hratt markvörðurinn færir sig. Báðir þessir eru ákvarðaðir af númerinu í
`fara () skref`{.b}-kubbunum fyrir `Bolti` og `Markvörður`.

Prófaðu mismumandi tölur fyrir bæði boltann og markvörðinn þar til þú finnur
samsetninguna sem þér líkar best. Gakktu ús skugga um að það gerist svolítið
erfitt, en ekki ómögulegt.


# Skref 5: Fyrsta skipti til 10! {.activity}

*Við munum loksins skoða hvernig við getum talið hversu mörg mörk eru skorin.*

## Gátlisti {.check}

Til að telja hversu mörg mörk þú hefur skorað og hversu mörg sinni `Markvörður`
hefur verjað markið munum við nota *breytur*.

- [ ] Smelltu á senunni hægra megin við kóðunarsvæðið.

- [ ] Smelltu á flipann `Breytur`{.blockdata} og búðu til nýja breytu. Gefðu
  nýja breytuna nafnið `Mörk`. Athugaðu að nýr kassi birtisti á senunni sem
  merktur er `Mörk` og sem synir númerið `0`{.blockdata}.

- [ ] Við munum nú telja mörkin. Búðu til nýtt atburðarit sem breytir
  `(Mörk)`{.b} í hvert skipti sem skilaboðin `Mark` eru send með því að búa til
  þetta atburðaritið á senunni:

  ```blocks
  þegar ég fæ sent [Mark v]
  breyttu [Mörk v] um (1)
  ```

- [ ] Við getum gert það sama til að telja fjölda varðanir. Búðu til nýja breytu
  sem heitir `(Varin)`{.b}.

- [ ] Búdu til nýjan atburðarit til að telja hversu mörg skot sem eru varin:

  ```blocks
  þegar ég fæ sent [Varið v]
  breyttu [Varin v] um (1)
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Telur leikurinn hvert skipti sem þú skorar mörk?

- [ ] Telur leikurinn einnig hvert skipti sem markvörðurinn stoppar boltann?

## Gátlisti {.check}

Að lokum munum við prófa hvort `Leo` tekst að skora 10 mörk eða að `Markvörður`
tekst að stoppa hann 10 sinnum. Þetta er svolítið mikið.

- [ ] Í fyrsta lagið munum við búa til tvær nýja bakgrunn, einn sem við getum
  notað ef leikmaðurinn vinnur (kötturinn skorar 10 sinnum) og einn sem við
  notum ef leikmaðurinn tapar (markvörðurinn varðar 10 sinnum). Smelltu á
  flipann `Bakgrunnar`. Hægrismeltu á litla útgáfuna af bakgrunni þínum í miðju
  skjásins og veldu `Gerðu afrit`.

- [ ] Veldu viðeigandi lit og smelltu síðan á textatólið. Veldu leturgerðina
  `Marker` neðst á skjánum. Skrifaðu texta svipað `Til hamingu, þú vannst!`
  svolítið hátt á afrit á bakgrunni. Gefðu þessari bakgrunni nafnið `Sigur`.

- [ ] Búðu til nýjan afrit af upprunalegu bakgrunni. Gefðu þessari bakgrunni
  nafnið `Tap` og skrifaðu viðeigandi texta.

- [ ] Búðu til handrit í bakgrunni sem setur breyturnar þínar í 0 í upphafi
  leiksins.

  ```blocks
  þegar smellt er á @greenFlag
  láttu [Mörk v] verða [0]
  láttu [Varin v] verða [0]
  bakgrunnur verður [Soccer 2]
  senda [Nýtt spark v]
  ```

- [ ] Við munum spila án þess að þurfa að smella á græna fánann í hvert skipti
  sem við skjóta vítaspyrnu. Fyrir þetta notum við skilaboðin `Nýtt spark`. Við
  verðum nú að skipta um

  ```blocks
  þegar smellt er á @greenFlag
  ```

  með

  ```blocks
  þegar ég fæ sent [Nýtt spark v]
  ```

  á bæði `Leo`, `Bolti` og `Markvörður`. Til dæmis verður atburðaritið hjá `Leo`
  svona:

  ```blocks
  þegar ég fæ sent [Nýtt spark v]
  fara til x: (-90) og y: (-60)
  ```

- [ ] Að lokum setjum við prófið um hvort við höfum skorað 10 mörk eða hvort
  markvörðurinn hefur varið 10 sinnum. Breyttu `Mark` atburðaritið á senunni
  þannig að það lítur svona út:

  ```blocks
  þegar ég fæ sent [Mark v]
  breyttu [Mörk v] um (1)
  bíða í (2) sekúndur
  ef <(Mörk) < [10]> þá
      senda [Nýtt spark v]
  annars
      bakgrunnur verður [Sigur v]
      stöðva [allt v]
  end
  ```

- [ ] Á sama hátt skaltu breyta `Varið` atburðaritið á senunni:

  ```blocks
  þegar ég fæ sent [Varið v]
  breyttu [Varin v] um (1)
  bíða í (2) sekúndur
  ef <(Varin) < [10]> þá
      senda [Nýtt spark v]
  annars
      bakgrunnur verður [Tap v]
      stöðva [allt v]
  end
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Færðu að skjóta mörk vítaspyrnur án þess að þurfa að slá græna fánann á
  hverjum tíma?

- [ ] Breytist leikurinn í rétta bakgrunni ef þú skorar 10 mörk?

- [ ] Breytist leikurinn í rétta bakgrunni ef markvörðurinn ver 10 sinnum?

- [ ] Endurstillur þú breyturnar `mörk` og `varin` þegar þú smellir á græna
  fánann?

## Hljóðbrellur {.protip}

Þú getur bætt við hljóðbrellur á leik með því að nota kubba undir
`Hljóð`{.blocksound}. Til dæmis geturðu reynt að bæta við hljóðum þegar
boltinn er sparkaður, þegar markvörðurinn ver eða þegar mark er skorað.

Til að finna fleiri hljóð til að nota í leiknum geturðu valið flipann `Hljóð`.
Hér geturðu fengið fleiri hljóð frá Scratch safninu eða jafnvel tekið upp eigin
hljóð. Prófaðu það!

## Vista leikinn {.save}

Þá erum við búnir með vítaspyrnu! Ef þú hefur einhverjar hugmyndir um hvernig á
að gera leikinn enn skemmtilegra skaltu reyna þá fyrir sjálfan þig.

Ef þú smellir á `Deila` verður verkefnið þitt sett á heimasíðu Scratch þannig
að aðrir geti spilað það!
