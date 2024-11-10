---
title: Астероїди
level: 4
author: 'Geir Arne Hjelle'
translator: 'Анатолій Пилипенко'
language: ua
---


# Вступ {.intro}

Наприкінці 1970-х Atari випустила дві гри, в яких потрібно було керувати космічним кораблем. Першою була "Місячний модуль", але її витіснила "Астероїди", яку Atari випустила кількома місяцями пізніше. Насправді, ігри були настільки схожі, що змогли повторно використати багато технологій. Ми збираємося зробити те ж саме! Отже, перед тим, як розпочати цей проект, вам потрібно буде створити "Місячний модуль". У "Астероїди" ваша мета - захистити свій космічний корабель від астероїдів, розстрілюючи їх на шматки.

![Illustrasjon av et ferdig astroide spill](asteroids_ua.png)


# Огляд проєкту {.activity}

*Більшу частину коду для "Астероїди" ви будете писати самостійно (а дещо ви вже написали). У "Астероїди" ми розглянемо деякі способи повторного використання коду у Scratch.*

## План {.check}

- [ ] Ще один літаючий космічний корабель

- [ ] Космічний корабель вміє стріляти!

- [ ] Обережно, астероїди!

- [ ] .. та інші виклики


# Крок 1: Ще один літаючий космічний корабель {.activity}

*У "Місячний модуль" ми зробили чудовий космічний корабель. Тепер ми побачимо, як ми можемо використовувати той самий космічний корабель у цьому проєкті.*

Ви, мабуть, знаєте, що можете реміксувати чужі Scratch-проєкти. Це дає вам можливість створити власну версію того, що зробили інші, і, зокрема, ви можете повторно використовувати код, написаний іншими раніше.

Давайте розглянемо трюк для повторного використання коду, який ми створили в минулому. Використовуючи `Сховок`, ви можете копіювати фігури та код між різними проєктами. Тому спочатку ми скопіюємо космічний корабель, який ми створили у "Місячний модуль".

## Контрольний список {.check}

- [ ] Відкрийте свій проєкт "Місячний модуль".
Зверніть увагу, що в самому низу екрана написано `Сховок`. Натисніть на нього, і перед вами відкриється трохи більше поле.

- [ ] Перетягніть фігуру космічного корабля до відкритого сховку. Копія вашої фігурки космічного корабля залишиться в сховку.

- [ ] Створіть новий проєкт, вибравши команду `Новий` в меню `Файл`. Видаліть символ кота і додайте зоряне тло.

- [ ] Тепер ви можете перетягнути репліку космічного корабля з сховку у вікно персонажа нового проєкту.

  ![Bilde av hvordan dra romskip-kopien fra ryggsekken i Scratch](ryggsekk_ua.png)

  Тепер ви побачите, що всі костюми, всі змінні і всі скрипти для космічного корабля були скопійовані. Ви можете трохи навести лад, видаливши скрипти, які не мають нічого спільного з керуванням космічним кораблем, наприклад, якщо у вас є скрипт `Перевірте посадку`, то він нам не потрібен у цій грі.

- [ ] Розмістіть на сцені сценарій, який надсилає повідомлення космічному кораблю про початок польоту після натискання на зелений прапорець. Спробуйте свою гру. Чи зможете ви керувати космічним кораблем?

- [ ] Ми збираємося внести невеликі зміни в поведінку космічного апарату. Астероїди знаходяться далеко в космосі, де немає помітної гравітації. Тому видаліть блок, який моделює гравітацію у вашому циклі `завжди`{.blockcontrol},
`замінити [швидкістьY v] на (-0.01)`{.b}.

- [ ] Ми також робимо дещо більшу зміну в грі. Ми хочемо, щоб космос відчувався трохи великим і захаращеним, тому, коли космічний корабель виходить з екрану з одного боку, він з'являється з іншого боку екрану.

  Ми робимо це за допомогою досить простих тестів `якщо`{.blockcontrol}. Потрібно пам'ятати, що координати `x` на екрані знаходяться в діапазоні від `-240` до `240`, а координати
  `y` від `-180` до `180`. Оскільки Scratch стежить за тим, щоб фігури не виходили повністю за межі екрану, ми зсуваємо їх трохи всередину краю екрану:

  ```blocks
  коли я отримую [Нова гра v]
  завжди
      якщо <(значення x) < [-235]> то
          змінити x на (470)
      slutt
      якщо <(значення x) > [235]> то
          змінити x на (-470)
      slutt
      якщо <(значення y) < [-175]> то
          змінити y на (350)
      slutt
      якщо <(значення y) > [175]> то
          змінити y на (-350)
      slutt
  slutt
  ```


# Крок 2: Космічний апарат може стріляти {.activity}

*Наш космічний корабель незабаром влетить в астероїдний рій, тому нам потрібно встановити ракети, які зможуть підірвати астероїди.*

## Контрольний список {.check}

- [ ] Створіть нового персонажа, якого ви назвете `Постріл`. Ви можете намалювати його самостійно. Ви також можете знайти фігури у вигляді куль, які можна використати як кулі. Використовуйте блок `задати розмір`{.blocklooks}, щоб зробити фігуру потрібного розміру. Також додайте блок `сховати`{.blocklooks}, щоб приховати фігуру.

- [ ] Ми хочемо використовувати клони, щоб зробити більше пострілів. Спочатку нам потрібен код, який створює новий клон пострілу при натисканні клавіші пробілу:

  Створіть скрипт для `Постріл` персонажа, який запускається на повідомленні `Нова гра`. Скрипт може складатися з `завжди`{.blockcontrol} циклу, де перевіряється, чи натиснута клавіша пробілу. Якщо потрібно здійснити постріл, спочатку перемістіть постріл до `перейти до`{.blockmotion} місячного модуля, а потім наведіть його в тому ж напрямку, що й місячний модуль. Останнє можна зробити за допомогою комбінації блоків `повернути в напрямку`{.blockmotion}, `напрям з Місячний модуль`{.blocksensing}. Нарешті, `створити клон з мене`{.blockcontrol}.

- [ ] Щоб переконатися, що при кожному натисканні клавіші пробілу надсилається лише одне повідомлення, ми можемо запустити тест `якщо`{.blockcontrol}, дочекавшись, поки клавішу пробілу знову не буде відпущено. Цей трюк виглядає приблизно так:

  ```blocks
  якщо <клавішу [пропуск v] натиснуто?> то
      чекати поки <не <клавішу [пропуск v] натиснуто?>>
      ...
  slutt
  ```

- [ ] Nå skal vi kode oppførselen til skuddet etter at det er avfyrt. Det kan
  være ganske enkelt. Når skuddfiguren `starter som klon`{.blockcontrol} må den
  `vises`{.blocklooks}, og deretter kan den flyttes i en løkke før den til slutt
  slettes. Eksperimenter med hastigheten og rekkevidden på skuddet ved å endre
  på hvor mange ganger løkka gjentas og hvor mange steg figuren går inne i
  løkka.

- [ ] Til slutt vil vi at også skuddene skal kunne forsvinne ut på den ene siden
  av skjermen og dukke opp igjen på den andre. Til dette vil vi bruke omtrent
  samme kode for romskipet.

  For å kopiere skript mellom figurer kan du bruke ryggsekken på samme måte som
  tidligere. En litt raskere metode er å bare dra skriptet du vil kopiere til
  den figuren du vil kopiere til.

  Kopier koden for å *warp'e* rundt skjermen fra romskipet til skudd-figuren.

- [ ] Vi kan nesten bruke denne koden som den er. Den eneste endringen vi
  trenger å gjøre er at den skal starte på `når jeg starter som klon`{.b} i
  stedet for på `når jeg mottar [Nytt spill v]`{.b}, siden denne oppførselen
  skal gjelde for alle skuddklonene.

- [ ] Prøv spillet ditt. Nå skal du kunne fly rundt i verdensrommet mens du
  skyter.


# Steg 3: Pass deg for asteroidene {.activity}

*Da er det på tide å lage en asteroidesverm. Noe av det som er kult med
 Asteroids er at asteroidene blir skutt i småbiter når de treffes, og man må
 fortsatt passe seg for og skyte disse mindre asteroidene. Vi vil kode dette ved
 å bruke kloner i forskjellige størrelser.*

## Sjekkliste {.check}

- [ ] Lag en asteroidefigur. En måte å gjøre dette på er å tegne en ny figur med
  vektorgrafikk. Start med en enkel firkant, og bruk deretter `Bøy`-verktøyet
  for å legge til flere hjørnepunkter og flytte dem rundt som i figuren under.

  ![Bilde av en astroidefigur i Scratch](flyttpunkt.png)

- [ ] Også for asteroidene vil vi bruke kloner. Lag et skript som
  `skjuler`{.blocklooks} figuren og lager et par asteroide-kloner tilfeldige
  steder på skjermen når det mottar `Nytt spill`-meldingen.

- [ ] Når figuren `starter som klon`{.blockcontrol} vil vi først at den
  `peker`{.blockmotion} i en tilfeldig retning og deretter `vises`{.blocklooks}.
  Videre kan den gå inn i en løkke som `gjentas til`{.blockcontrol} figuren
  `berører romskipet`{.blocksensing}. Inne i løkken lar du først asteroiden `gå
  noen steg`{.blockmotion}. Deretter må du teste om asteroiden `berører et
  skudd`{.blocksensing}. Hvis den gjør det kan du lage asteroiden mindre med en
  kloss som ligner

  ```blocks
  sett størrelse til ((størrelse) / (2)) %
  ```

  `Hvis`{.blockcontrol} `størrelsen`{.blocklooks} fortsatt er større enn for
  eksempel 10 kan du lage et par nye kloner av denne mindre asteroiden. Til
  slutt kan du `slette denne klonen`{.blockcontrol} uansett hva størrelsen er.

- [ ] Legg på en melding eller en `stopp`{.blockcontrol}-kloss slik at spillet
  kan avsluttes etter at `gjenta til`{.blockcontrol}-løkken avsluttes, siden
  romskipet da har krasjet i en asteroide.

- [ ] Også asteroidene skal kunne fly ut av skjermen på en side og dukke opp på
  en annen. Kopier derfor skriptet som fikser dette fra skudd-figuren på samme
  måte som tidligere.

- [ ] Til slutt vil vi også slette skudd-klonene når de treffer asteroidene. Her
  må vi være litt forsiktig så vi ikke sletter skudd-klonene før asteroidene
  merker at de er truffet. Dette kan vi fikse ved å legge inn en ørliten
  forsinkelse. Du kan for eksempel legge inn kode som dette i løkka som flytter
  skudd-figuren:

  ```blocks
  hvis <berører [Asteroide v] ?>
      vent (0.01) sekunder
      slett denne klonen
  slutt
  ```


# Steg 4: Videreutvikling av spillet {.activity}

*Du har nå laget en enkel variant av Asteroids. Men prøv å gjøre spillet
 morsommere ved å videreutvikle det. Du bestemmer selv hvordan du vil jobbe
 videre, men nedenfor er noen ideer som kanskje kan være til inspirasjon?*

## Ideer til videreutvikling {.check}

- [ ] Gi poeng når spilleren treffer en asteroide. Man burde kanskje få flere
  poeng for å treffe de små asteroidene? Det kan du fikse med en utregning
  omtrent som

  ```blocks
  avrund ((100) / (størrelse))
  ```

- [ ] Dersom du plasserer asteroidene helt tilfeldig når et nytt spill starter
  er det ganske sannsynlig at romskipet krasjer i en asteroide allerede før
  spillet har begynt. Det er ikke noe moro. En måte å fikse det på vil være å
  først la asteroideklonen `gå til romskipet`{.blockmotion}, men deretter peke i
  en tilfeldig retning og `gå 100 til 200 steg`{.blockmotion} før det til slutt
  `vises`{.blocklooks}.

- [ ] Spillet ser litt kulere ut om du tegner flere asteroidedrakter, og velger
  en av dem tilfeldig når en klon lages.

- [ ] Dersom man klarer å skyte ned alle asteroidene burde man komme videre til
  et vanskeligere nivå. Kanskje med flere asteroider? Eller med asteroider som
  beveger seg raskere? Eller deler seg i flere deler når de blir skutt?

  For å vite når du kan gå videre til et nytt nivå må du telle hvor mange
  asteroider som flyr rundt. Lag derfor en variabel `Antall
  asteroider`{.blockdata} som du øker med 1 når en asteroide `starter som
  klon`{.blockcontrol}. Deretter må variabelen minke med 1 når klonen slettes.

  Videre bruker du en `Nivå`{.blockdata}-variabel som holder styr på hvilket
  nivå spilleren har kommet til.

- [ ] I det originale Asteroids-spillet dukket det også opp en flyvende
  tallerken (UFO) innimellom. Denne måtte man også passe seg for, men i
  motsetning til asteroidene kunne UFOen skyte tilbake. Prøv å legg til en slik
  UFO i spillet ditt!
