---
title: Акула
level: 2
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Віталій'
language: ua
---


# Вступ {.intro}

Зараз ми створимо гру про Акулу! Мета гри - допомогти Акулі з'їсти всю здобич, що плаває в морі.

![Illustrasjon av eit ferdig Jafsefisk-spel](jafsefisk.png)


# Крок 1: Акула слідує за вказівником миші {.activity}

*Спершу ми змусимо Акулу плавати!*

## Контрольний список {.check}

- [ ] Почніть новий проект у Scratch.

- [ ] Щоб отримати потрібне тло, натисніть ![Velg en ferdig bakgrunn](../bilder/velg-bakgrunn.png).  у правому нижньому куті екрана. Виберіть фон Під водою/underwater2.

- [ ] Видаліть початкового персонажа і додайте нового, натиснувши  ![Vel drakt
  frå biblioteket](../bilder/hent-fra-bibliotek.png) і обравши `Тварини/Shark 2`.
  Назвіть персонажа `Акула`.

- [ ] Переконайтеся, що персонаж може рухатися тільки з боку в бік, вибравши режим обертання
  ![Høgre/Venstre](../bilder/rotasjonsmate-hv-ua.png).

- [ ] Змусьте Акулу слідувати за вказівником миші, створивши цей скрипт

  ```blocks
  коли @greenFlag натиснуто
  змінити образ на [shark2-b v]
  завжди
      слідувати за [вказівник v]
      перемістити на (3) кроків
  slutt
  ```

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Перемістіть вказівник миші навколо водойми. Чи слідує Акула за вказівником?

- [ ] Що станеться, якщо ви не відведете вказівник миші, а Акула знову його досягне? На що це схоже? Чому вона це робить?

## Контрольний список {.check}

- [ ] Ви можете зупинити перевертання Акули, якщо переконаєтеся, що вона рухається лише тоді, коли не знаходиться надто близько до вказівника миші 
  (`відстань до [вказівник v]`{.b} знаходиться в категорії `Датчики`.

  ```blocks
  коли @greenFlag натиснуто
  змінити образ на [shark2-b v]
  завжди
      якщо <(відстань до [вказівник v]) > [10] то>
          слідувати за [вказівник v]
          перемістити на (3) кроків
      slutt
  slutt
  ```

## Речі, які варто спробувати {.challenge}

За бажанням, ви можете змінити числа в скрипті і подивитися, як це змінює рухи.

- [ ] Встановіть обмеження відстані на велике число (наприклад `100`), або на мале
  (наприклад `1`).

- [ ] Встановіть кількість кроків, на які рухається Акула, на велике число (наприклад `20`)
  або на мале (наприклад `1`, або навіть `0`) що стається.


# Крок 2: Додайте здобич {.activity}

*Настав час нагодувати Акулу чимось смачненьким!*

## Контрольний список {.check}

- [ ] Додайте нового персонажа з бібліотеки, обравши `Тварини/Fish`. Надайте персонажу імʼя `Здобич`.

- [ ] Змусьте здобич рухатися у випадкових напрямках. Спочатку ми дозволимо їй трохи просунутися вперед, потім повернемо на випадково обраний кут за годинниковою стрілкою або проти годинникової стрілки, а потім повторимо.

  ```blocks
  коли @greenFlag натиснуто
  задати розмір (40)
  завжди
      перемістити на (2) кроків
      поворот @turnLeft на (випадкове від (-20) до (20)) градусів
      якщо на межі, відбити
  slutt
  ```

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи плаває здобич так, як ви очікували?

- [ ] Чи виглядають її рухи природно?

*Наразі Акула і здобич не взаємодіють один з одним. Ми зробимо щось з цим на наступному кроці.*

## Речі, які варто спробувати {.challenge}

- [ ] Спробуйте змінити числа в `перемістити на (2) кроків`{.b} та `випадкове від (-20)
  до (20)`{.b}. Як це змінює рухи здобичі?

- [ ] Що робить `якщо на межі, відбити`{.b}? Видаліть цей блок і подивіться, що станеться.

# Крок 3: Акула їсть здобич {.activity}

*Тепер нехай Акула з'їсть здобич!*

Коли Акула спіймала здобич у роті, мають відбутися дві речі: Акула повинна закрити свій рот і зробити звук ковтання. Здобич повинна зникнути і з'явитися через деякий час.

## Контрольний список {.check}

- [ ] Ми починаємо з того, що дозволяємо здобичі зникнути, якщо вона торкається Акули, а потім здобич повертається через `3` секунди. Використовуйте `торкається [Акула v]?`{.b} щоб перевірити, чи доторкнулася жертва до Акули. Розширте скрипт для здобичі таким чином:

  ```blocks
  коли @greenFlag натиснуто
  показати
  завжди
      перемістити на (2) кроків
      поворот @turnLeft на (випадкове від (-20) до (20)) градусів
      якщо на межі, відбити
      якщо <торкається [Акула v]? то>
          сховати
          чекати (3) секунд
          показати
      slutt
  slutt
  ```
## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Зверніть увагу, що здобич зникає незалежно від того, якої частини Акули вона торкається.

- [ ] Більше того, Акула може чекати лише 3 секунди, а потім з'їсти здобич, як тільки вона знову з'явиться, що не дуже чесно!

## Контрольний список {.check}

*Як зробити так, щоб здобич зникала лише тоді, коли торкнеться рота Акули? Ну, ми можемо використати `<торкається кольору  [#FFFFFF]?>`{.b} і подивитися, чи торкається здобич білих зубів риби.*

- [ ] Додайте `<торкається кольору [#FFFFFF]?>`{.b} разом з `<торкається
  [Акула v]?>`{.b} у ваш скрипт. Щоб вибрати білий колір, клацніть на колір у блоці, а потім на зуби риби.

- [ ] Тепер ми можемо дозволити здобичі переміститися у довільну точку екрана, перш ніж вона знову з'явиться на екрані за допомогою `перемістити в x: (випадкове від (-220) до (220)) y:
  (випадкове від (-170) до (170))`{.b} ми присвоюємо випадкові значення `x` та `y` здобичі.

Ось як повинен виглядати сценарій здобичі:

  ```blocks
  коли @greenFlag натиснуто
  показати
  завжди
      перемістити на (2) кроків
      поворот @turnLeft на (випадкове від (-20) до (20)) градусів
      якщо на межі, відбити
      якщо <<торкається [Акула v]?> і <торкається кольору [#FFFFFF]?> то>
          сховати
          чекати (3) секунд
          перемістити в x: (випадкове від (-220) до (220)) y: (випадкове від (-170) до (170))
          показати
      slutt
  slutt
  ```

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи зникає здобич тільки тоді, коли вона торкається зубів Акули?

- [ ] Чи з'являється вона знову у випадковому місці на екрані - тобто не там, де була з'їдена?

# Крок 4: Акула реагує {.activity}

*Акула повинна знати, коли вона щось з'їла, щоб видавати звуки і змінювати свій образ.*

## Контрольний список {.check}

- [ ] Щоб Акула знала, що відбувається, ми можемо дозволити здобичі надсилати сповіщення `оповістити
  [Ти з'їв мене! v]`{.b}, що її з'їли, перш ніж вона зникне.

  ```blocks
  коли @greenFlag натиснуто
  показати
  завжди
      перемістити на (2) кроків
      поворот @turnLeft на (випадкове від (-20) до (20)) градусів
      якщо на межі, відбити
      якщо <<торкається [Акула v]?> і <торкається кольру [#FFFFFF]?> то>
          оповістити [Ти з'їв мене! v]
          сховати
          чекати (3) секунд
          перемістити в x: (випадкове від (-220) до (220)) y: (випадкове від (-170) до (170))
          показати
      slutt
  slutt
  ```
  
Тепер ми хочемо, щоб Акула відреагувала на це повідомлення, зробивши звук ковтання і клацання щелепами.

- [ ] Legg til drakta `Dyr/shark-a` og lyden `Effekter/bubbles` på Jafsefisk.
  Kall drakta `Lukka munn`.

- [ ] Додайте новий скрипт до Акули, щоб вона могла реагувати на повідомлення `Ти з'їв мене!` від здобичі. Цей скрипт змушує Акулу відтворити звук укусу і зробити вигляд, наче вона кусає `змінити образ на [shark2-a v]`{.b}-drakta, трохи почекати, а потім переключитися назад.

  ```blocks
  коли я отримую [Ти з'їв мене! v]
  відтворити звук [Bite v]
  повторити (2)
      змінити образ на [shark2-a v]
      чекати (0.3) секунд
      змінити образ на [shark2-b v]
      чекати (0.3) секунд
  slutt
  ```

Тепер Акула готова їсти, тож давайте наповнимо море здобиччю.

- [ ] Клацніть правою кнопкою миші на здобич і виберіть `дублювати`, доки не відчуєте, що маєте достатньо риби.

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи їсть Акула свою здобич?

- [ ] Чи з'їдає вона всю здобич?

## Дещо для роздумів {.protip}

Чому ми повинні додати `показати`{.b} на початку скрипта для здобичі? Подумайте, що станеться, якщо здобич буде з'їдена, а гра зупиниться до того, як вона знову з'явиться. І що станеться, якщо гру перезапустити?

## Збережіть свій проект {.save}

__Молодець!__ Ви практично завершили гру! Але є кілька можливостей для розширення гри. Чи готові ви до виклику?

## Виклик 1: Змінити рух здобичі {.challenge}

Наразі всі здобичі рухаються однаково. __Чи можете ви змусити одну з них рухатися інакше?__ 

__Підказка:__ Не витрачайте занадто багато часу на це завдання, не подивившись на інші завдання цього проекту.

__Виберіть рибу-здобич для експерименту.__ Якщо у них усіх однаковий вигляд, то змініть колір `встановити ефект [колір v]- в (0)`{.b}. Так ви можете відрізнити її від решти здобичі. Тепер спробуйте змусити цю здобич рухатися повільніше, ніж інші.

__Підказка:__ Подивіться на блок `перемістити на (2) кроків`{.b}.

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи рухається здобич повільніше? Чи робить це гру кращою?

- [ ] Якщо вам вдалося це зробити, спробуйте зробити одну з жертв __швидшою за інших.__

- [ ] Чи рухається здобич у розумний спосіб? Чи роблять ці зміни гру кращою?

  __Підказка:__ Якщо ваша здобич плаває колами, перевірте значення у полі  `поворот @turnLeft на (випадкове від (-20) до (20)) градусів`{.b}.

- [ ] Що, якщо дозволити здобичі рухатися по-різному, використовуючи різні комбінації цих рухів?

- [ ] Чи роблять якісь із цих змін гру кращою? Вони роблять гру цікавішою, веселішою, складнішою чи легшою? Як ви вважаєте, які з них кращі?

## Виклик 2: Допоможіть здобичі уникнути Акули {.challenge}

Здобич у цій грі дуже дурна! Вона просто плаває навмання, поки її не з'їдять. Справжні риби тікають від хижих риб. Зараз ми __дозволимо одній з жертв втекти від Акули.__

У Scratch немає блоку, який би вказував нам напрямок руху від іншого персонажа. Але ви можете змусити одного персонажа повернутися в напрямку іншого, а потім змусити його повернутися в протилежному напрямку. Блоки, які вам потрібні, знаходяться у категорії `Рух `{.blockmotion}.

Тепер спробуйте допомогти одній рибі __відвернутися від Акули.__. Крім того, нехай вона трохи поворушиться, відпливаючи! Ви ймовірно можете помітити, що здобич застрягла в кутку? Ви можете помітити, що здобич хоче втекти лише тоді, коли Акула підпливе надто близько? __Підказка:__ Згадайте, як ми використовували `(відстань до
[вказівник v])`{.b} на початку гри.

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи робить це полювання складнішим? Чи робить це гру кращою?

## Виклик 3: Додайте бали {.challenge}

Недостатньо просто їсти рибу. Як дізнатися, що ти кращий гравець, ніж твої друзі? Для цього потрібно вміти набирати очки, тож давайте додамо табло. Створіть змінну з назвою `(Бали)`{.b}, і змінюйте її, коли Акула їсть. Переконайтеся, що бали повертаються до нуля на початку гри. Куди потрібно внести ці зміни?

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи збільшується рахунок щоразу, коли Акула з'їдає здобич?

- [ ] Чи повертається він до нуля, коли гра починається?

## Виклик 4: Додайте зворотний відлік {.challenge}

Встановіть собі __дедлайн__. Скільки риби ви можете з'їсти за 30 секунд?

Додайте нову змінну, `(Час)`{.b}. Створіть новий скрипт, який встановлює змінну, наприклад, на 30, потім змінює її на -1, чекає 1 секунду і знову змінює її, поки вона не досягне нуля. Нарешті, ви можете скористатися блоком `зупинити [все
v]`{.b}-kloss щоб завершити гру.

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи починається таймер на 30?

- [ ] Чи він відраховує час з правильною швидкістю?

- [ ] Чи можна ловити рибу під час зворотного відліку часу?

- [ ] Чи зупиняється гра, коли лічильник досягає нуля?

## Виклик 5: Додайте бонусні бали {.challenge}

Додайте винагороду з великою кількістю бонусних балів, якщо вдасться з'їсти всю рибу одночасно. Як визначити, скільки рибок було з'їдено?

__Підказка:__ Один із способів зробити це - використати змінну для підрахунку кількості здобичі, що плаває в океані.

## Протестуйте проект {.flag}

__Натисніть на зелений прапорець.__

- [ ] Чи отримуєте ви бонуси за те, що з'їли всю рибу?

## Виклик 6: Змінити правила гри: Збережіть здобич живою! {.challenge}

Іноді ви можете знайти чудові нові ідеї, роблячи протилежне тому, що ви вже робили.

Змініть гру так, щоб замість цього ви керували здобиччю в морі з безліччю Акул. Як довго ви зможете протриматися, перш ніж вас з'їдять? Замість того, щоб використовувати очки, ви можете рахувати життя. Як щодо того, щоб дати здобичі 3 життя і закінчити гру, коли вони закінчаться?

## Збережіть свій проект {.save}

__Молодець, ти впорався! Тепер ти можеш насолоджуватися грою!__

Не забувай, що ти можете поділитися своєю грою з друзями та родиною, натиснувши кнопку "Поділитись" у верхньому меню!

