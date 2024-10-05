---
title: Анімація на Хелловін
level: 1
author: 'Торбйорн Скаулі та Гейр Арне Хєлле'
translator: 'Anatolii Pylypenko'
language: ua
---


# Вступ {.intro}

Тут ми розглянемо, як можна створювати різні анімації на тему Хелловіну. 
Ми можемо поділитися ними з друзями за допомогою Scratch, або ж зробити ще цікавіше: Ми можемо спроектувати їх на штору, простирадло або стіну під час Хелловіну.

![Зображення страшного обличчя на Хелловін](halloweenimasjon.jpg)


# Крок 1: Початкова анімація {.activity}

*Ми починаємо з того, що дозволяємо страшному привиду літати туди-сюди по екрану.*

## Контрольний список {.check}

- [ ] Почніть новий проект. Видаліть символ кота, наприклад, клацнувши правою кнопкою миші на ньому і вибравши пункт `вилучити`.

- [ ] Виберіть нового персонажа, натиснувши
  ![Виберіть форму з бібліотеки](../bilder/hent-fra-bibliotek.png). Знайдіть щось страшне, наприклад, привида! Ми використовували `Фантазії/Привид`.

- [ ] Торкніться поля імені над своєю фігурою. Назвіть його `Привид`.

  ![Зображення страшного привида](spokelse.png)

- [ ] Тепер ми створимо простий скрипт, який змусить привида літати по екрану.  Створіть `повторити`{.blockcontrol}- та блок
  `перемістити`{.blockmotion}-kloss таким чином:

  ```blocks
  повторити (200) 
      перемістити на (5) кроків
  slutt
  ```

- [ ] Натисніть на свій сценарій, щоб запустити анімацію. Ваш привид рухається? Ви бачите проблему?

- [ ] Привид виглядає так, ніби він застрягає, коли доходить до краю! Ми можемо виправити це за допомогою блоку 
  `якщо на межі, відбити`{.blockmotion}:

  ```blocks
  повторити (200)
      перемістити на (5) кроків
      якщо на межі, відбити
  slutt
  ```

- [ ] Знову натисніть на свій сценарій. Тепер це працює краще?

- [ ] Хм... Привид летить догори ногами... Виглядає трохи дивно. Можна сказати, що привид повинен повертатися тільки в бік з блоком
  `стиль обертання`{.blockmotion}. Ми поставимо це на самому початку сценарію, ось так:

  ```blocks
  стиль обертання [не обертати]
  повторити (200) 
      перемістити на (5) кроків
      якщо на межі, відбити
  slutt
  ```

- [ ] Нарешті, на чорному тлі це виглядає ще страшніше! Натисніть
  `Сцена` у правому нижньому куті екрана, а потім перейдіть на вкладку
  `Тло`{.blocklightgrey} у верхній частині екрана. І тепер натисніть  `У растрове`.

- [ ] Клацніть на відерце з фарбою,
  ![Заповнити кольором](../bilder/fyll-med-farge.png), а потім на тло, щоб зафарбувати його чорним кольором.

- [ ] Назвемо тло `Чорний`.


# Крок 2: Ще одна анімація {.activity}

*Для нашої другої анімації до нас прилетить кажан.*

![Зображення страшного кажана](flaggermus.png)

## Контрольний список {.check}

- [ ] Створіть нового персонажа, натиснувши
  ![Виберіть форму з бібліотеки](../bilder/hent-fra-bibliotek.png). Ми використали `Фантазії/Bat`. Змініть ім'я персонажа на `Кажан`.

- [ ] Щоб виглядало так, ніби кажан летить до нас, ми хочемо, щоб він спочатку був дуже маленьким, а потім збільшувався. Створіть цей скрипт.

  ```blocks
  задати розмір (0) %
  повторити (100)
      змінити розмір на (4)
  slutt
  ```

- [ ] Натисніть на скрипт, щоб перевірити, чи він працює.

- [ ] Невелика проблема полягає в тому, що привид також знаходиться на екрані. Було б краще приховати привида, коли він не анімаційний. Клацніть на персонажа-привида і додайте до сценарію блок `показати`{.blocklooks}- і
  `сховати`{.blocklooks}:

  ```blocks
  стиль обертання [не обертати]
  показати
  повторити (200) 
      перемістити на (5) кроків
      якщо на межі, відбити
  slutt
  сховати
  ```

- [ ] Натисніть на сценарій привида. Чи сховається привид після того, як закінчить літати туди-сюди?

- [ ] Те ж саме можна зробити зі скриптом кажана. Натисніть на малюнок кажана і змініть скрипт на

  ```blocks
  задати розмір (0) %
  показати
  повторити (100) 
      зміниити розмір на (4)
  slutt
  сховати
  ```

- [ ] Для більшої різноманітності ми хочемо, щоб кажана було анімовано на моторошному лісовому тлі. Натисніть на
  ![Виберіть готовий фон](../bilder/velg-bakgrunn.png)
  у правому нижньому куті екрана і виберіть тло
  `Поза приміщенням/Woods`. Назвіть тло `Ліс`.


# Крок 3: Змініть тло {.activity}

*Зараз ми розглянемо, як можна легко перемикати фон під час запуску анімації.*

## Контрольний список {.check}

Наприклад, якщо ми хочемо показати анімацію привида на чорному тлі, ми повинні спочатку натиснути `Сцена`, потім вкладку `Тло`та чорний фон. Крім того, нам потрібно натиснути фігуру привида, вкладку `Код` і, нарешті, сам сценарій. Це дуже громіздко! Тепер ми побачимо, як ми можемо використовувати повідомлення, щоб зробити це набагато простіше.

Meldinger gjør det lett å få flere ting til å skje samtidig. Vi skal
nå først lage en melding, `Animer spøkelse`. Vi vil at denne meldingen
skal både bytte bakgrunnen og starte spøkelsesanimasjonen.

- [ ] Klikk på `Scene` og lag dette skriptet:

  ```blocks
  når jeg mottar [Animer spøkelse v]
  bytt bakgrunn til [Svart v]
  ```

- [ ] Klikk på spøkelsesfiguren og endre skriptet ved å legge til en kloss
  på toppen:

  ```blocks
  når jeg mottar [Animer spøkelse v]
  begrens rotasjon [vend sideveis v]
  vis
  gjenta (200) ganger
      gå (5) steg
      sprett tilbake ved kanten
  slutt
  skjul
  ```

- [ ] Nå venter skriptene våre på meldingen. For å teste kan vi dra
  klossen

  ```blocks
  send melding [Animer spøkelse v]
  ```

  ut ved siden av det store skriptet til spøkelset.

- [ ] Send meldingen ved å klikke på `send melding`{.blockevents}-klossen.
  Animeres spøkelset over en svart bakgrunn?

- [ ] Vi vil nå gjøre det samme for flaggermusen. Legg til et nytt skript på
  scenen:

  ```blocks
  når jeg mottar [Animer flaggermus v]
  bytt bakgrunn til [Skog v]
  ```

- [ ] Klikk på flaggermusfiguren og endre skriptet slik

  ```blocks
  når jeg mottar [Animer flaggermus v]
  sett størrelse til (0) %
  vis
  gjenta (100) ganger
      endre størrelse med (4)
  slutt
  skjul
  ```

- [ ] Legg også til klossen

  ```blocks
  send melding [Animer flaggermus v]
  ```

  for å teste at animasjonen fungerer.

- [ ] Send meldingene som animerer spøkelset og flaggermusen. Starter
  animasjonene når du klikker på meldingene? Byttes bakgrunnene
  riktig?


# Steg 4: Koble sammen animasjonene {.activity}

*Nå skal vi se hvordan vi kan koble sammen animasjonene slik at de
 vises i sekvens etter hverandre.*

## Sjekkliste {.check}

- [ ] Vi begynner med å lage en `gjenta for alltid`{.blockcontrol}-løkke på
  scenen, som sender meldinger:

  ```blocks
  gjenta for alltid
      send melding [Animer spøkelse v] og vent
      send melding [Animer flaggermus v] og vent
  slutt
  ```

- [ ] Klikk på skriptet for å teste det. Trykk den røde stopp-sirkelen for
  å stoppe animasjonen. Vises animasjonene etter hverandre om og om igjen?

- [ ] Det vil se litt bedre ut med en kort pause mellom animasjonene. Legg
  til et par `vent`{.blockcontrol}-klosser i skriptet.

  ```blocks
  gjenta for alltid
      send melding [Animer spøkelse v] og vent
      vent (1) sekunder
      send melding [Animer flaggermusen v] og vent
      vent (1) sekunder
  slutt
  ```

- [ ] For å gjøre det enklere å starte animasjonen legger vi til en kloss
  som gjør at animasjonen starter når det grønne flagget øverst på
  skjermen klikkes.

  ```blocks
  når @greenFlag klikkes
  gjenta for alltid
      send melding [Animer spøkelse v] og vent
      vent (1) sekunder
      send melding [Animer flaggermus v] og vent
      vent (1) sekunder
  slutt
  ```

- [ ] Vi kan også bruke grønt flagg-klosser på figurene for å være sikre
  på at de starter animasjonen på riktig måte. Legg dette skriptet på
  spøkelset:

  ```blocks
  når @greenFlag klikkes
  skjul
  gå til x: (0) y:(0)
  ```

- [ ] Legg et tilsvarende skript på flaggermusen:

  ```blocks
  når @greenFlag klikkes
  skjul
  gå til x: (0) y:(0)
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Kjøres begge animasjonene etter hverandre? Dukker figurene opp når de skal?

- [ ] Endre gjerne i animasjonene slik at du synes de ser bedre
  ut. Kanskje du vil ha litt andre figurer? Hvordan kan du få figurene
  til å bevege seg raskere? Kanskje litt mer tilfeldig? Prøv deg frem!


# Steg 5: Tegn egne figurer {.activity}

*Vi vil nå lage en tredje animasjon hvor vi tegner en figur på egen hånd*

## Sjekkliste {.check}

- [ ] Lag en ny figur ved å flytte pekeren over
  ![Velg figur fra biblioteket](../bilder/hent-fra-bibliotek.png), og
  klikk så `Tegn`. Du kan tegne hva du vil. Her har vi tegnet et
  Jack-O'-Lantern-gresskar.

  ![Bilde av gresskar med utskjært ansikt](gresskar.png)

- [ ] Lag en kopi av drakten du nettopp tegnet ved å høyreklikke på
  miniatyren under `Ny drakt`-overskriften og velg `lag en kopi`.

  ![Bilde av hvordan lage en kopi av gresskaret i scratch](kopier_gresskar.png)

- [ ] Endre litt på den kopierte drakten, slik at du får to drakter som er
  ganske, men ikke helt, like. Vi vil nå animere figuren ved å bytte
  mellom de to draktene.

- [ ] Klikk på `Kode`{.blocklightgrey}-fanen og legg på dette skriptet:

  ```blocks
  når jeg mottar [Animer gresskar v]
  vis
  gjenta (50) ganger
      neste drakt
      vent (tilfeldig tall fra (0.1) til (0.3)) sekunder
  slutt
  skjul
  ```

  Bytt gjerne ut meldingsnavnet `Animer gresskar` med noe som passer
  for din figur. Klikk på skriptet (eller send en melding) for å
  teste animasjonen. Ser det bra ut?

- [ ] Legg også til startposisjonen for den figuren:

  ```blocks
  når @greenFlag klikkes
  skjul
  gå til x: (0) y: (0)
  ```

- [ ] Gå så til scenen og legg på et skript som bytter til riktig bakgrunn
  for den siste animasjonen. Her har vi brukt den svarte bakgrunnen.

  ```blocks
  når jeg mottar [Animer gresskar v]
  bytt bakgrunn til [Svart v]
  ```

- [ ] Til slutt legger vi denne siste animasjonen til i hovedløkken som
  viser animasjonene:

  ```blocks
  når @greenFlag klikkes
  gjenta for alltid
      send melding [Animer spøkelse v] og vent
      vent (1) sekunder
      send melding [Animer flaggermus v] og vent
      vent (1) sekunder
      send melding [Animer gresskar v] og vent
      vent (1) sekunder
  slutt
  ```


# Steg 6: Enda flere animasjoner? {.activity}

## Prøv selv {.challenge}

Vi har nå sett noen eksempler på hvordan vi kan lage skumle
halloween-animasjoner. Prøv å bruk lignende teknikker for å lage dine
egne animasjoner!

## Legg ut prosjektet {.save}

Når du er fornøyd med animasjonene dine kan du dele det med familie og
venner, ved å trykke `Legg ut`.


# Projiser animasjonene {.activity}

*Vi avslutter med å se på hvordan du kan skremme nabolaget med de
 skumle animasjonene dine slik at alle kan se dem.*

Det enkleste er å sette skjermen i vinduet, og klikke på firkanten for
fullskjermvisning øverst til venstre under Scratch-logoen. Men hvis du
kan låne en prosjektør til Halloween kan du vise animasjonen utendørs,
på en vegg eller på et gardin eller laken, slik bildet i begynnelsen
viser. I begge tilfeller er det litt dumt at Scratch viser animasjonen
med en hvit ramme på skjermen. For å få en bedre visning kan du følge
tipsene nedenfor.

## Sjekkliste {.check}

- [ ] Først lager vi en fil som viser animasjonen din i et større vindu
  med svart bakgrunn. Dette gjør vi med litt HTML-kode. HTML er det
  språket som brukes til å lage nettsider.

  Last ned filen [projiser.html](projiser.html).  Etter at du har
  gått til denne adressen kan du velge `Fil > lagre som`, eller noe
  som ligner, i menyen til nettleseren din. Legg filen et sted du
  finner den igjen.

- [ ] Åpne filen i Notepad eller et tilsvarende program. Du vil se en
  tekst som ser slik ut:

  ```html
  <html>
  <head>
  <title>Halloweenimasjon</title>
  </head>

  <body bgcolor="#000000">
  <div style="overflow-y: hidden; height: 890px; margin-left: auto; margin-right: auto; width: 1180px;" id="applet">
  <iframe
    style="margin-top:-56px; margin-left: -10px"
    allowtransparency="true"
    width="1200"
    height="960"
    src="http://scratch.mit.edu/projects/embed/30923784/?autostart=true"
    frameborder="0"
    scrolling="no"
    seamless="seamless"
    allowfullscreen=""></iframe>
  </div>
  </body>
  </html>
  ```

- [ ] Gjemt inne i denne teksten står det et Scratch-prosjektnummer. I
  dette tilfelle er nummeret `30923784`. Du må bytte dette nummeret
  med prosjektnummeret ditt.

### Prosjektnummer {.protip}

For å finne prosjektnummeret ditt kan du se i adressefeltet i
nettleseren din mens du jobber med prosjektet. Som en del av adressen
finner du et 8-sifret tall. Dette er ditt prosjektnummer.

## Sjekkliste {.check}

- [ ] Bytt `30923784` med ditt prosjektnummer og lagre filen.

- [ ] I nettleseren din kan du nå åpne filen du nettopp endret. Velg
  `Fil > åpne fil`, eller noe som ligner, i nettleseren din. Velg den
  riktige filen.

- [ ] Du skal nå se animasjonen din på svart bakgrunn.

- [ ] Koble datamaskinen din til en prosjektør, og vis animasjonen
  din på et hvitt laken, en gardin eller kanskje en vegg!
