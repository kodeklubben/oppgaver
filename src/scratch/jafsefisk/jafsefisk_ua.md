---
title: Акула
level: 2
author: 'Omsett frå [Code Club UK](//codeclub.org.uk)'
translator: 'Vitalii'
language: ua
---


# Вступ {.intro}

Зараз ми створимо гру про Акулу! Мета гри - допомогти Акулі з'їсти всю здобич, що плаває в морі.

![Illustrasjon av eit ferdig Jafsefisk-spel](jafsefisk.png)


# Крок 1: Акула слідує за вказівником миші {.activity}

*Спершу ми змусимо Акулу плавати!*

## Контрольний список {.check}

- [ ] Почніть новий проект у Scratch.

- [ ] Щоб отримати потрібне тло, натисніть ![Vel drakt
  frå biblioteket](../bilder/hent-fra-bibliotek.png).  у правому нижньому куті екрана. Виберіть фон Під водою/underwater2.

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

- [ ] Viss du klarte dette, prøv å gjere eit av byttedyra __raskere__ enn dei
  andre.

- [ ] Beveger byttedyra seg på ein fornuftig måte? Gjer desse forandringane
  spelet betre?

  __Hint:__ Viss byttet ditt svømmer rundt i sirklar, sjekk verdiane i `snu @turnLeft (tilfeldig tal frå (-20) til (20)) gradar`{.b}.

- [ ] Kva viss du let alle byttedyra bevege seg ulikt ved å bruke ulike
  kombinasjonar av desse rørslene?

- [ ] Gjer nokre av desse forandringane spelet betre? Gjer dei spelet meir
  interessant, morosamt, vanskelegare eller lettare? Er noko av dette betre,
  synest du?

## Utfordring 2: Hjelp byttet å unngå Jafsefisk {.challenge}

Byttedyrene i dette spelet er skikkeleg dumme! De svømmer berre tilfeldig rundt
til dei blir etne. Ekte fisk svømmer vekk frå rovfiskane. No vil me __la eitt av
byttedyra svømme vekk frå Jafsefisk.__

Det finst ingen kloss i Scratch som kan gi oss retningen vekk frå ein annan
figur. Men du kan få en figur til å snu seg i retninga mot ein annen, og så la
den snu seg i motsett retning. Klossane du treng er i
`Rørsle `{.blockmotion}-kategorien.

Prøv å hjelpe eitt av byttedyra med å __snu seg vekk frå Jafsefisk__. La den
også virre litt mens den svømmer bort! Du vil kanskje oppdage at byttet set seg
fast i eit hjørne? Kanskje vil du berre at byttet skal flykte viss Jafsefisk
kjem for nære? __Hint:__ Sjå tilbake på korleis me brukte `(avstand til
[musepeikar v])`{.b} tidlegare i spelet.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Gjør dette at fisken blir vanskelegare å ta? Gjer det spelet betre?

## Utfordring 3: Legg til poeng {.challenge}

Det er ikkje nok å berre ete fisk. Korleis vet du at du er ein betre spelar enn
venene dine? Du må kunne __samle poeng__, så la oss leggje til __ei
poengtavle.__ Lag ein variabel som heiter `(poeng)`{.b}, og endre denne når
Jafsefisk et. Pass på at poenga går tilbake til null når spelet startar. Kor
skal du leggje inn desse endringane?

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Går poengsummen opp kvar gong Jafsefisk et byttedyr?

- [ ] Går den tilbake til null når spelet startar?

## Utfordring 4: Legg til ei nedtelling {.challenge}

Gi deg sjølv __ein tidsfrist__. Kor mange fisk kan du ete på `30` sekund?

Legg til ein ny variabel, `(tid)`{.b}. Lag eit nytt skript som set variabelen
til til dømes `30`, for så å endre denne med `-1`, vente eitt sekund, og endre
att, heilt til den når null. Til slutt kan du bruke ein `stopp [alle
v]`{.b}-kloss for å avslutte spelet.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Startar tidtakaren på 30?

- [ ] Tel den ned med rett hastigheit?

- [ ] Kan du fange fisk når tida tel ned?

- [ ] Stoppar spelet når teljaren når null?

## Utfordring 5: Legg til bonuspoeng {.challenge}

Legg til ei belønning med mange bonuspoeng om du klarar å ete alle fiskane
samstundes. Korleis kan du vite hvor mange som er etne?

__Hint:__ Ein måte å gjere dette på er å bruke ein variabel for å __telje__ kor
mange byttedyr som svømmer i havet.

## Test prosjektet {.flag}

__Klikk på det grøne flagget.__

- [ ] Får du bonuspoeng for å ete opp alle fiskane?

## Utfordring 6: Forandre spelet: Hald byttedyra i live! {.challenge}

Av og til kan ein få glimrande nye idear ved å gjere det motsette av det ein
allereie har gjort.

Endre spelet slik at du i staden __kontrollerer eit byttedyr__ i eit hav med
__mange Jafsefiskar__. Kor lenge kan du halde det gåande før du blir ete? I
staden for å bruke poeng kan du telje liv. Kva med å gi byttedyret `3` liv og
avslutte spelet når dei er brukt opp?

## Lagre prosjektet {.save}

__Godt gjort, du er ferdig! No kan du nyte spelet ditt!__

Ikkje gløym at du kan dele spelet med alle venene og familien din ved å klikke
på `Legg ut` i topp-menyen!

