---
title: День народження в Антарктиді
level: 2
author: Керолайн Тандберг
translator: Olexandr
language: ua
---


# Вступ {.intro}

«День народження в Антарктиді» — це інтерактивна анімація, яка розповідає про маленького котика, 
який зник безвісти у свій день народження. На щастя, він зустрічає кількох милих пінгвінів, щоб відсвяткують з ним.

![Картинка з Феліксом, будиночком та двома пінгвінами](bursdag_i_antarktis.png)


# Крок 1: Бродячий кіт {.activity}

*Ми створюємо кота, який зможе самостійно ходити по Антарктиді.*

Поступово ми розповімо цікаву історію про кота, який у свій день народження зустрічає танцюючих пінгвінів. 
Але, як завжди, ми збираємось почати з чогось досить простого, а потім розвивати це.


## Контрольний список {.check}

- [ ] Розпочніть новий проект.  З фігурки кота `Фелікс` і встановіть для нього режим обертання
       ![90 градусів](./burshdag_90_ua.png).

- [ ] Створіть новий фон, клацніть по кнопці ![кнопка зображення](../bilder/velg-bakgrunn.png) у нижній лівій частині екрана. Виберіть
  `winter.svg.`.

- [ ] Також додайте `winter-lights.svg`.

- [ ] Ми починаємо зі скрипту на сцені, який забезпечує показ `зимового` фону на початку анімації.
      Перейдіть на вкладку `Код`{.blocklightgrey} та додайте код

  ```blocks
  коли зелений прапорець натиснуто
  змінити тіло на [winter v]
  ```


- [ ] Тоді ми зможемо змусити кота рухатися.
      Натисніть `Фелікс` і дайте йому наступний скрипт:
  
  ```blocks
  коли зелений прапорець натиснуто 
  перемістити до x: (-100) y: (-50)
  ```
  
  Тут ви можете поексперементувати з числами для `x` та `y`
  доки ви не підбеете значення, яке ви вважаєте підходящтим

  - [ ] Тепер давайте змусимо Фелікса рухатися по екрану.
  Ми перемикаємося між двома його костюмами, щоб виглядало так,
  ніби він ходить. Розширте скрипт Фелікса так:

  ```blocks
  коли зелений прапорець натиснуто
  перемістити в x: (-100) y: (-50)
  повернути в напрямку (100 v)
  повторити до <(x-значення) > [240]>
      перемістити на (10) кроків
      наступний образ
      чекати (0.1) секунди
  кінець
  ```
  Число 100 у блоку `повернути в напрямку`{.blockmotion} змушує Фелікса трохи опускатися, коли він йде по екрану.
  Не соромтеся спробувати деякі інші числа, щоб побачити їхній ефект.

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи блукає Фелікс по екрану?

- [ ] Він зупиняється, коли доходить до краю екрана?

- [ ] Він перезапускається в лівій частині екрана,
      якщо ви знову клацнете зелений прапорець?

### Антарктида {.protip}

Антарктида - це назва території, де розташований Південний полюс. 
Хоча ні люди, ні кішки не живуть постійно в Антарктиді, там багато пінгвінів.

## Контрольний список {.check}

Тепер ми змінимо фон, коли кіт досягне кінця екрана. 
Ми починаємо з чогось простого, але, на жаль, не дуже добре працює.

- [ ] Створіть новий скрипт на сцені.

  ```blocks
  коли зелений прапорець натиснуто
  чекати (3) секунди
  змінити тіло на [winter-lights v]
  ```

- [ ] Також додайте блок, який переміщує Фелікса на дорогу після зміни фону.

  ```blocks
  коли зелений прапорець натиснуто
  перемістити в x: (-100) y: (-50)
  повернути в напрямку (100 v)
  повторити до <(x-posisjon) > [240]>
      перемістити на (10) кроків
      наступний образ
      чекати (0.1) секунд
  кінець
  перемістити в x: (-20) y: (-100)
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи змінюється фон, коли Фелікс досягає кінця екрана?

- [ ] Чи можете ви змінити число в кружечку на `блоці на 3 секунди`{.blockcontrol},
  щоб воно виглядало краще?

# Крок 2. З повідомленнями стає легше {.activity}

*Тепер ми почнемо використовувати повідомлення, щоб все відбувалося таким же чином.*

Ми побачили, що можемо змусити речі відбуватися одночасно, використовуючи блок `чекати__секунд`{.blockcontrol}. 
Але важко визначити, скільки саме часу нам потрібно чекати, і нудно змінювати цей час, 
якщо ми змінюємо, наприклад, швидкість ходьби Фелікса.

Тому ми будемо використовувати __оповіщення__. 
Такі повідомлення є тим, що персонажі можуть надсилати один одному або на сцену,
і вони не будуть видимими для нас, хто спостерігає.

## Контрольний список {.check}

- [ ] Дозвольте коту надіслати повідомлення, коли він досягне краю екрана.

  ```blocks
  коли зелений прапорець натиснуто
  перемістити в x: (-100) y: (-50)
  повернути в напрямку (100 v)
  повернути до <(x-позиції) > [240]>
      перемістити на (10) кроків
      наступний образ
      чекати (0.1) секунд
  кінець
  оповістити [Scene 2 v]
  ```

- [ ] Тепер ми можемо видалити старий сценарій на сцені,
   який змінив фон на `winter-lights`, і замість цього використати це:
  
  ```blocks
  коли я отримую [Scene 2 v]
  змінити тіло на [winter-lights v]
  ```

- [ ] Фелікс також може отримувати повідомлення, які надсилає сам.
  Ми можемо використовувати це, щоб перемістити його на дорогу, змінивши фон.
  Додайте наступне як новий сценарій на Felix:

  ```blocks
  коли я отримую [Scene 2 v]
  перемістити в x: (-20) y: (-100)
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи Фелікс все ще ходить по екрану?

- [ ] Що станеться, коли він добереться до краю екрана?
      Ми створили два сценарії, які говорять, що фон повинен змінитися,
      а кіт повинен переміститися в центр екрана. Це відбувається?


# Крок 3: Фелікс представляється {.activity}

*Перш ніж Фелікс зайде, ми думаємо, що він повинен представитися!*

Як і всі ввічливі коти, Фелікс представляється, коли знайомиться з новими людьми.

## Контрольний список {.check}

- [ ] Розпочніть новий скрипт на Felix::

  ```blocks
  Коли я отримую [Скожи привіт!]
  говорити [О ні! Де я?] (2) секунди
  подумати [Я заблукав... у свій день народження] на (2) секунди
  запитати [Скільки мені буде років?] і чекати
  ```

- [ ] Щоб перевірити, як працює сценарій, ви можете просто натиснути, наприклад,
      на блок `коли я отримаю Скажи привіт`{.blockevents}. Чи розмовляє і думає Фелікс?

- [ ] Коли ви відповідаєте на запитання Фелікса,
ваша відповідь зберігається у змінній під назвою `відповідь`{.blocksensing}.
Ми створимо нову змінну з кращою назвою, яка зможе подбати про цю відповідь.
Створіть нову змінну під назвою `alder`{.blockdata}. Застосуйте цю змінну до всіх фігур і приберіть відображення,
щоб змінна не з'являлася.

- [ ] Додайте блок внизу скрипта:

  ```blocks
  коли я отримую [Si hei v]
  говорити [О ні! Де я знаходжусь?] на (2) секунди
  подумати [Я заблукав ... у свій день народження] на (2) секунди
  запитати [Скільки мені буде років?] і чекати
  надати [alder v] значення (відповідь)
  ```

- [ ] Тепер ми хочемо, щоб Фелікс все це сказав і зробив, перш ніж блукати лісом.
      Додайте блок `надсилання повідомлень` до першого сценарію Фелікса:

  ```blocks
  коли зелений прапор натиснуто
  перемістити в x: (-100) y: (-50)
  повернути в напрямку (100 v)
  оповістити [Скажи привіт!] і чекати
  повторити до <(x-значення) > [240]>
      перемістити на (10) кроків
      наступний образ
      чекати (0.1) секунд
  кінець
  оповістити [Scene 2 v]
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи правильно розмовляє Фелікс?

- [ ] Можливо, це трохи грубо, що Фелікс просто втікає, поки розмовляє з нами?

## Контрольний список {.check}

- [ ] Ми хочемо, щоб Фелікс закінчив говорити до того, як почне ходити.
  На щастя, це досить просто. Якщо замінимо блок `оповістити`{.blockevents} на інший `оповістити і чекайти`{.blockevents},
  Фелікс не почне ходити, поки не закінчить говорити (і ми відповіли на його запитання):

  ```blocks
  коли зелений прапор натиснуто
  пеемістити в x: (-100) y: (-50)
  поврнути в напрямку (100 v)
  оповістити [Скажи привіт!] і чекати
  повторити до <(x-posisjon) > [240]>
      перемістити на (10) кроків
      наступний образ
      чкати (0.1) секунд
  кінець
  оповістити [Scene 2 v]
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Фелікс чекає, поки ви не відповісте на його запитання?


# Крок 4: Підніміться до будинків {.activity}

*Тоді ми готові допомогти Феліксу знайти дорогу до двох будинків.*

Тепер дозволимо Феліксу пройти дорогою до будинків. 
Щоб виглядало, ніби він йде в гору до будинків, 
ми дозволимо йому ставати все меншим і меншим під час ходьби.

## Контрольний список {.check}

- [ ] Тепер ми продовжимо сценарій Фелікса, який починається з отримання ним повідомлення `scene2`.
      Додайте маленький блок `говорити`{.blocklooks} на початок:

  ```blocks
  коли я отримую [Scene 2 v]
  перемістити в x: (-20) y: (-100)
  говорити [О! Кілька будинків!] (2) секунди
  ```

- [ ] Тепер ми дозволимо Феліксу слідувати дорогою вгору. Спершу спробуйте наступний сценарій:

  ```blocks
  коли я отримую [Scene 2 v]
  перемістити в x: (-20) y: (-100)
  говорити [О! Кілька будинків!] (2) секунди
  повернути в напрямку (20 v)
  повторювати (6) разів
      перемістити на (9) кроків
      наступний образ
      змінити розмір на (-2)
      чекати (0.1) секунд
  кінець
  ```

- [ ] Чи йде Фелікс шляхом вгору? Чи стає він меншим під час ходьби?
      Пам’ятайте, що якщо ви хочете перевірити цей скрипт,
      не переглядаючи всю анімацію, ви можете натиснути кнопку `коли я отримаю scene2`{.blockevents}.
      Ви також повинні натиснути на блок `задати розмір 100`{.blockevents} у групі `Вигляд`{.blockevents} час від часу вкладку,
      щоб Фелікс повернувся до свого нормального розміру.

- [ ] Тепер ми хочемо, щоб Фелікс змінив напрямок, щоб він слідував дорогою.
      Одна хитрість полягає в тому, що ми можемо помножити його напрямок на -1.
      Тоді він ніби обернеться. Оскільки ми хочемо зробити це чотири рази,
      ми також створюємо новий блок `повторювати`{.blockcontrol}:

  ```blocks
  коли я отримую [Scene 2 v]
  перемістити в: (-20) y: (-100)
  говоити [О! Кілька будинків!] (2) секунди
  повернути в напрямку (20 v)
  повторити (4) рази
      повторити (6) рази
          перемістити на (9) кроків
          наступний образ
          змінити розмір на (-2)
          чекати (0.1) секунди
      кінець
      повернути в напрямку ((напрямок) * (-1))
  кінець
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи йде Фелікс дорогою вгору до двох будинків?

Якщо ви трохи уважніше придивитесь до дороги, то побачите, що вона рівна. 
Ми можемо імітувати це для Фелікса, помноживши на число, 
яке трохи відрізняється від -1 у напрямку.

## Контрольний список {.check}

- [ ] Змініть `-1` в точці в `блоці напрямків`{.blockmotion} на `-1,5`.

- [ ] Щоб краще зрозуміти, що відбувається, ви можете натиснути піктограму `Фелікс`{.blockmotion}
      і спостерігати за `напрямком` під час виконання скрипту.

- [ ] Коли Фелікс прибуває в будинок, ми можемо сховати його і переключитися на нову сцену.

  ```blocks
  коли я отримую [Scene 2 v]
  перемістити на x: (-20) y: (-100)
  говорити [О₴ Кілька будинків!] (2) секунди
  повернути в напрямку (20 v)
  повтоити (4) рази
     повторити (6) рази
          перемістити на (9) кроків
          наступний образ
          змінити розмір на (-2)
          чекати (0.1) секунд
      кінець
      поврнути в напрямку ((напрямок) * (-1.5))
  кінець
  сховати
  чекати (1) секунд
  оповісти [Scene 3 v]
  ```

- [ ] Для цієї сцени нам потрібен новий фон.
      Натисніть ![зміна фону](../bilder/velg-bakgrunn.png)
      і додайте цю картинку як фон `Holiday/gingerbread`.
      Додайте до сцени цей скрипт:

  ```blocks
  коли я отримую [Scene 3 v]
  змінити тло на [gingerbread v]
  ```

- [ ] Коли ми переходимо до нової сцени, ми також хочемо,
      щоб Фелікс повернувся до свого нормального розміру.
      Клацніть на Felix і запустіть новий сценарій:

  ```blocks
  коли я отримую [Scene 3 v]
  задати розмір (100)%
  перемістити в x: (-160) y: (-65)
  показати
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи став Фелікс краще слідувати по дорозі, ведучому до будинків?

- [ ] Чи фон з будинками перемикається як слід?

- [ ] Чи отримує Фелікс правильний розмір наприкінці анімації? А коли ви перезапускаєте анімацію?

- [ ] Як ви можете це виправити, адже Фелікс завжди з'являється у повному розмірі, коли ви натискаєте на зелений прапорець?


# Крок 5: Передай привіт пінгвінам {.activity}

*Фелікс зустріне двох пінгвінів, які живуть в будиночку. Вони вийдуть і будуть розмовляти з феліксом*

## Контрольний список {.check}

- [ ] Створіть дві нові фігури, натиснувши
![нові фігури](../bilder/hent-fra-bibliotek.png).
`Penguin1` з файлу `penguin1.svg`. Дайте пінгвінам імена, які вам подобаються, я вирішив назвати їх `Pingu` та  `Pappa Pingu`.

- [ ] Щоб пінгвіни не з'являлися на `scene3`, ми повинні сховати їх, коли почнеться анімація.
      Додайте наступний сценарій до обох фігур:

  ```blocks
  коли зелений прапорець натиснуто
  сховати
  ```

- [ ] Спочатку Фелікс запитає, чи є хтось вдома, а потім надішле повідомлення,
      попросивши пінгвінів вийти. Змініть сценарій Фелікса, додавши два блоки в кінці:

  ```blocks
  коли я отримую [Scene 3 v]
  задати розмір(100)%
  перемістити в x: (-160) y: (-65)
  показати
  подумати [Ой який гарний будинок, цікаво є хтось вдома?] (2) секунди
  оповістити [Kom ut v]
  ```

- [ ] Зараз Pingu вийде з дверей і піде трохи вбік.
      Перевірте за допомогою вказівника миші положення дверей по `x-` і `y-`.
      Додайте такий сценарій до Pingu:

  ```blocks
  коли я отримую [Kom ut v]
  перемістити в x: (45) y: (-70)
  показати
  ковзати (1) сек до x: (150) y: (-100)
  ```

- [ ] Papa Pingu виходить трохи пізніше і ставить запитання Феліксу. Додайте наступний сценарій до Pappa Pingu:

  ```blocks
  Коли я отримую [Kom ut v]
  чекати (2) секунд
  перемістити в x: (45) y: (-70)
  показати
  чекати (1) секунд
  запитати [Як тебе звати] і чекати
  оповістити [Navn1]
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи виходять пінгвіни з будиночка, як і очікувалося?

- [ ] Як ви думаєте, що станеться з ім’ям, яке ви ввели?


# Step 6: The penguins dance {.activity}

*Пінгвіни раді зустрічі з Феліксом, і після короткої розмови один пінгвін починає танцювати, оскільки у Фелікса день народження.*

## Контрольний список {.check}

- [ ] Попросіть  Papa Pingu надіслати повідомлення після того,
      як він запитає, як звуть Фелікса. Ви можете, наприклад, назвати повідомлення `Navn1`

- [ ] Додайте наступний сценарій до Pingu

  ```blocks
  коли я отримую [Navn1 v]
  говорити (відповідь) (2) секунди
  говорити [Це дивне ім'я!] (2) секунди
  оповістити [Navn2 v]
  ```

- [ ] Додайте наступний сценарій до Фелікса, щоб він відповів і сказав, що у нього день народження:

  ```blocks
  коли я отримую [Navn2 v]
  говорити [У мене сьогодні день народження!] (2) секунди
  говорити (з'єднати [Мені буде] (alder)) (2) секунди
  оповістити [Party v]
  ```
Набір приміток для блоку `з’єднати`{.blockoperators}. Я можу використовувати його, щоб скласти текст. 
Переконайтеся, що ви пишете пробіл після слів `Мені буде`!

- [ ] Зараз змусимо Pingu танцювати!
      Створіть два нових костюми для Pingu, імпортувавши Penguin1 з файла `Penguin1.svg` ще два рази.
      Злегка поверніть два нових костюми відносно один одного, клацнувши на костюмах у вікні малювання
      та обертаючи мишкою (може знадобитися переключитися на векторну графіку).

  ![обертаня пінгу](roter_pingu.png)

- [ ] Додайте звук, який вам подобається, у `Lydar`{.blocklightgrey} і
      створіть наступний скрипт на Pingu (я використав звук `pop`):

  ```blocks
  коли я отримую [Party v]
  відтворити звук [pop v]
  повторити (20) раз
      наступний образ
      чекати (0.2) секунд
  кінець
  ```

## Тестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Пінгвін танцює так, як ви очікували?

- [ ] Чому, на вашу думку, було б гарною ідеєю заощадити на відповіді, яку Papa Pingu отримує у змінній?

- [ ] Чи з’являється Pingu в правильному вбранні, коли ви перезапускаєте анімацію?
 Якщо ні, ви повинні дізнатися, як це виправити!

## Збережіть проект {.save}

Зараз ми почали розповідь про кота,
який святкує свій день народження в Антарктиді. 
Чи можете ви розповісти нам більше про те, що буде далі?*

Якщо ви бажаєте показати свою історію родині та друзям,
ви можете вибрати `Розмістити` у верхній частині екрана.

## Завдання: історія має продовження {.challenge}

Чи можете ви продовжити історію? Що буде далі?

Можливо, ви могли б додати більше фігур або більше фону?
Наприклад, чи могли б пінгвіни запросити Фелікса в будинок? 
А може, вони разом продовжують шукати човен, яким кіт зможе дістатися додому?

Пам’ятайте, що ви можете поєднати анімацію з маленькою грою, 
а потім повернутися до більшої анімації. Це повністю залежить від вас!