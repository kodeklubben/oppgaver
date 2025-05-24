---
title: Мистецтво з геометричними фігурами
author: 'Карл Андреас Мірланд'
translator: 'Анатолій Пилипенко'
language: ua
---

# Вступ {.intro}

У цьому завданні ми навчимося створювати стильні роботи, використовуючи геометричні фігури, випадковість та функції.

![Bildebeskrivelse](./scratchopplegg.png)

# Крок 1: Готуємо олівець {.activity}

Спочатку ми налаштовуємо "нудні" речі, щоб потім програма працювала належним чином.

## Контрольний список {.check}

- [ ] Видалити символ кота

- [ ] Вставте фігуру `Pencil`

- [ ] Перейдіть на вкладку "Образи", і перемістіть олівець так, щоб кінчик олівця вказував на центральну точку.
      
- [ ] Поверніться на вкладку "Код".

- [ ] Додайте бібліотеку олівця, натиснувши синій значок "+" у лівому нижньому кутку екрана та вибравши "Олівець"

- [ ] Отримайте блок, `коли зелений прапорець натиснуто`{.blockevents} і надішліть `оповістити [повідомлення1]`{.blockevents}, а потім об'єднайте їх разом.

- [ ] Натисніть маленьку білу стрілку поруч із "повідомлення1", , виберіть «нове повідомлення» та назвіть його "готовий":

```blocks
коли grønt flagg натиснуто
оповістит [готовий v]
```

- [ ] Тепер ми створимо нову послідовність, яка підготує нашого персонажа до малювання:

```blocks
коли я отримую [готовий v]
стиль обертання [не обертати v]
сховати
підняти олівець
очистити все
показати
оповістити [завершено v]
```

- [ ] Наприкінці цього кроку ми створюємо невелику послідовність, яка наказує персонажу слідувати за вказівником миші або нашим пальцем, коли ми рухаємо його по екрану:

```blocks
коли я отримую [завершино v]
завжди
перейти до [вказівник v]
```

## Тестування проєкту {.flag}

**Натисніть на зелений прапор.**

- [ ] Тепер ви побачите, що наш персонаж слідує за вказівником миші або пальцем, коли ви переміщуєте його по сцені.

- [ ] Ви розумієте, чому це відбувається?

# Крок 2: Створюйте мистецтво (ПК){.activity}

## ПК чи планшет?{.protip}

На цьому кроці ви знайдете інструкції як для пристроїв із зовнішньою мишею, так і для пристроїв із сенсорним екраном. Переконайтеся, що ви вибрали правильну інструкцію для пристрою, який ви використовуєте, наприклад, iPad або ПК.

Тепер давайте складемо код, який дозволить нам малювати геометричні фігури! Ми почнемо з простої версії, а потім зробимо код більш просунутим у кроці 3.

## Інструкція для ПК: {.check}

- [ ] Пропустіть цей крок, якщо ви використовуєте пристрій із сенсорним екраном, наприклад, iPad або подібний.

- [ ] Ми хочемо, щоб фігура починала малюватися, коли ми натискаємо ліву кнопку миші. Тому ми встановили таку послідовність:

```blocks
коли спрайт натиснуто
зупинити [інші скрипти цього спрайту v]
опустити олівець
повернути в напрямку (90)
повторити (4)
перемістити на (100) кроків
поворот høyre на (90) градусів
end
підняти олівець
оповістити [завершино v]
```

## Тестування проєкту{.flag}

**Натисніть на зелений прапор.**

- [ ] Доторкніться до довільного місця на сцені. Бачите квадрат? Спробуйте торкнутися кількох місць поспіль. Що відбувається?

- [ ] Однак зараз ми можемо намалювати лише один тип фігур. Зрозуміло, чому? У наступному розділі ми навчимося створювати більше фігур!

# Крок 2: Створюємо мистецтво (планшет){.activity}

## Інструкція для планшетів {.check}

Оскільки сенсорні пристрої, такі як iPad, не мають вказівників миші, ми повинні створити дещо інше рішення.

- [ ] Якщо у вас є PC/Mac з мишкою, ви можете перейти до кроку 3.

- [ ] По-перше, нам потрібно створити кнопку, яку ми зможемо натиснути. Вставте нову фігуру з галереї, наприклад  `Button1`, і напишіть цей код:

```blocks
коли grønt flagg натиснуто
перемістити x: (180) y: (-150)

коли спрайт натиснуто
оповістити [старт v]
```

- [ ] Поверніться до символу Олівець і напишіть цей код:

```blocks
коли я отримую [старт v]
зупинити [інші скрипти цього сайту v]
опустити олівець
повернути в напрямку (90)
повторити (4)
перемістити на (100) кроків
поворот høyre на (90) градусів
end
підняти олівець
оповістити [завершино v]
```

## Тестування проєкту {.flag}

**Натисніть на зелений прапор.**

- [ ] Торкніться довільного місця на сцені

- [ ] Натисніть кнопку, яку ми вставили

- [ ] Чи з'явилася фігура там, де ви натиснули?

- [ ] Торкніться кількох місць на екрані, а потім торкніться кнопки. Що відбувається?

- [ ] Тепер ми можемо малювати лише один тип фігур. Зрозуміло, чому? У наступному розділі ми дізнаємося, як створювати більше фігур!

# Крок 3: Більше геометричних фігур {.activity}

На цьому кроці ми навчимося створювати трикутники, квадрати та п'ятикутники для наших робіт.

**УВАГА! На цьому кроці вам не потрібно додавати нові блоки коду. Ми лише змінимо значення деяких блоків, які у нас вже є!
**

## Ми робимо кілька геометричних фігур {.check}

- [ ] Секрет створення різних геометричних фігур криється в цій невеликій послідовності з кроку 2:

```blocks
повторити (4) 
перемістити на (100) кроків
повернути høyre на (90) градусів
end
```

- [ ] Ключовим моментом є взаємозв'язок між кількістю циклів  `повторити`{.blockcontrol} і тим, на скільки градусів повинна повернутися фігура.

## Кутові суми{.protip}

Ви, мабуть, знаєте, що різні фігури мають різні кутові суми. З математики ми знаємо, що трикутник має суму кутів 180 градусів, квадрат - 360 градусів, п'ятикутник - 540 градусів тощо.

Це правильно, якщо вимірювати внутрішні кути фігури. Але для того, щоб це було правильно на комп'ютері, нам потрібно враховувати зовнішні кути, тобто сусідні кути до тих, які ми зазвичай вимірюємо в математиці.

Ви, мабуть, знаєте, що сума двох сусідніх кутів завжди дорівнює 180 градусам. Це означає, що коли ми говоримо, що всі кути в рівносторонньому трикутнику дорівнюють 60 градусам, ми повинні використовувати сусідній кут 120 градусів, коли просимо комп'ютер намалювати рівносторонній трикутник. Для прямокутного чотирикутника сусідній кут завжди дорівнює 90 градусам. Для п'ятикутника сусідній кут дорівнює 72 градусам тощо.

Коли ми обчислюємо зовнішні кути правильних геометричних фігур, сума кутів завжди дорівнює 360 градусам! Розумієте, чому?

- [ ] Мета полягає в тому, щоб добуток кількості повторень на кількість градусів дорівнював 360 градусам. Можна уявити, що кількість повторень (`повторити (3)`{.blockcontrol}) говорить нам, скільки ребер матиме наша фігура, в той час як кількість градусів потрібно підбирати так, щоб добуток дорівнював 360 градусам. крок перемістити `перемістити`{.blockmotion} вказує лише на те, якої довжини будуть сторони фігури:

```blocks
повторити (3)
перемістити на (100) кроків
поворот høyre на (120) градусів
end
```

## {.protip}

Як швидко знайти зовнішній кут
Якщо вам потрібно дізнатися, наскільки великим повинен бути зовнішній кут для даного багатокутника, ви можете знайти його, розділивши 360 на кількість сторін у фігурі:

360 : 3 = 120

360 : 4 = 90

360 : 5 = 72

і т.д.

## Тестування проєкту {.flag}

**Натисніть на зелений прапор.**

- [ ] Змініть значення у вашому коді так, щоб ви могли малювати трикутники та п'ятикутники.

- [ ] Запустіть код і подивіться, що станеться далі!

- [ ] Чи розумієте ви, чому це відбувається?

# Крок 4: Функції та змінні {.activity}

Тепер, коли у нас є робочий код, який дозволяє нам малювати різні фігури, ми можемо розглянути, як ми можемо трохи прибрати код, щоб зробити його ще кращим і заощадити нашу роботу пізніше! Спочатку ми створимо `функцію`{.blockmoreblocks}, яка автоматизує частину роботи за нас. У Scratch `функції`{.blockmoreblocks} називаються "`Мої блоки`{.blockmoreblocks}", тож ми знаходимо першу потрібну цеглинку там.

## Створіть функцію {.check}

- [ ] Перейдіть на вкладку `Мої блоки`{.blockmoreblocks}, і натисніть "Створити блок".

- [ ] При цьому з'являється меню, яке дозволяє вам вирішити, як викликати функцію і які параметри вона повинна мати.
- [ ] Назвемо блок "багатокутник" і додамо два поля для  "чисел або тексту".
- [ ] Перше поле назвемо "ребра", друге -  "довжина сторони".
- [ ] Коли ти закінчиш, ти отримаєш новий блок на своєму робочому місці і новий блок під `Мої блоки`{.blockmoreblocks}:

```blocks
визначити багатокутник (ребра) (довжина сторони)

багатокутник (ребра) (довжина сторони)

```

## Ми змінюємо наш код {.check}

**Цей крок може бути трохи складним. Переконайтеся, що ви тримаєте язик за зубами і уважно читаєте інструкції.**
Тепер ми перебудуємо наш код так, що зможемо легко перемикатися між трикутниками, чотирикутниками і п'ятикутниками, аж до кіл, без необхідності обчислювати кути самостійно!

- [ ] Спочатку визначимо нашу функцію. Рожеві змінні (ребра) і (довжина сторони) беруться прямо з блоку визначення вгорі і вставляються в код як звичайні змінні:

```blocks
визначити багатокутник (ребра) (довжина сторони)
повторити (ребра)
перемістити на (довжина сторони) кроків
поворот høyre на ((180) -  ((((ребра) - (2)) * (180)) / (ребра))) градусів
end

багатокутник (ребра) (довжина сторони)

```

- [ ] Тепер ми змінимо послідовність, `коли спрайт натиснуто`{.blockevents} яка запускається при натисканні на цю фігуру, якщо ви використовуєте мишу, або `коли я отримую старт`{.blockevents} якщо ви використовуєте сенсорний екран, і замість цього використаємо функцію `багатокутника`{.blockmoreblocks}.

## Viktig info {.protip}

Koden for mus og berøringsskjerm er lik herfra og ut, den eneste forskjellen er hendelsen som starter skriptet som lager tegningen. For mus er det `Når denne figuren klikkes`{.blockevents}, for berøringsskjerm er det `Når jeg mottar [start]`{.blockevents}

- [ ] Først må vi fjerne `gjenta`{.blockcontrol}-løkken fra sekvensen, slik at vi sitter igjen med

```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
penn av
send melding [ferdig v]

```

- [ ] Så setter vi inn `mangekant`{.blockmoreblocks}-blokken der gjenta-løkka var:

```blocks
Når denne figuren klikkes
stopp [andre skript i figuren v]
penn på
pek i retning (90)
mangekant () ()
penn av
send melding [ferdig v]

```

#### Feil farge på klossene? {.protip}

`Mangekant`{.blockmoreblocks}-blokken vises med rød farge i koden over, men det er av tekniske årsaker i verktøyet vi skriver oppgaven med. Du kan se bort fra feil farger på klossene i denne delen av oppgaven.

Du kan nå fylle inn hvor mange kanter du vil at figuren skal ha, og hvor lange de skal være i funksjonsblokken

- [ ] Hvis vi vil tegne en sekskant med 40 piksler lange sider, fyller vi inn:

```blocks
mangekant (6) (40)
```

## Test koden din {.flag}

- [ ] Fyll inn hvor mange kanter du vil at figuren din skal ha, og hvor lange sidene skal være

- [ ] Trykk på grønt flagg

- [ ] Hvis du bruker mus, trykk et sted på scena der du vil at figuren skal tegnes.

- [ ] Hva skjer om du endrer på verdiene i `mangekant`{.blockmoreblocks}?

- [ ] Forstår du hva som skjer?

## Den magiske formelen {.challenge}

Denne formelen er det "magiske" elementet i koden vår:

```blocks
vend høyre ((180) -  ((((kanter) - (2)) * (180)) / (kanter))) grader
```

Denne utregningen finner nemlig vinkelen i en regulær mangekant, kun ved å vite hvor mange kanter figuren består av. Sett inn hvor mange kanter figuren din skal ha (3 for trekant, 4 for firkant, osv) i `kanter`{.blockdata}-variabelen, og regn ut, så finner du alltid riktig vinkel.

Klarer du å finne ut hvorfor det blir slik?

# Steg 5: Litt mer farge og liv! {.activity}

Vi har nå laget et program som lar deg lage mange forskjellige kunstverk ved hjelp av geometriske figurer, men figurene har kanskje litt kjedelige farger?

- [ ] Ved å sette inn

```blocks
sett pennbredde til ()
```

og

```blocks
sett pennens (farge v) til ()
```

etter `penn på`{.blockpen}-klossen, kan du endre på både strekens bredde og farge. Prøv deg frem!

- [ ] Du kan også eksperimentere med klossene

```blocks
endre pennens (farge v) med ()
```

og

```blocks
endre pennens bredde med ()
```

og se hva som skjer da!

- [ ] For å gjøre kunsten enda mer variert, kan du også eksperimentere med å sette inn klossen

```blocks
tilfeldig tall fra () til ()
```

fra `operatorer`{.blockoperators}-kategorien. `Tilfeldig tall`{.blockoperators}-klossen kan settes inn i `pek i retning`{.blockmotion}-klossen, i `mangekant`{.blockmoreblocks}-klossen, og i de ulike `penn`{.blockpen}-klossene for å endre farge og bredde.

## Gjør programmet enda enklere å bruke! {.protip}

For å gjøre programmet enda mer brukervennlig, kan du lage to variabler. La oss kalle dem `sideAntall`{.blockdata} og `sideLengde`{.blockdata}. Sett inn variablene i `mangekant ( ) ( )`{.blockmoreblocks}-klossen. Variablene vil også vises på scena. Trykk og hold på hver av variabel-boblene, slik at du får opp en meny. I denne menyen velger du "skyveknapp". Da kan du enkelt endre på hva slags type mangekant du vil ha, og hvor lange sidene skal være, ved å dra skyveknappen til høyre eller venstre. I menyen kan du også velge å endre verdiområdet for variabelen, sånn at sideAntall begrenses mellom 3 og 20, og sideLengde begrenses mellom 10 og 100, for eksempel.

## Lagre programmet {.save}

Husk å gi programmet ditt et navn, sånn at du lett finner det igjen senere. Når du er ferdig kan du klikke på "Legg
ut"-knappen. Da vil det bli lagt ut på Scratch-hjemmesiden din slik at du enkelt
kan dele det med familien og vennene dine.

