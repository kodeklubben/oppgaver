---
title: Змія
level: 4
author: 'Geir Arne Hjelle og Martin Lie'
translator: 'Оксана Біщак'
language: ua
---


# Вступ {.intro}

Деякі варіанти Змійки існували майже на кожному персональному комп’ютері з кінця 1970-х років. Гра стала особливо популярною, коли вона з’явилася на мобільних телефонах Nokia у 1997 році, а останніми роками гра навіть була включена до колекції Музею сучасного мистецтва Нью-Йорка.

Сама гра передбачає просто керування змією по екрану, при цьому змія повинна уникати зіткнення з краєм екрана або з самою собою. Змія росте, поїдаючи яблука, які з’являються у випадкових місцях на екрані. Змію можна розвивати багатьма способами, або створюючи додаткові перешкоди на екрані, за допомогою різних видів бонусних яблук або, наприклад, за допомогою двох змій, які змагаються, щоб з’їсти яблука та замкнути одна одну.

![Illustrasjon av et ferdig Snake spill](snake.png)


# Огляд проекту {.activity}

*Більшу частину кодування Snake ви зробите самостійно. У Snake ми використовуємо клонів трохи особливим і досить хитрим способом. Тому ми зосередимося на клонуванні на початку цього уроку.*

## План перевірки {.check}

- [ ] Змія рухається...чи це так?

- [ ] Керуйте змією, поки вона не розіб'ється!

- [ ] Яблука та інші закуски.

- [ ] Стіни, бонусні яблука, більше змій та інші випробування.


# Крок 1. Змія рухається... чи це так? {.activity}

*Змійка — це в основному проста гра. Але одна проблема полягає в тому, як рухати саму змійку. Спочатку може здатися, що вам потрібен якийсь список, який пам’ятає, де знаходиться кожна частина змійки, щоб ви могли її перемістити.*

Замість використання списків ми будемо використовувати клонування дещо особливим способом. Пам'ятайте, що під час клонування ми копіюємо як зовнішність, так і поведінку персонажа. Ми почнемо з простого блоку, який буде частиною тіла змії. Цей блок ми будемо переміщати, клонувати, переміщати, клонувати і так далі. Фокус, щоб створити враження, що змія рухається, полягає в тому, що старі клони через деякий час видаляються.

На малюнку синє поле — це голова змії, зелені — тіло змії, а білі — вказують, де була змія (але насправді це видалені клоновані поля).

![Bilde av slangen, og hvor den har vært](teller.png)

Щоб знати, коли видаляти клони, ми використовуємо три змінні:
`довжина`{.blockdata} — це довжина змії, `кількість`{.blockdata} — простий лічильник, який підраховує, скільки кроків зробила змія з початку гри. Нарешті, `моїм ідентифікатором`{.blockdata} буде число, яке вказує, яким номером у рядку є даний клон. Зверху в кожному полі вказано `мій ідентифікатор`{.blockdata}, `кількість`{.blockdata} — 16, оскільки змія зробила 16 кроків, а `довжина`{.blockdata} — 6.

Трюк тепер досить простий. Кожен клон видаляється сам, якщо `мій ідентифікатор`{.blockdata} менший за `довжину`{.blockdata} - `лічильника`{.blockdata}. Давайте спробуємо це на практиці.

## Контрольний список {.check}

- [ ] Розпочніть новий проект.

- [ ] Зробіть форму блока. Намалюйте це самі. Ви повинні зробити його досить маленьким, щоб у вас було місце для довгої 
  змії на екрані. Також переконайтеся, що блок такий же широкий, як і високий. Десь між `10 х 10` і `20 х 20` є хорошим       розміром.

  ![Bilde av en eksempelboks i Scratch](boks_ua.png)

- [ ] Потім створіть три змінні: `довжина`{.blockdata} і `кількість`{.blockdata}
  мають застосовуватися до всіх фігур, тоді як `мій ідентифікатор`{.blockdata} має застосовуватися лише до цієї фігури,       оскільки він має бути різним для кожного клону.

- [ ] Тепер ми створимо основний цикл гри. Спочатку ми встановлюємо необхідні змінні, а потім використовуємо цикл для         постійного створення нових блоків змійки.

  ```blocks
  коли я отримую [Нова гра v]
  змінити [Рахунок v] на [0]
  змінити [Довжина v] на [5]
  повторити до <торкається [межа v] ?>
      змінити [Мій ідентифікатор v] на (Рахунок)
      надати [Рахунок v] значення (1)
      чекати (0.1) секунд
      створити клон з [мене v]
      перемістити на (10) кроків
  slutt
  ```

  Тут `10` у блоці `перемістити на 10 кроків`{.blockmotion} мають збігатися з розміром вашого блоку.

- [ ] Самим клонованим боксам тепер потрібно просто почекати, доки вони самі видаляться. Це досить просто.

  ```blocks
  коли я починаю як клон
  чекати поки <((Рахунок) - (Довжина)) > (Мій ідентифікатор)>
  вилучити цей клон
  ```

  Порівняйте ці сценарії з малюнком і поясненням вище. Ви розумієте, як вони працюють?

- [ ] Спробуйте свою гру. Було б добре створити сценарій на сцені, який видає повідомлення `Нова гра`, коли клацає зелений    прапорець. Ви повинні побачити змію, що рухається по екрану, звичайно, ви ще не можете керувати нею!


# Steg 2: Styr slangen til den krasjer! {.activity}

*Vi skal nå kontrollere slangen med piltastene.*

Det er lett å bruke piltastene til å kontrollere slangen. Siden den går av seg
selv trenger vi bare å endre retningen når piltastene trykkes.

## Sjekkliste {.check}

- [ ] Lag et nytt skript som også starter på `Nytt spill`-meldingen. Lag en
  `gjenta for alltid`{.blockcontrol}-løkke hvor du tester om hver piltast er
  trykket og endrer hvilken retning figuren peker tilsvarende.

- [ ] Legg til en `gå til x: y:`{.blockmotion}- og en `pek i
  retning`{.blockmotion}-kloss først i skriptet ditt slik at slangen starter et
  fornuftig sted i begynnelsen av spillet.

- [ ] Du kan markere hodet til slangen ved å lage en ekstra drakt. Lag for
  eksempel en kopi av den boksen du allerede har tegnet, og endre fargen på
  denne. Kall en av draktene `hode` og den andre `kropp`. Du kan da bruke
  `hode`-drakten i hovedløkken hvor du genererer klonen. I skriptet for hver
  klon endrer du så drakten til `kropp` før `vente`{.blockcontrol}-klossen.

- [ ] Legg også inn en sjekk på om slangen krasjer i seg selv. Dette kan du for
  eksempel gjøre ved å utvide testen i `gjenta til`{.blockcontrol}-klossen med
  `eller`{.blockoperators} og `berører fargen`{.blocksensing}.

- [ ] Prøv spillet ditt. Du skal nå kunne styre slangen din rundt på skjermen,
  helt til du krasjer i kanten eller i deg selv.


# Steg 3: Epler og annet snadder {.activity}

*Nå skal vi gi slangen litt mål og mening. Ved å spise epler kan slangen vokse
 seg stor og sterk!*

Eplene er ganske enkle å lage da vi bare trenger en figur som blir borte når
slangen spiser dem. For å enklere kunne utvide med flere epler og slikt senere
bruker vi kloner av eplene også.

## Sjekkliste {.check}

- [ ] Lag en ny eplefigur. Denne bør være omtrent like stor som slangen. For
  eksempel en rød fyllt sirkel som er omtrent `10 x 10` passer bra.

- [ ] Lag et skript som starter på en ny melding `Lag eple`. Dette skriptet skal
  flytte eplet til et tilfeldig sted på skjermen, og deretter lage en klon. Men
  vi vil være litt nøye med at eplet havner i samme "rutenett" som slangen. For
  eksempel, om slangeboksene dine er `10 x 10` kan du bruke noe som dette:

  ```blocks
  gå til x: ((10) * (tilfeldig tall fra (-23) til (23))) y: ((10) * (tilfeldig tall fra (-16) til (16)))
  ```

  Husk at skjermen har koordinater fra `-240` til `240` i x-retning, og `-180`
  til `180` i y-retning. Pass på at eplene dine lander godt innenfor skjermen
  slik at slangen kan spise dem.

- [ ] Nå trenger vi et skript som sender ut slike `Lag eple`-meldinger. Lag et
  skript som starter når det mottar `Nytt spill`. Dette skriptet skal
  `skjule`{.blocklooks} eplet og deretter sende en `Lag eple`-melding.

- [ ] Til slutt lager vi oppførselen for et slikt kloneeple. Lag et nytt skript
  som starter med `når jeg starter som klon`{.blockcontrol}. Dette skriptet må
  `vise`{.blocklooks} eplet, `vente til`{.blockcontrol} det `berører
  slangen`{.blocksensing}, øke `lengden`{.blockdata} på slangen, deretter
  `sende`{.blockevents} en `Lag eple`-melding og til slutt `slette denne
  klonen`{.blockcontrol}.

- [ ] Legg på noen enkle lydeffekter! For eksempel passer lyden `chomp` ganske
  bra når et eple blir spist. Hvilken lyd passer når slangen krasjer?


# Steg 4: Videreutvikling av spillet {.activity}

*Du står helt fritt i hvordan du vil jobbe videre med spillet ditt, men her er
 noen ideer som kan gjøre spillet enda morsommere å spille:*

## Ideer til videreutvikling {.check}

- [ ] Legg til en poeng-teller. Det enkleste er bare å bruke
  `lengde`{.blockdata} som poeng. Vis denne variabelen på skjermen. Høyreklikk
  på den og velg `stor`.

- [ ] La hastigheten øke etterhvert i spillet. Vanligvis gjør vi dette ved å
  forandre hvor mange steg en figur går. Det kan vi ikke gjøre her siden hver
  boks i slangekroppen må henge sammen. I stedet kan du forandre på hvor lenge
  det ventes mellom hver klon som lages.

- [ ] Kanskje du kan videreutvikle hele konseptet, slik at det er mulig å plukke
  opp forskjellige bonusepler underveis. For eksempel kan du ha epler som øker
  lengden på slangen med mer enn 1, epler som lager flere epler, ekstra store
  epler, eller noe helt annet.

- [ ] Det trenger jo ikke bare være ett eple om gangen. Om du for eksempel lager
  tre epler i starten av spillet vil det være litt mindre leting etter eplene og
  spillet kan være litt morsommere. Du kan gjøre dette ved hjelp av kloning,
  bare pass på at ikke klonene lager nye kloner igjen!

- [ ] La eplene flytte seg om det går en viss tid uten at de blir spist. For å
  holde styr på tiden kan du bruke `tid`{.blocksensing}-klossen i
  `Sansning`{.blocksensing}-kategorien.

- [ ] I stedet for at slangen bare kan krasje i seg selv eller i kanten, kan du
  også lage hindringer på selve brettet. Disse kan du for eksempel tegne på
  bakgrunnen i en spesiell farge og deretter undersøke om slangen `berører
  fargen`{.blocksensing}. Du kan til og med ha flere brett med dører mellom.

- [ ] Hva med å lage en to-spiller versjon? Spillerene styrer hver sin slange,
  og samtidig som de konkurrerer om å spise eplene prøver de å sperre hverandre
  inne.

- [ ] Spillet ditt fortjener også en forside og en meny som kan starte spillet.
  Her kan du også la spillerene velge vanskelighetsgrad ved å endre på ting som
  lengde, hastighet, hinder i banen og så videre.

