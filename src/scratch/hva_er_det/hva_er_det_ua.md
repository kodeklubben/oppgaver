---
title: 'Що це?'
level: 3
author: 'Oversatt fra [Code Club UK](//codeclub.org.uk)'
translator: 'Ольга Паньків'
language: ua
---


# Вступ {.intro}

На дошці з’являється зображення випадкового предмету. Воно спотворене, тож вам потрібно вгадати, що це, натиснувши на одну з опцій під картинкою. Чим швидше ви впізнаєте зображення, тим більше балів отримаєте.

![Illustrasjon av et ferdig hva-er-det spill](hva_er_det.png)


# Крок 1: Додайте нові предмети {.activity}

*Ми хочемо, щоб на дошці з’являлися різні зображення.*

## Контрольний перелік {.check}

- [ ] Розпочніть новий проект Scratch і видаліть фігуру кота.

- [ ] В розділі “Сцена” зайдіть у вкладку “Тло”. Відкрийте бібліотеку з різними варіантами тла, натиснувши на ![Velg en ferdig
  bakgrunn](../bilder/velg-bakgrunn.png) і виберіть `У приміщенні/Chalkboard`.

- [ ] Оберіть довільний спрайт.

- [ ] Розташуйте спрайт в центрі дошки та змініть його розмір, якщо потрібно.

- [ ] Виберіть ще чотири образи для цього спрайту. Можна обирати будь-які інші спрайти, але додавати їх як образи. Для цього виберіть вкладку `Образи` і натисніть на зображення кота в лівому нижньому куті екрану.

- [ ]  Тепер давайте зробимо так, щоб на дошці з’являвся випадковий предмет. Використовуйте цей скрипт.

  ```blocks
  коли grønt flagg натиснуто
  змінити образ на (випадкове від (1) до (5))
  ```

## Протестуйте свій проект {.flag}

__Натисніть на зелений прапорець в Scratch.__

- [ ] Фігура змінюється?

- [ ] Натисніть на прапорець кілька разів. Чи з’являються на дошці зображення спрайту і його нещодавно доданих  образів? Чудово.

Одне і те ж зображення може з’явиться кілька разів поспіль. Це цілком нормально, оскільки кожного разу воно вибирається випадково.


# Крок 2: Спотворюємо зображення {.activity}

*Тепер давайте спотворимо фігуру, що з’явиться на дошці, щоб важче було вгадати, що це таке. Потім ми поступово знову зробимо її зрозумілішою.*

Для того, щоб контролювати ступінь спотворення, ми будемо використовувати змінну `оцінка`{.blockdata} Якщо оцінка висока, зображення буде сильно спотвореним. Зі зменшенням оцінки,  спотворення також буде зменшуватися. Таким чином, оцінка функціонує як своєрідний таймер.

## Контрольний перелік {.check}

- [ ] Оберіть категорію `Змінні`{.blockdata}  в якій створіть змінну з назвою
  `оцінка`{.blockdata}. При створенні, підтвердіть, що змінна застосовується `для всіх спрайтів`.

- [ ] Змініть скрипт наступним чином:

  ```blocks
  коли grønt flagg натиснуто
  змінити образ на (випадкове від (1) до (5))
  надати [оцінка v] значення [110]
  повторити до <(оцінка) = [0]>
      змінити [оцінка v] на (-10)
      встановити ефект [пікселями v] в (оцінка)
      встановити ефект [колір v] в (оцінка)
      чекати (1) секунд
  slutt
  ```

## Протестуйте свій проект {.flag}

__Натисніть на зелений прапорець в Scratch.__

- [ ] Чи з’являється випадкове та спотворене зображення?

- [ ] Зображення поступово стає чіткішим?

- [ ] Чи зменшується оцінка, коли зображення стає чіткішим?

- [ ] Чи стає зображення повністю чітким при оцінці 0?

- [ ] Ви отримуєте новий предмет на дошці, коли знову натискаєте зелений прапорець?

## Поекспериментуйте {.challenge}

- [ ] Спробуйте змінити початкове значення оцінки, а також розмір кроку, на який вона змінюється під час проходження кожного циклу. Як це впливає на вигляд зображення? Стає важче чи легше побачити, що зображено на малюнку?

- [ ] Спробуйте різні ефекти з блоку __встановити ефект__. Як вони впливають на зміну зображення?


# Крок 3: Дозвольте гравцю вгадати предмет {.activity}

Отже, наше випадкове зображення поступово стає чіткішим, а оцінка падає. Але як грати в цю гру? Ми додамо варіанти зображень, на які гравець зможе натиснути. Якщо вибір правильний, гру виграно. Якщо натиснути неправильно, зображення зникає і гра продовжується.

Спочатку нам потрібно знати, яка відповідь є правильною.

## Контрольний перелік {.check}

- [ ] Створіть нову змінну та назвіть її `відповідь`{.blockdata}. Переконайтеся, що змінна застосовується для всіх спрайтів. Видаліть галочку, щоб змінну не було видно в полі гри.

- [ ] Змініть скрипт, щоб він відслідковував правильну відповідь. Після того, як програма визначає, який саме образ буде показано, додайте блок, що присвоїть змінній `відповідь`{.blockdata}`його номер:

  ```blocks
  коли grønt flagg натиснуто
  змінити образ на (випадкове від (1) до (5))
  надати [відповідь v] значення (образ [номер v])
  надати [оцінка v] значення [110]
  повторити до <(оцінка) = [0]>
      змінити [оцінка v] на (-10)
      встановити ефект [пікселями v] в (оцінка)
      встановити ефект [колір v] в (оцінка)
      чекати (1) секунд
  slutt
  ```

Тепер додаймо більше зображень, з яких гравець зможе обирати.

- [ ] Назвіть ваш спрайт `питання`.

- [ ] Зробіть копію спрайту, натиснувши на нього правою кнопкою миші. Перетягніть новий спрайт у лівий кут сцени.

- [ ] Змініть назву новоствореного спрайту на `відповідь1`. 

- [ ] Видаліть його скрипт (у вкладці `Код`) і всі його образи, крім першого.

- [ ] Повторіть останні три кроки ще раз (назвіть наступну копію `відповідь2`), помістіть `відповідь2` поруч із `відповідь1`, видаліть скрипт для цього спрайту і всі образи, крім другого.

- [ ] Повторіть ці кроки ще три рази, щоб створити спрайти `відповідь3`, `відповідь4` і `відповідь5`.

  Тепер в ​​нижній частині сцени у вас є п’ять зображень з образами, що може отримати головний спрайт. Жоден спрайт-відповідь не повинен мати скрипту.

- [ ] Тепер нам потрібно змусити фігури реагувати, коли на них натискають. Що саме станеться, залежить від того, правильно чи неправильно натиснув гравець. Додайте такий скрипт до спрайту `відповідь1`:

  ```blocks
  коли спрайт натиснуто
  якщо <(відповідь) = [1] то>
      оповістити [Ти виграв v]
  інакше
      сховати
  slutt
  ```

- [ ] Перетягніть скрипт до інших спрайтів-відповідей, змінюючи `відповідь` на 2, 3, 4 чи 5, відповідно до назви спрайту.

- [ ] Тепер ми створимо скрипт, який сповіщатиме гравця про виграш. Натисніть на спрайт `питання` і додайте цей скрипт:

  ```blocks
  коли я отримую [Ти виграв v]
  говорити (з'єднати [Вітаємо! Твій бал: ] (оцінка))
  ```

## Протестуйте свій проект {.flag}

__Натисніть на зелений прапорець в Scratch.__

Під час тестування, правильну відповідь можна побачити на зображенні з назвою `питання` під сценою.

- [ ] Що відбувається, коли ви натискаєте на правильну відповідь?

- [ ] Що відбувається, коли ви натиснете на неправильну відповідь?

- [ ] Що стається з неправильною відповіддю, коли ви починаєте нову гру?

## Контрольний перелік {.check}

Тест показав нам дві проблеми: по-перше, зображення, на які клацнули неправильно, не повертаються, коли починається нова гра. По-друге, рахунок продовжує знижуватися навіть після того, як гравець натиснув на правильну відповідь.

- [ ] Щоб вирішити першу проблему, ми можемо додати наступний скрипт для кожної з п’яти можливих відповідей:

  ```blocks
  коли grønt flagg натиснуто
  показати
  ```

Для вирішення другої проблеми, нам потрібно зупинити цикл `повторити до`{.blockcontrol}, що виконує спрайт `питання`, коли гравець натискає на правильну відповідь. Для цього ми можемо використати нову змінну. Назвемо її `виграш`{.blockdata} , і помістимо в блок `надати значення`{.blockdata} що присвоює їй значення 0, коли гра починається. Також в другу частину коду для спрайту “питання” додамо блок, що присвоює виграшу значення 1, коли гру виграно.
Перегляньте скрипти нижче.

- [ ] Нам потрібно зупинити повтор циклу `повторити до`{.blockcontrol}, коли оцінка стане 0 або `виграш`{.blockdata} дорівнюватиме 1.

- [ ] Нарешті, ми додаємо блок `очистити графічні ефекти`{.blocklooks}, щоб показати неспотворене зображення, коли гравець вгадав його. Сценарії для спрайту `питання` тепер мають виглядати так:

  ```blocks
  коли grønt flagg натиснуто
  змінити образ на (випадкове від (1) до (5))
  надати [відповідь v] значення (образ [номер v])
  надати [оцінка v] значення [110]
  надати [виграш v] значення [0]
  повторити до <<(оцінка) = [0]> або <(виграш) = [1]>>
      змінити [оцінка v] на (-10)
      встановити ефект [пікселями v] в (оцінка)
      встановити ефект [колір v] в (оцінка)
      чекати (1) секунд
  slutt

  коли я отримую [Ти виграв v]
  надати [виграш v] значення [1]
  очистити графічні ефекти
  говорити (з'єднати [Вітаємо! Твій бал:] (оцінка))
  ```

## Збережіть проект {.save}

__Gratulerer! Du er nå ferdig med spillet.__

Men det finnes mange flere ting du kan gjøre med spillet. Prøv deg gjerne på
utfordringene nedenfor!

## Utfordring 1: Gjør spillet enklere eller vanskeligere {.challenge}

Endre vanskelighetsgrad for spillet.

* Forsøk å endre hvor lenge bildet vises frem og hvor raskt poengsummen minker.

* Forsøk å endre forvrengingen av bildet.

* Forsøk å gjøre figurene likere hverandre eller mer forskjellig. Husk også å
  forandre svarfigurenes drakter.

## Utfordring 2: Forvreng bildet ulikt fra gang til gang {.challenge}

For øyeblikket bruker spillet samme forvrengingsalgoritme hele tiden. Men i steg
2 prøvde du kanskje ut noen forskjellige alternativer. Prøv nå om du kan finne
noen flere forvrenginger som du synes fungerer like bra som `farge` og
`piksler`.

Endre spillet slik at hvert spill bruker forskjellige forvrengninger i `gjenta
til`{.blockcontrol}-løkken.

__Hint:__ Forsøk å opprette en ny variabel som du kaller `forvrenging`. Sett
denne til en tilfeldig verdi i starten av spillet. Bruk så
`hvis`{.blockcontrol}-klosser i `gjenta til`{.blockcontrol}-løkken for å velge
ut en forvrenging til hvert spill.

## Utfordring 3: La hvert spill ha flere runder {.challenge}

For øyeblikket er hvert spill uavhengig av andre. Prøv om du kan legge til flere
runder slik at man får gjette på for eksempel tre ting og kan vinne inntil 300
poeng.

__Hint:__ Du vil trenge en ekstra variabel for å lagre den totale poengsummen.
Du må også ha en løkke som går rundt for hver runde.

## Utfordring 4: Øk vanskelighetsgraden gradvis {.challenge}

Gjør nå spillet vanskeligere og vanskeligere for hver runde.

Kanskje hver runde også skal gi ulikt antall poeng? Bør spilleren også få ekstra
mange poeng for å gjette kjapt i de vanskeligste rundene?

__Hint:__ Hvordan kan du vite hvilken runde du er i? Hvordan kan du bruke det
til å endre vanskelighetsgraden og poengsummen?

## Utfordring 5: Fortsett til spilleren gjør feil {.challenge}

I stedet for et bestemt antall runder kan du la spillet gå til det blir klikket
på feil svar. Dette fungerer nok best dersom man også øker vanskelighetsgraden
utover i spillet.

## Utfordring 6: Tilpass spillet til hvor flink spilleren er {.challenge}

I stedet for å gjøre det stadig vanskeligere kan vi tilpasse vanskelighetsgraden
til spillernes dyktighet. Hvis de raskt gjetter riktig ting, kan den neste
runden gjøres vanskeligere. Hvis de klikker feil eller gjetter sakte, kan neste
runde gjøres enklere.

Dette fungerer bare hvis du ikke samler opp poengsummen fra runde til runde.

## Utfordring 7: Hold styr på rekorden {.challenge}

Finn en måte å lagre den høyeste poengsummen på. Klarer du også å lagre navnet
til spilleren, og få spillet til å si hvem som har rekorden?

## Utfordring 8: Gi en straff for galt svar {.challenge}

Slik spillet er nå kan man bare klikke som en gal på alle svarene, og dermed
raskt finne riktig svar. Det kan derfor være en god idé å trekke fra poeng hver
gang spilleren klikker på feil figur.

Gjør dette spillet bedre?

## Lagre prosjektet{.save}

__Veldig bra! Nå er du ferdig og kan spille det nye spillet du har laget!__

Ikke glem å dele spillet ditt med venner og familie ved å trykke på `Legg ut` i
menyen!

