---
title: Різдвяна листівка
level: 1
author: 'Еспен Клауз'
translator: 'Анатолій Пилипенко'
language: ua
---


# Вступ {.intro}

Ми створимо різдвяну листівку у Scratch. Вона матиме кілька простих функцій та анімацій. Коли вона буде готова, вона виглядатиме приблизно так.

![Eksempel på bilde av et julekort](julekort_ua.png)

# Крок 1: Змініть фон і знайдіть фігури {.activity}

## Контрольний список {.check}

- [ ] Почніть новий проєкт. На стартовій сторінці Scratch натисніть на своє ім'я у верхньому правому куті. Потім натисніть "Мої проекти" і, нарешті, "Створити проект". Ти побачиш кота, який чекає, щоб його запрограмували!

- [ ] Натисніть
![Velg figur fra biblioteket](../bilder/velg-bakgrunn.png) у правому нижньому куті, щоб імпортувати готове тло. Виберіть потрібне тло. Потім натисніть `Сцена`, `Тло`, виберіть порожнє тло зліва і видаліть його, клацнувши правою кнопкою миші і вибравши `Вилучити`.

- [ ] Видаліть персонажа кота `Спрайт 1`.

- [ ] Виберіть нові фігури з бібліотеки за допомогою цієї іконки в правому нижньому куті: ![Hent fra bibliotek](../bilder/hent-fra-bibliotek.png)

   Додайте оленя, сніговика та подарунок.


# Крок 2: Додайте код {.activity}

Тепер ми зробимо так, щоб фігури виконували певні дії при натисканні на них.

## Контрольний список {.check}

- [ ] Виберіть `reindeer` та вкладку `код`{.blocklightgrey}і створіть цей код. Коли на оленя натискають, він повинен сказати `Щасливого Різдва!`.

  ```blocks
  коли спрайт натиснуто
  говорити [Щасливого Різдва!] (2) сек
  ```

## Тестування проєкту {.flag}

__Натисніть на оленя та перевірте, чи працює ваш код.__

- [ ] Чи каже олень `Щасливого Різдва!`?

## Контрольний список {.check}

- [ ] Виберіть сніговика та вкладку `код` і створіть цей код.Сніговик запитає ваше ім'я. Він вставить відповідь у нове речення. Після цього він повинен змінити колір.

  ```blocks
  коли спрайт натиснуто
  запитати [Як Вас звати?] і чекати
  говорити (з'єднати [Щасливого Різдва! ] (відповідь)) (2) сек
  завжди
      змінити ефект [колір v] на (25)
  slutt
  ```

## Тестування проєкту {.flag}

__Натисніть на сніговика і перевірте, чи працює ваш код.__

- [ ] Чи запитує сніговик ваше ім'я?

- [ ] Чи відгукується сніговик на ваше ім'я після того, як ви його 
ввели?
- [ ] Чи змінює сніговик колір?

## Контрольний список {.check}

- [ ] Виберіть подарунок та вкладку `код`{.blocklightgrey} і створіть цей код. Тепер подарунок має змінити колір і вигляд.

  ```blocks
  коли @greenFlag натиснуто
  завжди
      чекати (0.3) секунд
      змінити ефект [колір v] на (25)
      наступний образ
  slutt
  ```

## Тестування проєкту {.flag}

__Натисніть зелений прапорець і перевірте, чи все працює.__

- [ ] Чи змінює подарунок колір?

- [ ] Чи двигається подарунок?


# Крок 3: Чи є у вас вільний час? {.activity}

Тоді ви добре попрацювали! Якщо у вас ще залишився вільний час, ви можете це зробити:

## Контрольний список {.check}

- [ ] Legge til din egen velkomsthilsen, for eksempel "God jul" eller du
kan synge din egen julesang.

  Klikk på `Scene`, og velg fanen `Lyder`{.blocklightgrey}. Flytt
  musepekeren over `Velg en lyd`-ikonet helt nede til venstre, og
  klikk `Spill inn lyd`.

  ![Bilde av fanen "Lyder" i Scratch](lyder.png)

   Ta opp din egen lyd, og gi den et navn, for
  eksempel `julehilsen`. Gå deretter inn på `Skript`{.blocklightgrey},
  og legg inn følgende kode:

  ```blocks
  når @greenFlag klikkes
  spill lyden [julehilsen v] til den er ferdig
  ```

- [ ] Kanskje finne på noen andre morsomme animasjoner? Snømannen kan
danse eller turne litt? Kan vi ha snakkende eller hoppende gale
julepresanger? Du bestemmer!


# Steg 4: Lagre og publisere {.activity}

Gi julekortet ditt et navn. Klikk `Fil`-menyen øverst til venstre, og klikk `Lagre nå` under den.

Deretter kan du publisere julekortet ditt ved å velge `Legg ut`.

![Bilde av hvordan publisere Scratch julekortet](leggut.png)
