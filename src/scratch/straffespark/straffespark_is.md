---
title: Vítaspyrna
level: 1
author: Erik Kalstad og Geir Arne Hjelle
translator: Stein Olav Romslo og Aldís Mjöll Geirsdóttir
language: is
---


# Kynning {.intro}

Við ætlum að gera einfaldan fótboltaleik, þar sem þú verður að reyna að skora
eins margar vítaspyrnur og hægt er.

![Mynd af tilbúnum vítaspyrnuleik](straffespark.png)


# Skref 1: Kötturinn og fótboltavöllurinn {.activity}

*Við byrjum á því að búa til kött sem getur hreyft sig á fótboltavelli.*

## Gátlisti {.check}

- [ ] Byrjaðu nýtt verkefni, til dæmis með því að smella á `Smiða` efst á
  síðunni. Ef þú hefur nú þegar hafið verkefni geturðu byrjað nýtt með því að
  velja `Skrá` og síðan `Ný`.

- [ ] Smelltu á köttinn, og kallaðu köttinn `Leo`.

- [ ] Smelltu á ![Velja nýjan bakgrunn](../bilder/velg-bakgrunn.png) neðst til
  hægri á skjánum til að sækja nýjan bakgrunn. Veldu til dæmis bakgrunninn
  `Soccer 2` til þess að fá fótboltavöll með marki.

- [ ] Nú skulum við skrifa örforrit sem færir köttinn `Leo` þegar við smellum á
  hann. Smelltu á `Leo` í myndglugganum neðst á skjánum til þess að kóða hvað
  hann á að gera. Settu saman eftirfarandi kubba í kóðunargluggann til vinstri:

  ```blocks
  þegar smellt er á þennan karakter
  fara (10) skref
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Fer `Leo` áfram þegar þú smellir á hann?

- [ ] Hvað gerist þegar þú smellir á `Leo` þangað til hann fer út á enda?

## Gátlisti {.check}

- [ ] Þú getur flutt `Leo` aftur á skjáinn með því að smella á hann og draga
  hann þar sem þú vilt.

- [ ] Við munum forrita auðveldari leið til að fá `Leo` aftur á völlinn. Búðu
  til nýtt örforrit við hliðina á því sem þú hefur þegar búið til, sem lítur
  svona út:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (-90) og y: (-60)
  ```

- [ ] Nú mun `Leo` koma aftur á völlinn í hvert skipti sem þú smellir á græna
  fánann.

## Vista verkefnið {.save}

Þú hefur nú skrifað lítið forrit! Scratch vistar allt sem þú gerir reglulega.
Það er engu að síður góð venja að vista inni á milli.

- [ ] Yfir senunni er textareitur þar sem þú getur gefið leiknum þínum nafn. Til
  dæmis geturðu kallað hann `Vítaspyrna`.

- [ ] Í valmyndinni `Skrá` er hægt að velja `Vista núna` til að vista verkefnið.


# Skref 2: Leo sparkar boltanum {.activity}

*Það næsta sem við þurfum í leik okkar er bolti!*

## Gátlisti {.check}

- [ ] Við munum nú bæta við bolta í leik okkar. Smelltu á ![Veldu mynd úr
  safni](../bilder/hent-fra-bibliotek.png) og veldu fótboltann `Sports/Soccer
  Ball`.

- [ ] Kallaðu boltann `Bolti`.

- [ ] Gerðu boltann minni með því að ýta fyrst á `Stærð` reitinn og breyta
  númerinu frá 100 til 60.

- [ ] Við munum nú skrifa örlítið lengra örforrit fyrir boltann. Í þessu
  örforriti setjum við fyrst boltann fyrir framan köttinn. Eftir að boltinn
  snertir `Leo` (þ.e. `Leo` sparkar í boltann) byrjar boltinn að hreyfa sig.
  Sjáðu hvort þú þekkir hvar í örforritinu mismunandi hlutir eru gerðir:

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

- [ ] Sparkar `Leo` í boltann þegar þú smellir á hann?

- [ ] Getur `Leo` sparkað í boltann aftur ef þú smellir á græna fánann aftur?

- [ ] Ef `Leo` snertir boltann áður en þú smellir á hann (þegar þú smellir á
  græna fánann) þarftu að breyta tölunum í `fara til x: () og y: ()`{.b}-kubbnum
  þannig að boltinn er í hvild fyrir framan `Leo`.

- [ ] Stundum hreyfist boltinn aftur *áður en* `Leo` er á réttum stað, þannig að
  hann snertir boltann aftur og boltinn byrjar hreyfast. Þá hjálpar það að bæta
  við einu `bíða í (1) sekúndur`{.b}-kubba fyrir `bíða þangað til <snertir [Leo
  v]?>`{.b}-kubbann.


# Skref 3: Við þurfum markvörð! {.activity}

*Við munum nú gera leikinn svolítið erfiðari með því að forrita markvörð.*

## Gátlisti {.check}

- [ ] Bættu við fígúru sem getur verið markvörður. Við höfum notað kolkrabba
  `Animals/Octopus`, en þú getur líka notað aðrar fígúrur ef þú vilt.

- [ ] Settu fígúruna inn í markið. Það er hægt að snúa fígúrunni með því að
  smella á `Búningar` og síðan á táknið sem er hægra megin við eyða-takkann.

- [ ] Gefðu fígúrunni nafnið `Markvörður`.

- [ ] Gerðu eftirfarandi örforrit fyrir markvörðinn:

  ```blocks
  þegar smellt er á @greenFlag
  fara til x: (200) og y: (-50)
  stefna í (0 v) gráður
  endalaust
    fara (15) skref
    ef á kanti snúðu við
  end
  ```

  Það eru nokkrir nýir kubbar í þessu örforriti. Lestu forritið vandlega. Hvað
  heldurðu að nýju kubbarnir geri?

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Byrjar markvörðurinn í markinu?

- [ ] Fer `Markvörður` til hægri og vinstri á skjánum?

## Gátlisti {.check}

- [ ] Finnst þér kannski markvörðurinn vera svolítið stór? Þú getur breytt stærð
  hans eins og þú gerðir áður. Önnur leið til að breyta stærð er með því að nota
  kubba úr flipanum `Útlit`{.blocklooks}.

  Settu inn kubbinn `stærð verður (100)%`{.b} í
  `endalaust`{.blockcontrol}-slaufuna. Þú getur prófað að breyta `100%` í aðrar
  tölur þar til þú finnur viðeigandi stærð fyrir markvörðinn. Ef þú notar
  kolkrabbann sem `Markvörður` passar `50%` nokkuð vel. Prófaðu það!

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Hvað gerist þegar `Leo` skýtur á markið? Getur markvörðurinn varið markið?


# Skref 4: Markvörðurinn ver! {.activity}

*Nú er kominn tími á að markvörðurinn verji markið!*

Við munum nú gera nokkrar *prófanir* sem segja okkur hvort markvörðurinn verji
boltann eða hvort boltinn fari í mark.

## Gátlisti {.check}

- [ ] Við byrjum á að finna út hvort markvörðurinn ver boltann. Smelltu á
  `Bolti`. Bættu við einum `ef annars`{.blockcontrol}-kubbi í örforritið:

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

  Í kubbnum `senda [message1 v]`{.b} verður þú að velja `Ný skilaboð` og síðan
  skrifa `Varið` sem skilaboð.

  Fígúrurnar geta sent skilaboð í leiknum á milli sín án þess að þú sjáir það í
  raun. Þetta gerir það einfaldara fyrir margar fígúrur að bregðast við því sem
  gerist.

- [ ] Nú viljum við að bæði boltinn og markvörðurinn hætti að hreyfa sig ef
  boltinn verður varinn. Bættu þessu við sem nýju örforriti bæði á `Bolti` og
  `Markvörður`:

  ```blocks
  þegar ég fæ sent [Varið v]
  stöðva [önnur forrit á karakter v]
  ```

  Eitt ráð er að skrifa fyrst þennan kóða fyrir boltann. Síðan er hægt að afrita
  það til `Markvörður` með því að draga kóðann í `Markvörður`-fígúruna í
  myndglugganum neðst á skjánum.

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Hættir bæði boltinn og markvörðurinn að hreyfa sig ef markvörðurinn ver
  boltann?

## Gátlisti {.check}

Nú munum við einnig athuga hvort boltinn hafi farið í mark. Við gerum þetta með
því að skoða hversu langt til hægri á skjánum boltinn hefur farið. Staða fígúru
í Scratch er lýst með hnitum: `(x hnit)`{.b} segir hvar fígúran er á skjánum frá
vinstri til hægri en `(y hnit)`{.b} segir hversu langt upp eða niður á skjánum
hún er. Rétt fyrir neðan leikinn eru tvær tölur merktar `x` og `y`. Þetta sýnir
hnit músarbendilsins. Þær breytast sjálfkrafa þegar hann færist.

![Mynd af því hvar x og y hnitin birtast í Scratch](koordinater.png)

- [ ] `Leo` skorar ef boltinn fer nógu langt til hægri án þess að hann sé
  varinn. Ef þú reynir að setja músarbendilinn á markið sérðu að marklínan er
  þar sem `x` er 230. Breyttu örforriti boltans svolítið meira þannig að það
  líti svona út:

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

- [ ] A sama hátt og boltinn er varinn er hægt að stoppa hreyfingu `Bolti` og
  `Markvörður` með því að setja þetta örforrit á báðar fígúrurnar.

  ```blocks
  þegar ég fæ sent [Mark v]
  stöðva [önnur forrit á karakter v]
  ```

- [ ] Við getum líka látið `Leo` fagna smá þegar hann skorar mörk. Smelltu á
  köttinn og gefðu honum eftirfarandi örforrit:

  ```blocks
  þegar ég fæ sent [Mark v]
  segðu [Já, ég skoraði!!] í (2) sekúndur
  ```

- [ ] Gerðu svipað örforrit þar sem `Leo` segir eitthvað um að hann sé leiður
  vegna þess að skotið hans var varið. Prófaðu þetta á eigin spýtur!

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Geturðu skorað mörk?

- [ ] Getur markvörðurinn varið einhver skot?

## Breyttu hraða {.protip}

Þú getur gert leikinn auðveldari eða erfiðari með því að breyta hraða boltans og
hversu hratt markvörðurinn færir sig. Hraði fyrir bolta og markvörð ákvarðast af
númerinu í `fara () skref`{.b}-kubbunum fyrir `Bolti` og `Markvörður`.

Prófaðu mismumandi tölur fyrir bæði boltann og markvörðinn þar til þú finnur
samsetningu sem þér líkar best. Gakktu úr skugga um að það verði svolítið
erfitt, en ekki ómögulegt.


# Skref 5: Fyrri til að ná 10! {.activity}

*Við munum skoða hvernig við getum talið hversu mörg mörk eru skoruð.*

## Gátlisti {.check}

Til að telja hversu mörg mörk þú hefur skorað og hversu mörgum sinnum
`Markvörður` hefur varið markið munum við nota *breytur*.

- [ ] Smelltu á senuna hægra megin við kóðunarsvæðið.

- [ ] Smelltu á flipann `Breytur`{.blockdata} og búðu til nýja breytu. Gefðu
  nýju breytunni nafnið `Mörk`. Athugaðu að nýr kassi birtist á senunni sem
  merktur er `Mörk` og sem sýnir númerið `0`{.blockdata}.

- [ ] Við munum nú telja mörkin. Búðu til nýtt örforrit sem breytir `(Mörk)`{.b}
  í hvert skipti sem skilaboðin `Mark` eru send með því að búa til þetta
  örforrit á senunni:

  ```blocks
  þegar ég fæ sent [Mark v]
  breyttu [Mörk v] um (1)
  ```

- [ ] Við getum gert það sama til að telja hversu oft markmaðurinn varði. Búðu
  til nýja breytu sem heitir `(Varin)`{.b}.

- [ ] Búðu til nýtt örforrit til að telja hversu mörg skot eru varin:

  ```blocks
  þegar ég fæ sent [Varið v]
  breyttu [Varin v] um (1)
  ```

## Prófaðu verkefnið {.flag}

__Smelltu á græna fánann.__

- [ ] Telur leikurinn hvert skipti sem þú skorar mörk?

- [ ] Telur leikurinn einnig hvert skipti sem markvörðurinn ver boltann?

## Gátlisti {.check}

Að lokum munum við prófa hvort `Leo` tekst að skora 10 mörk eða hvort
`Markvörður` tekst að verja hann 10 sinnum. Þetta er svolítið mikið.

- [ ] Í fyrsta lagi munum við búa til tvo nýja bakgrunni, einn sem við getum
  notað ef leikmaðurinn vinnur (kötturinn skorar 10 sinnum) og einn sem við
  notum ef leikmaðurinn tapar (markvörðurinn ver 10 sinnum). Smelltu á flipann
  `Bakgrunnar`. Hægrismelltu á litlu útgáfuna af bakgrunninum þínum og veldu
  `Gerðu afrit`.

- [ ] Veldu viðeigandi lit og smelltu síðan á textaverkfærið. Veldu leturgerðina
  `Marker` neðst á skjánum. Skrifaðu texta eins og `Til hamingu, þú vannst!`
  svolítið hátt á afritinu af bakgrunninum. Gefðu þessum bakgrunni nafnið
  `Sigur`.

- [ ] Búðu til nýtt afrit af upprunalega bakgrunninum. Gefðu þessum bakgrunni
  nafnið `Tap` og skrifaðu viðeigandi texta.

- [ ] Búðu til örforrit á bakgrunninn sem setur breyturnar þínar í 0 í upphafi
  leiksins.

  ```blocks
  þegar smellt er á @greenFlag
  láttu [Mörk v] verða [0]
  láttu [Varin v] verða [0]
  bakgrunnur verður [Soccer 2]
  senda [Nýtt spark v]
  ```

- [ ] Við munum spila án þess að þurfa að smella á græna fánann í hvert skipti
  sem við tökum vítaspyrnu. Fyrir þetta notum við skilaboðin `Nýtt spark`. Við
  verðum nú að skipta um

  ```blocks
  þegar smellt er á @greenFlag
  ```

  með

  ```blocks
  þegar ég fæ sent [Nýtt spark v]
  ```

  á bæði `Leo`, `Bolti` og `Markvörður`. Sem dæmi verður örforritið hjá `Leo`
  svona:

  ```blocks
  þegar ég fæ sent [Nýtt spark v]
  fara til x: (-90) og y: (-60)
  ```

- [ ] Að lokum prófum við hvort við höfum skorað 10 mörk eða hvort markvörðurinn
  hefur varið 10 sinnum. Breyttu `Mark` örforritinu á senunni þannig að það líti
  svona út:

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

- [ ] Á sama hátt skaltu breyta `Varið` örforritinu á senunni:

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

- [ ] Færðu að taka margar vítaspyrnur án þess að þurfa að smella á græna fánann
  í hvert skipti?

- [ ] Breytist leikurinn í réttan bakgrunn ef þú skorar 10 mörk?

- [ ] Breytist leikurinn í réttan bakgrunn ef markvörðurinn ver 10 sinnum?

- [ ] Endurstillir þú breyturnar `mörk` og `varin` þegar þú smellir á græna
  fánann?

## Hljóðbrellur {.protip}

Þú getur bætt við hljóðbrellum í leikinn með því að nota kubba undir
`Hljóð`{.blocksound}. Til dæmis geturðu reynt að bæta við hljóðum þegar sparkað
er í boltann, markvörðurinn ver eða mark er skorað.

Til að finna fleiri hljóð til að nota í leiknum geturðu valið flipann `Hljóð`.
Hér geturðu fengið fleiri hljóð frá Scratch safninu eða jafnvel tekið upp eigin
hljóð. Prófaðu það!

## Vista leikinn {.save}

Þá erum við búin með vítaspyrnuleikinn! Ef þú hefur einhverjar hugmyndir um
hvernig á að gera leikinn enn skemmtilegri skaltu prófa það á eigin spýtur.

Ef þú smellir á `Deila` verður leikurinn þinn settur á heimasíðu Scratch þannig
að aðrir geti spilað hann!
