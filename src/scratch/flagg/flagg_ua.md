---
title: Прапор
level: 3
author: 'Sverre Oskar Konestabo og Geir Arne Hjelle'
translator: 'Анатолій Пилипенко'
language: ua
---


# Вступ {.intro}

У цьому завданні ми розглянемо, як за допомогою математики можна створювати захоплюючі візерунки та анімації. Зокрема, ми намалюємо прапор, який ніби розвівається на вітрі.

![Bilde av Norges flagg som vaier i vind](flagg.png)


# Крок 1: Пройдіться по колу {.activity}

Раніше ми вже бачили кілька способів, як змусити фігури рухатися по колу. Ми відсунули фігуру від центру і використали `слідувати за [вказівник v]`{.b} для переміщення фігури по колу.

У цьому завданні ми будемо використовувати дві функції, синус і косинус, щоб краще контролювати, як відбувається круговий рух. Можливо, ви ще не чули про синус і косинус? Це числа, які показують, якою є довжина сторін прямокутного трикутника відносно одна до одної. На прикладі нижче, косинус, `cos(кут)`, показує, якою є довжина горизонтальної лінії відносно похилої лінії.

![Bilde av sammenhengen mellom vinkel, sinus og cosinus](sinus_cosinus_ua.png)

Давайте подивимося, як ми можемо використовувати це для малювання кіл!

## Контрольний список {.check}

- [ ] Розпочати новий проект.

- [ ] Напишіть наступний сценарій для персонажа кота:

  ```blocks
  коли @greenFlag натиснуто
  стиль обертання [не обертати v]
  завжди
      задати x ((100) * ([cos v] з (напрям)))
      задати y ((100) * ([sin v] з (напрям)))
      поворот @turnLeft на (5) градусів
  slutt
  ```

## Перевірте проєкт {.flag}

__Натисніть на зелений прапорець.__

- [ ] Що відбувається? Ви розумієте, чому фігурка кота рухається по колу?

  Число `100` показує, якого розміру має бути коло (це довжина похилої лінії на малюнку вище). Спробуйте змінити число (в     обох місцях) і подивіться, що станеться.

- [ ] Що станеться, якщо замість `100` використати різні числа в цих двох місцях?

- [ ] Як зміниться рух кота, якщо змінити число 5 у
  `поворот @turnLeft на (5) градусів`{.b}? Не соромтеся пробувати і з від'ємними числами!

## Напрямок кругового руху {.tip}

Ви можете помітити, що кіт рухається в напрямку, протилежному напрямку стрілки на `поворот @turnLeft на (5) градусів`{.b} Це тому, що Scratch вимірює кути у протилежному напрямку від того, що прийнято в математиці (і який ми намалювали вище).

# Крок 2: Перемістіть коло {.activity}

Поки що ми просто намалювали коло в центрі екрана. Спробуймо його перемістити!

## Контрольний список {.check}

- [ ] Оскільки ми вже рухаємо фігуру по колу, ми не можемо використовувати блок `перемістити в x: () y: ()`{.b} для переміщення всього кола. Замість цього ми будемо використовувати змінні. Створіть дві змінні з іменами `(центрX)`{.b} та `(центрY)`{.b} і яка застосовується _Тільки для цього спрайту_.

- [ ] Тепер ми можемо перемістити коло, встановивши змінні `(центрX)`{.b} та
  `(центрY)`{.b}:

  ```blocks
  коли @greenFlag натиснуто
  стиль обертання [не обертати v]
  надати [центрX v] значення [-100]
  надати [центрY v] значення [50]
  завжди
      задати x ((центрX) + ((100) * ([cos v] з (напрям)))
      задати y ((центрY) + ((100) * ([sin v] з (напрям)))
      поворот @turnLeft на (5) градусів
  slutt
  ```

## Перевірте проєкт {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи рухається коло до нового центру?

## Спробуйте самі. {.challenge}

- [ ] Додайте нову змінну, `(радіус)`{.b}, яка також застосовується _Тільки для цього спрайту_.
  Чи можна за допомогою цього контролювати розмір кола?
  Тобто, `(радіус)`{.b} повинен показувати довжину похилої лінії на малюнку який був на початку завдання.

  Вам потрібен блок `надати [радіус v] значення []`{.b} на додаток до використання
  `(радіус)`{.b} у двох місцях вашого коду.


# Крок 3: Танцювальні диски {.activity}

Тепер ми спробуємо змусити багато фігур обертатися по колу одночасно.

## Контрольний список {.check}

- [ ] Намалюйте новий костюм для свого персонажа. За допомогою векторної графіки намалюйте коло (диск), заповнене червоним    кольором. Він може бути досить маленьким, наприклад, `20 x 20` пікселів.

  ![Bilde av en liten rød fyllt disk i Scratch](rod_disk_ua.png)

- [ ] Ми можемо створити багато червоних дисків, дублюючі один диск. Розділіть свій код на дві частини і змініть його таким   чином:

  ```blocks
  коли @greenFlag натиснуто
  повторити (99) 
      надати [центрX v] значення (випадкове від (-150) до (150))
      надати [центрY v] значення (випадкове від (-100) до (100))
      надати [радіус v] значення [50]
      створити клон з [мене v]
  slutt

  коли я починаю як клон
  завжди
      задати x ((центрX) + ((радіус) * ([cos v] з (напрям)))
      задати y ((центрY) + ((радіус) * ([sin v] з (напрям)))
      поворот @turnLeft на (5) градусів
  slutt
  ```

- [ ] Якщо ви запустите програму зараз, то побачите 99 дисків, що танцюють (і 1, що стоїть на місці) по екрану в чудовому     хаосі!

  Хаос насправді виникає через те, що Scratch потребує певного часу для запуску кожного клону. Таким чином ми можемо          створити менш хаотичний танець:

  Змінемо `коли я починаю як клон`{.b} на `коли я отримую  [танець v]`{.b}, і додайте
  `оповістити [танець v]`{.b} після `повторити (99)`{.b}.

  Якщо ви запустите програму ще раз, то побачите, що всі диски танцюють в такт. Який вам подобається найбільше?

# Крок 4: Підняття прапора {.activity}

Давайте подивимося, як можна перетворити цей хаотичний танець на щось схоже на триколірний прапор.

## Контрольний список {.check}

- [ ] На попередньому кроці ми клонували диски у випадкові місця. Тепер ми розкладемо їх більш впорядковано. Перепишіть скрипт, який розкладає диски таким чином:

  ```blocks
  коли @greenFlag натиснуто
  показати
  надати [радіус v] значення [25]
  надати [центрX v] значення [-160]
  повторити (19) 
      надати [центрY v] значення [-100]
      повторити (14) 
          створити клон з [мене v]
          змінити [центрY v] на (16)
      slutt
      змінити [центрX v] на (16)
  slutt
  оповістити [майоріти v]
  сховати
  ```

- [ ] Тоді нехай сценарій `майоріти` буде тим самим, який був у сценарії танець:

  ```blocks
  коли я отримую [майоріти v]
  завжди
      задати x ((центрX) + ((радіус) * ([cos v] з (напрям)))
      задати y ((центрY) + ((радіус) * ([sin v] з (напрям)))
      поворот @turnLeft на (5) градусів
  slutt
  ```

- [ ] Запустіть програму. Тепер ви побачите прапор, що складається з багатьох червоних дисків, які рухаються по колу. Але      ось найцікавіше: Ми можемо змусити червоні диски рухатися трохи не синхронно!


  Додайте блок `поворот @turnRight на (1) градусів`{.b} після блоку `створити клон з [мене
  v]`{.b}, і спробуйте свою програму ще раз. Що сталося?


# Steg 5: Det norske flagget {.activity}

Nå skal vi se hvordan vi kan tegne flagget i forskjellige farger.

## Sjekkliste {.check}

- [ ] Tegn først to nye drakter, begge kopier av den røde disken. Den første
  skal være en hvit disk mens den andre skal være en blå disk. Gi de tre
  diskfigurene dine navnene `r`, `h` og `b` slik at navnet er første bokstaven i
  fargen på disken: `r`ød, `h`vit og `b`lå.

  ![Bilde av en rød, hvit og blå disk i Scratch](tre_disker.png)

- [ ] Vi skal nå bruke en ny variabel `(flagg)`{.b} som beskriver fargene i
  flagget. Lag variabelen _for alle figurer_ og legg deretter til koden:

  ```blocks
  når @greenFlag klikkes
  sett [flagg v] til [rrrrrhbbhrrrrr]
  ```

  Bokstavene `rrrrrhbbhrrrrr` beskriver at vi først vil ha 5 røde disker,
  deretter 1 hvit, 2 blå, 1 hvit og 5 røde disker.

- [ ] For å kunne bruke den nye `(flagg)`{.b}-variabelen må også hver disk vite
  hvilket nummer den har. Lag en ny variabel `(nummer)`{.b} som gjelder kun _for
  denne figuren_.

- [ ] Legg til `sett [nummer v] til [1]`{.b} rett under `vis`{.b} og `endre
  [nummer v] med (1)`{.b} rett under `lag klon av [meg v]`{.b}-klossen.

- [ ] Til slutt skal vi endre drakt på diskene. Legg til

  ```blocks
  bytt drakt til (bokstav (nummer) i (flagg))
  ```

  øverst i `gjenta for alltid`{.blockcontrol}-løkken i `flagre`-skriptet.

- [ ] Kjør programmet ditt. Den venstre delen av flagget ditt skal nå ha fått
  fargene til det norske flagget. For å fargelegge hele flagget må vi gi mange
  flere bokstaver til `(flagg)`{.b}-variabelen. Hele det norske flagget vil ha
  bokstavene

  ```
  rrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrr
  hhhhhhbbhhhhhhbbbbbbbbbbbbbbbbbbbbbbbbbbbbhhhhhhbbhhhhhhrrrrrhbbhrrrrr
  rrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrr
  rrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrrrrrrrhbbhrrrrr
  ```

- [ ] En enklere måte å tegne flagg på er å si at vi vil at mønsteret skal
  gjenta seg selv. Da trenger vi ikke skrive en bokstav for hver disk. Til dette
  kan vi bruke `() mod ()`{.b}-klossen.

  Bytt `(bokstav (nummer) i (flagg))`{.b} med `(bokstav ((nummer) mod (lengden
  av (flagg))) i (flagg))`{.b} i `bytt drakt til [ v]`{.b}-klossen. Om du prøver
  programmet igjen vil du se at flaggmønsteret gjentas (sett for eksempel
  `(flagg)`{.b} til `rhb` for å se dette).

## Prøv selv {.challenge}

- [ ] Tegn egne flagg. Om du trenger flere farger er det bare å lage flere
  drakter. Pass på at hver drakt har en bokstav eller tall som navn.

- [ ] Du kan også leke litt med de forskjellige tallene for en litt annerledes
  animasjon. Prøv for eksempel med `snu @turnRight (25) grader`{.b} i klossen etter
  `lag klon av [meg v]`{.b}.

- [ ] Du kan endre utseendet på flagget underveis. For eksempel om du bruker en
  `når [ v] trykkes`{.b}-kloss kan du endre verdien av `(flagg)`{.b} basert på
  hvilke taster som trykkes. Fargene i flagget vil da også oppdatere seg.
