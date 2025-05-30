---
title: Hoppehelt
level: 4
author: 'Geir Arne Hjelle'
translator: Anatolii
language: ua
---


# Вступ {.intro}

Герой-стрибун трохи натхненний музичною грою Guitar Hero. У грі вам потрібно керувати кількома героями одночасно, 
поки вони перестрибують через кольорові ящики, які видають звуки. На прикладі гри Герой-стрибун ми ближче познайомимося з тим,
як використовуються клони при програмуванні на Скретч. Ми навіть побачимо приклади клонів клонів!

![Зображення готової гри](hoppehelt.png)


# Крок 1: Лінія {.activity}

*Ми починаємо гру зі створення дуже простого фону.*

## Контрольний список {.check}

- [ ] Запустіть новий проект і видаліть персонажа кота.

- [ ] Намалюйте новий фон, що складається з одноколірної прямої лінії досить далеко внизу екрана.
      Використовуйте векторну графіку. Це земля, по якій буде бігти наш герой.

- [ ] Щоб пізніше було легше додати назву, ми створюємо на сцені повідомлення `Нова гра`:

  ```blocks
  коли @greenFlag натиснуто
  оповістити [Нова гра v]
  ```


# Крок 2: Герой-стрибун {.activity}

*Зараз ми представимо вам героя-стрибуна.*

## Контрольний список {.check}

- [ ] Намалюйте просту маленьку фігурку з палички, яка виглядає так, ніби вона біжить ліворуч. Назвіть цю фігурку `Герой 1`.

  Пізніше ви можете створити більше образів, щоб гра виглядала краще, але зараз ми не хочемо витрачати на це час.

- [ ] Створіть нову змінну, яку ви назвете `стрибок`{.blockdata}. Важливо, щоб вона застосовувалася лише до цього персонажа.
 
 Ми будемо використовувати змінну `стрибок`{.blockdata} для опису руху героя, коли він стрибає.

- [ ] В основному циклі героя ми дозволяємо гравітації працювати, постійно намагаючись зробити `стрибок`{.blockdata} меншим,
     в той же час кажучи, що якщо герой торкнеться землі, він не впаде.

  ```blocks
  коли я отримую [Нова гра v]
  перемістити в x: (210) y: (-120)
  завжди
      змінити [стрибок v] на (-1)
      якщо <торкається кольору [#00cc00] ?> то
          наступний образ
          надати [стрибок v] значення [0]
      slutt
      змінити y на (стрибок)
  slutt
  ```

  Встановіть у блоці `торкається`{.blocksensing} кольору той самий колір, що й лінія, яку ви намалювали на тлі в Кроці 1.

- [ ] Спробуйте змінити початкову позицію героя, особливо координату y. Чи можете ви змусити героя впасти на землю?

- [ ] Додайте нову умову `якщо то`{.blockcontrol} до вже наявної `якщо то`{.blockcontrol}. Якщо натиснути клавішу `m`,
   ви встановлюєте `стрибок`{.blockdata} на додатнє число. 
   Експериментуйте, щоб знайти значення, яке дозволить герою робити достатньо великі стрибки.

## Тестування проєкту {.flag}

__Натисніть на зелений прапорець.__

- [ ] Герой стоїть на ногах чи біжить по землі? Фігура не повинна рухатися боком.

- [ ] Чи стрибає герой при натисканні клавіші `m`?

# Крок 3: Коробки зі звуком {.activity}

*Зараз ми створимо кілька коробок, через які герой зможе перестрибувати.*

## Контрольний список {.check}

- [ ] Створіть нового персонажа, намалювавши невелику кольорову коробку, через яку герой може перестрибнути. 
  Назвіть фігуру `Коробка`. За допомогою кнопки  ![Вибрати центральну точку](../bilder/velg_senterpunkt.png) 
  встановіть центральну точку в нижньому лівому куті коробки.

- [ ] Коли коробка отримає повідомлення `Нова гра`, ми хочемо, щоб вона стала на землю в крайньому лівому кутку екрана. 
Скористайтеся блоком `перемістити`{.blockmotion} в і створіть цей сценарій самостійно.
 Переконайтеся, що коробка не торкається краю екрана.

- [ ] Після того, як ви знайшли вдалу позицію для коробки, ви можете продовжити скрипт, 
      `сховати`{.blocklooks} фігуру і створити цикл, в якому коробка робить свій клон кожні дві секунди.

- [ ] Перейдіть на сцену і створіть змінну, яку ви назвете `швидкість`{.blockdata}. Створіть на сцені скрипт, 
      який надає змінній значення `3`, коли ви отримуєте повідомлення `Нова гра`.

- [ ] Поверніться до персонажа-коробки. Тепер ми хочемо, щоб клони коробки рухалися до героя. 
      Створіть новий скрипт, який починається, коли коробка запускається як клон. 
	  У цьому скрипті вам потрібно `показати`{.blocklooks} коробку. Потім ви можете запустити цикл, 
	  який повторюватиметься доти, доки коробка не торкнеться краю. Усередині циклу ви будете змінювати x зі `швидкістю`{.blockdata}. 
	  Після циклу ви можете видалити цей клон.

## Тестування проєкту {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи є постійний потік банок, який рухається до героя?

- [ ] Чи можна з допомогою `m` перестрибнути через ящики?

- [ ] Що станеться, якщо герой стрибне у коробку?

## Контрольний список {.check}

- [ ] Ми хочемо, щоб гра зупинялася, коли герой стрибає в коробку. Перейдіть до `Героя 1`. 
      Тепер замініть цикл `завжди`{.blockcontrol} на цикл `повторити до`{.blockcontrol}, який буде повторюватися до тих пір, 
	  поки герой не торкнеться `Коробки`.
 
- [ ] Після того, як цикл `повторити до`{.blockcontrol} буде завершено, 
      ви можете надіслати нове повідомлення `Гру завершено!`

- [ ] Клацніть на символ коробки. Додайте скрипт, який зупиняє інші скрипти на малюнку, а потім видаляє цей клон після 
      отримання повідомлення `Гру завершено!`

Спробуйте свою гру ще раз. Що станеться, якщо герой стрибне в коробку?

- [ ] Ми можемо відтворювати невеликий звук щоразу, коли пропускаємо ящик. Додайте:


  ```blocks
  відтворити звук [поп] до кінця
  ```

 після циклу, який переміщує коробку, але до того, як клон буде видалено.
 
## Спробуйте самі. {.challenge}

Перш ніж ми продовжимо, давайте розглянемо кілька способів зробити кожну скриньку дещо особливою та відмінною від інших. 
Спробуйте поекспериментувати з цими та іншими налаштуваннями у вашій грі.

На самому початку скрипту, де коробка починається як клон, до того, як вона з'явиться, 
ви можете спробувати деякі з наступних дій. Ви можете довільно змінювати розмір коробки, наприклад, за допомогою блоку


```blocks
задати розмір (випадкове від (100) до (200)) %
```

 В такий же спосіб можна використати

```blocks
змінити ефект [колір v] на (випадкове від (-100) до (100))
```

щоб випадковим чином змінювати колір квадратів. Також придумайте інші ефекти, можливо, використовуючи кілька образів?


Ми також можемо зробити звуки, які лунатимуть, коли ми пропускаємо зайві коробки. 
Наприклад, спробуйте зробити так, щоб довжина тону залежала від розміру коробки.

Нарешті, спробуйте змінити частоту появи нових блоків. Не соромтеся використовувати блок

```blocks
випадкове від (1.2) до` (3.2)
```

Експериментуйте зі значеннями в блоці.


# Крок 4: Більше ліній та квадратів {.activity}

*Тепер ми зробимо гру трохи складнішою, створивши три ряди квадратів.*

## Контрольний список {.check}

- [ ]  Подивіться на скрипти для коробки. Ви побачите, що у вас є *цикл генератора*, який створює нові коробки приблизно 
кожні дві секунди (можливо, ви додали `випадковий`{.blockoperators} блок до цього циклу). 
Також у вас є *цикл переміщення*, який переміщує коробки праворуч, з будь-якими випадковими параметрами на коробках.

   Відірвіть обидва ці цикли і відкладіть їх у бік. Ми скоро знову їх використаємо, тому нічого не видаляйте.

- [ ] Створіть нову змінну, яку ви назвете `генератор`{.blockdata}. Вона має застосовуватися лише до цієї фігури. 
      Ми будемо використовувати цю змінну для ідентифікації циклу генератора.

- [ ] Тепер ми додамо новий цикл, який створить три незалежні цикли генератора. Змініть скрипт, який запускається `Нова гра`, на цей: 

  ```blocks
  коли я отримую [Нова гра v]
  перемістити в x: (-239) y: (-161)
  надати [генератор v] значення [так]
  сховати
  повторити (3)
      створити клон з [мене v]
      змінити y на (110)
  slutt
  ```

Використовуйте ту саму початкову позицію, що й раніше. Це створить три *клони генератора* з різними значеннями y.

- [ ] Тепер ми перебудуємо скрипт, який запускається, коли коробка запускається як клон. Спочатку створіть наступне

  ```blocks
  коли я починаю як клон
  якщо <(генератор) = [так]> то
      надати [генератор v] значення [ні]
  інакше
  slutt
  ```

- [ ] Тепер перемістіть цикл генератора, який ви раніше відклали, у `якщо`{.blockcontrol} тест трохи нижче блоку `надати генератор значення`{.blockdata}.

- [ ] Аналогічно, ви додаєте цикл переміщення з попереднього етапу до тесту `інакше`{.blockcontrol} .

Спробуй свою гру. Тепер у вас має бути три ряди квадратів, що рухаються по екрану.

- [ ] Натисніть на `Сцена` в крайньому правому куті екрана. Перейдіть до `Тло`{.blocklightgrey}. Намалюйте дві нові лінії того ж кольору, 
      що й перша. Перевірте гру та перемістіть лінії так, щоб коробки природньо рухалися поверх них.

## Тестування проєкту {.flag}

__Натисніть на зелений прапорець.__

- [ ] У вас є три ряди квадратиків, що ковзають по екрану?

- [ ] Наразі в нижньому ряду лише один герой-стрибун?


# Крок 5: Де всі герої? {.activity}

*Зараз ми зробимо двох останніх героїв!*

## Контрольний список {.check}

- [ ] Зробіть копію фігури `Герой 1`. Копії буде автоматично присвоєно назву `Герой 2`.

- [ ] Натисніть на `Герой 2`. Єдине, що нам потрібно змінити, це позиція по осі Y та клавіша, яка використовується для стрибка.

  
   Змініть положення блоку `перемістити`{.blockmotion} по осі Y на 110.

   Змініть `m` на `k` в `клавішу натиснуто`{.blocksensing}.

Спробуйте свою гру ще раз. У вас тепер є два герої? Чи працюють вони так, як повинні?

- [ ] Зробіть нову копію фігури `Герой 1`. Змініть цю копію так, щоб її позиція була на 110 вище за `Герой 2`, і щоб вона стрибала при натисканні `o`. 

## Тестування проєкту {.flag}

__Натисніть на зелений прапорець.__

- [ ] Тепер у вас має бути троє героїв-стрибунів, які мають перестрибувати через ящики, що з'являються! 
      Це раптом стало досить складною грою, яка вимагає концентрації та координації!

## Спробуйте самі {.challenge}

На цьому завдання закінчується, але є ще багато цікавих речей, 
які ви можете зробити зі своєю грою, щоб зробити її ще кращою.

Наприклад, спробуйте додати бали, створивши змінну `Очки`{.blockdata}, яку ви збільшуєте щоразу, 
коли пропускаєте клітинку. Ви також можете збільшувати швидкість у міру проходження гри.

Спробуйте зробити так, щоб зіграна нота залежала від положення прямокутника по осі Y. 
Це трохи складно, але виходить справді круто, оскільки звучить так, 
ніби стрибаючі герої грають маленьку пісеньку, перестрибуючи через коробки.
