---
title: Spøkelsesjakten
level: 1
author: 'Oversatt fra [Code Club UK](//codeclub.org.uk)'
translator: 'Malin Bruland'
language: ua
---


# Вступ {.intro}

Цей проект створено за мотивами ярмаркової гри __Вдарити крота__, де
один збиває кротів назад у їхні нори. У нашій грі так і є
привиди, які зникають, коли ми натискаємо на них. Мета - натиснути
видалити якомога більше протягом 30 секунд.

![Illustrasjon av et ferdig spøkelsejakt spill](spokelsesjakten.png)

# Крок 1: створіть літаючого привида {.activity}

## Контрольний список {.check}

- [ ] Розпочати новий проект Scratch.

- [ ] Видаліть фігуру кота, клацнувши її правою кнопкою миші та вибравши «видалити»

- [ ] Змінити фон на `Outdoor/Woods`.

- [ ] Щоб додати привида, натисніть
 Кнопка ![Вибрати форму з бібліотеки](../images/get-from-library.png).
 Виберіть персонажа `Fantasy/Ghost'.

- [ ] Дайте привиду ім’я `ghost1`.

Тепер ви __створите змінну__, яка контролює швидкість руху привида
себе. Пізніше ми можемо використати це, щоб змінити швидкість під час гри
в процесі.

- [ ] У розділі `Код`{.blocklightgrey} натисніть `Змінні`{.blockdata}, а потім
 `Створити змінну'. Викличте змінну `швидкість'. Перекресліть там, де написано
 «Для цієї фігури».

- [ ] На сцені змінна має називатися `ghost1: speed`. Якби тільки
 називається `швидкість', тому видаліть його та додайте знову.

- [ ] Видаліть відступ біля змінної, щоб вона не з’являлася на
 сцена: ![Зображення того, як не показувати змінну швидкості](speed.png)

- [ ] Ми хочемо, щоб привид рухався, коли починається гра. Ми робимо
 створивши такий сценарій:

    ``` блоки
    коли клацнути зелений прапорець
    встановіть [швидкість v] на [5]
    повторювати вічно
        ходьба (швидкість) крок
    кінець
    ```

FIXME Sjekk om blokk-programmering virker

    ```blocks
    når grønt flagg klikkes
    sett [hastighet v] til [5]
    gjenta for alltid
        gå (hastighet) steg
    slutt
    ```

## Перевірте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Привид літає по екрану?

- [ ] Чому привид застрягає, коли торкається краю екрана?

## Контрольний список {.check}

- [ ] Щоб привид не застряг на краю, ми повинні змусити його повертатися
 коли він потрапляє в нього. Це робиться шляхом додавання блоку `bounce
 назад на краю`{.blockmotion}. Тоді сценарій виглядає так:

    ``` блоки
    коли клацнути зелений прапорець
    встановіть [швидкість v] на [5]
    повторювати вічно
        ходьба (швидкість) крок
        відскочити на краю
    кінець
    ```

FIXME Sjekk om blokken virker

  ```blocks
  når grønt flagg klikkes
  sett [hastighet v] til [5]
  gjenta for alltid
      gå (hastighet) steg
      sprett tilbake ved kanten
  slutt
  ```

- [ ] Щоб привид не перевернувся догори дном, клацніть поле «Напрямок» над фігурою.
 Виберіть середній режим обертання («вперед-назад»).

  ![venstre/høyre](../bilder/rotasjonsmate-hv.png)

## Перевірте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Привид літає туди-сюди?

- [ ] Привид летить у правильному напрямку?

## Що спробувати {.challenge}

- [ ] __Змініть змінну швидкості__, щоб привид рухався швидше або
 повільніше.

- [ ] Як ми можемо змусити привида __літати швидше, ніж далі
 літати?__ (Це досить важко, тому не хвилюйтеся, якщо ви цього не зробите
 зрозуміти як. Попутно ви отримаєте більше підказок.)


# Крок 2: змусьте привида з’являтися та зникати {.activity}

* Щоб зробити гру веселішою, ми зробимо так, щоб привид з'явився і
 зникнути.*

## Контрольний список {.check}

- [ ] Ми створюємо новий скрипт, який буде працювати одночасно зі скриптом, який
 рухається привид. Новий сценарій __показує привид
 випадковий період__ і __тоді ховає його у випадковому
 період__. Це повинно відбуватися знову і знову, поки гра не закінчиться
 кінець. Як створити сценарій:

    ``` блоки
    коли клацнути зелений прапорець
    повторювати вічно
        шоу
        зачекайте (випадкове число від (3) до (5)) секунд
        приховати
        зачекайте (випадкове число від (2) до (4)) секунд
     кінець
 ```

FIXME Sjekk blokk

  ```blocks
  når grønt flagg klikkes
  gjenta for alltid
      vis
      vent (tilfeldig tall fra (3) til (5)) sekunder
      skjul
      vent (tilfeldig tall fra (2) til (4)) sekunder
  slutt
  ```

## Перевірте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи рухається привид з боку в бік?

- [ ] Він зникає і знову з’являється абсолютно випадково?

## Що спробувати {.challenge}

- [ ] Спробуйте __змінити числа в коді__, де написано «випадкове число з _
 до _`{.blockoperators}. Що станеться, якщо вибрати дуже великий
 чи маленькі цифри? (Це може дати вам ще одну підказку щодо того, як ми
 має змусити привида рухатися швидше, чим довше ви граєте.)


# Крок 3: Викличте привида одним клацанням! {.activity}

* Щоб зробити цю гру правильною, нам потрібно дати гравцеві щось робити
 зробити - наприклад, клацанням геть привида. Коли це станеться, ми це зробимо
 також, щоб був стильний магічний звук!*

## Контрольний список {.check}

- [ ] Перейдіть на вкладку `Звуки`{.blocklightgrey}, додайте новий звук за допомогою
 унизу ліворуч. Знайдіть звук «Fairydust» у полі пошуку та
 виберіть його. Тепер він доступний для скриптів у привиді.

- [ ] Створіть сценарій, який змушує __привид зникати__, коли він стає
 натиснув на:

    ``` блоки
     коли клацнути цю фігуру
     приховати
     початковий звук [fairydust v]
     ```

FIXME Sjekk blokken

  ```blocks
  når denne figuren klikkes
  skjul
  start lyden [fairydust v]
  ```

## Перевірте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи зникає привид із чарівним звуком, коли ви натискаєте його?

## Що спробувати {.challenge}

- [ ] Запитайте дорослих, чи можете ви записати власний звук. Ви можете використовувати це в
 місце чарівного звуку.


# Крок 4: Додайте час і бали {.activity}

*Нам потрібно викликати привида, тож тепер ми хочемо підкреслити
 the! Ми також хочемо часові рамки ist, так що мова йде про те, щоб отримати
 якомога більше очок за цей час. Ми вирішуємо обидва за допомогою
 змінні.*

 ===

## Sjekkliste {.check}

- [ ] Lag en ny variabel som heter `Poeng`{.blockdata}. Denne skal
  gjelde `For alle figurer`. Legg til en ny kloss som gjør at
  `Poeng`{.blockdata}-variabelen økes med 1 poeng for hver gang
  spilleren klikker på spøkelset.

  ```blocks
  når denne figuren klikkes
  skjul
  start lyden [fairydust v]
  endre [Poeng v] med (1)
  ```

- [ ] Klikk på `Scene` og lag en ny variabel som heter `Tid`. La variablen
  vises på skjermen.

- [ ] Lag et nytt skript som setter `Tid`{.blockdata}-variabelen til
  __30__ og `Poeng`-variablen til __0__ når det grønne flagget
  klikkes.

- [ ] Bruk så en `gjenta til`{.blockcontrol}-kloss for å vente i __1__
  sekund og deretter redusere tiden med 1 sekund. Denne skal kjøre
  fram til tiden er ute. Til slutt stopper du hele spillet med en
  `stopp alle`{.blockcontrol}-kloss.

  ```blocks
  Når grønt flagg klikkes
  sett [Tid v] til [30]
  sett [Poeng v] til [0]
  gjenta til <(tid) = [0]>
      vent (1) sekunder
      endre [Tid v] med (-1)
  slutt
  stopp [alle v] :: control
  ```

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

## Ting å prøve {.challenge}

- [ ] Hvordan kan du få spøkelset til å gå fortere etter at spillet er i
  gang?

## Lagre prosjektet {.save}

- [ ] __Bra jobba!__ Nå er du egentlig ferdig med spillet, men prøv deg
  gjerne på neste steg også.

## En ekstra utfordring: Flere spøkelser! {.challenge}

*Hvis ett spøkelse er bra, må vel flere være enda bedre! La oss ha tre
 spøkelser flyvende rundt!*

- [ ] __Lag flere spøkelser__ ved å høyreklikke på det du allerede har, og så
  kopiere dette.

- [ ] __La spøkelsene få ulik størrelse__. Dette gjør du ved å velge
  et spøkelse, trykke `Størrelse`-boksen og endre tallet litt.

- [ ] Du kan også __endre spøkelsenes flyvefart__. Dette gjøres i
  `hastighet`{.blockdata}-variabelen i det øverste skriptet for hver enkelt
  figur.

- [ ] Til slutt kan du __spre spøkelsene__ litt bedre ut på scenen. Dette gjør
  du ved å klikke og dra figurene rundt i selve skjermbildet.

## Test prosjektet {.flag}

__Klikk på det grønne flagget.__

- [ ] Har du nå tre spøkelser som flyr fra side til side?

- [ ] Som plutselig forsvinner og dukker opp igjen?

- [ ] Forsvinner de når du klikker på dem?

Gratulerer! Da har du gjort alt riktig!

## Ting å prøve {.challenge}

- [ ] Hvor mange spøkelser synes du spillet fungerer best med? __Legg til
  flere__ og prøv!

- [ ] Klarer du å få spøkelsene til __å se forskjellige ut__? Klikk på
  `Drakter`{.blocklightgrey} og prøv deg frem. Du kan også velge noen av
  klossene under `Utseende`{.blocklooks}.

- [ ] Kan du få spøkelsene til __å bli verdt forskjellige antall poeng?__ Hva
  med å få den minste og raskeste til å gi 10 poeng?

## Lagre prosjektet {.save}

Bra jobba! Nå er du ferdig, og det er på tide med litt seriøs spilling. Husk
også at du kan dele spillet med vennene dine. Det gjør du ved å klikke på `Legg
ut` i toppmenyen.
