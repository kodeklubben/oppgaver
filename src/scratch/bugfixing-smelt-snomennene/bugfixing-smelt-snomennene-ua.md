
---
title: "Виправлення помилок: Розтопити сніговиків!"
author: "[c4creativity](https://scratch.mit.edu/users/c4creativity)"
translator: "Ніна"
language: "ua"
---


# Вступ до завдання {.intro}

У цьому завданні ви спробуєте поміняти та покращити код, який вже було створено у програмі на Scratch. Мета полягає в тому, щоб змусити трьох сніговиків говорити по черзі, а потім одночасно розтанути!

![Bildebeskrivelse](bugfix1.jpg)


# Крок 1: Копіювання {.activity}

По-перше, нам потрібно відкрити існуючий проект і створити його копію. Прочитайте весь чек-лист перед тим, як перейти за посиланням!

## Контрольний список {.check}

- [ ] Відкрийте проект: [Bugfixing: Smelt snømennene!](https://scratch.mit.edu/projects/445564165/ ){target=_blank}
- [ ] Обов'язково натисни на кнопку "Ремікс"
- [ ] Краще дати проекту нову назву, щоб легше було знайти знову.

## Тестуйте проект {.flag}

**Стартуйте проект, щоб протестувати код.**

Не соромтеся відповідати на ці питання в зошиті, обговоріть їх з одним-двома однокласниками і намагайтеся відповідати якомога точніше.

- [ ] Що відбувається, коли ви натискаєте зелений прапорець?

- [ ] Мета полягає в тому, щоб сніговики по черзі сказали «Готово, увага, танути!», причому кожний сніговик повинен сказати лише одне слово. Як цього досягти?

- [ ] Прочитайте код для трьох різних фігур. Чи знаходите ви в коді якісь підказки або натяки, які дають вам уявлення про те, які зміни потрібно внести?

## Контрольний список {.check}

Деякі поради для вас:

- [ ] Всі фігури мають блок

```blocks
говорити [готово] (2) сек
```
- [ ] Фігура "Сніговик-1"  має додатковий блок

```blocks
чекати (1) секунду
```

Змінити блок `говорити`{.blocklooks}.
- [ ] Що станеться, якщо перемістити блок `чекати`{.blockcontrol} над блоком `говорити`{.blocklooks} і змінити час очікування, наприклад, на 3 секунди замість 1?

## Тестуйте проект {.flag}

**Натисніть на зелений прапорець.**

- [ ] Перевірте свій новий код. Що відбувається далі? Запишіть те, що ви спостерігаєте, або обговоріть це з однокласником.
- [ ] Чи розмовляють три сніговики одночасно?


# Крок 2: Готово, увага, танути! {.activity}

На основі того, що ми виявили на кроці 1, ми готові виправити першу помилку в нашому коді: Сніговики повинні по черзі говорити «Готово», «Увага», «Танути!».

## Контрольний список {.check}

- [ ] Сніговик 1 повинен сказати «Готово», коли ви натиснете на зелений прапорець.

- [ ] Сніговик 2 повинен сказати «Увага» після того, як сніговик 1 скаже «Готово»

- [ ] Сніговик 3 повинен сказати «Танути!» після того, як сніговик 2 скаже «Увага» 

Вам необхідно вставити оператор очікування для Сніговиків 1 і 2, розмістити це перед оператором говорити, подібно до:

```blocks
чекати (1) секунду
говорити [Готово] (2) сек
```
- [ ] Приберіть блок `чекати`{.blockcontrol} для Сніговіка 1

- [ ] Як довго Сніговику 2 і Сніговику 3 доведеться чекати, перш ніж вони скажуть своє слово?

## Тестуйте проект {.flag}

**Натисніть на зелений прапорець для тестування коду**

Дайте відповіді на запитання в зошиті або обговоріть їх з однокласником.

- [ ] Чи кажуть зараз три сніговика по черзі «Готово, увага, танути!»?

- [ ] Чи зникають вони після того, як останній сказав «Танути!»?

- [ ] Чи знаходите ви в коді підказки, які дають уявлення про те, що робити далі?

## {.tip}
Створення подібних алгоритмів для кожної окремої фігури у Скретч може бути громіздким. Ось чому варто спочатку більш-менш доопрацювати код для однієї фігури, а потім скопіювати його до інших фігур. Просто перетягніть алгоритм, який ви хочете скопіювати, на огляд фігур під сценою і перетягніть його на фігуру, до якої ви хочете скопіювати. Після цього вам потрібно буде внести лише кілька невеликих змін до коду, замість того, щоб переписувати його для кожного персонажа.
#

# КРОК 3: Танути! {.activity}

Тепер, коли ми по черзі поговорили зі сніговиками, настав час виправити код танення.

Сніговик 2 має для нас важливу підказку:

```blocks
повторити (2)
змінити ефект [ghost v] на (25)
чекати (1) секунд
змінити розмір на (-10)
```

Ефект `ghost`{.blocklooks} допомагає зробити персонажа все більш і більш невидимим, за шкалою від 0 (повністю видимий) до 100 (повністю невидимий). Крім того, ми хочемо, щоб сніговик щоразу ставав трохи меншим, щоб показати, що він «тане». Тому ми також використовуємо `зміна розміру`{.blocklooks}.

## Контрольний список {.check}
- [ ] Змініть код таким чином, щоб ефект `ghost`{.blocklooks} досягав 100 після завершення роботи циклу. Значення ефекту починається з 0, коли натискається зелений прапорець. Скільки разів потрібно повторити цикл, якщо ми дозволимо примарному значенню змінюватися на 25 кожного разу?

- [ ] Чи можете ви налаштувати співвідношення між кількістю `повторити`{.blockevents}, `ghost`{.blocklooks} ефектом і `чекати`{.blockcontrol}, щоб отримати більш плавну анімацію танення?

## Test prosjektet {.flag}
Noter svarene i en notatblokk eller diskuter med en medelev.

- [ ] Smelter Snømann 1 helt bort?

- [ ] Ser smelteanimasjonen grei ut? Går den passe fort, og med jevnt tempo helt til snømannen er borte?

- [ ] Hva er det som ikke fungerer som det skal hittil?
#

# Steg 4: Siste justeringer {.activity}
Når du har kommet så langt i oppgaven, skal de tre snømennene si "Klar, ferdig, smelt!" i tur og orden, og snømann 1 smelter helt bort. Men vi er ikke helt i mål enda. Oppgaven er at de tre snømennene skal smelte samtidig *etter* at de har sagt "Klar, ferdig, smelt!" - og der er vi ikke helt i mål enda.

## Sjekkliste {.check}
- [ ] Kopier `gjenta`{.blockcontrol}-løkka over til Snømann 2 og 3.
- [ ] Du ser at Snømann 2 har en algoritme som skal starte `Når denne figuren klikkes`{.blockevents}. Du kan slette hele den algoritmen nå.
- [ ] For å sørge for at alle snømennene smelter samtidig, må du legge til en `vent`{.blockcontrol}-kloss over `gjenta`{.blockcontrol}-løkka til hver enkelt snømann. Snømann 1 må vente lengre enn de to andre før han starter på `gjenta`{.blockcontrol}-løkka, men hvor lenge må han vente?
- [ ] Et hint er at han må vente helt til Snømann 3 har sagt "Smelt!"
- [ ] Til slutt rydder vi opp ved å legge `Sett størrelse`{.blocklooks}-klossen øverst i `Når grønt flagg klikkes`{.blockevents}-algoritmen på alle figurene, sletter eventuelt ubrukte klosser og ser over en siste gang for å sjekke at koden er i orden på alle de tre snømennene.

## Test prosjektet {.flag}
- [ ] Sier de tre snømennene hvert sitt ord i tur og orden?

- [ ] Smelter de bort samtidig og blir helt borte?

- [ ] Blir alle tre snømennene like store og synlige igjen hver gang du trykker på grønt flagg?


Hvis svaret på hvert av de tre spørsmålene er "Ja": Gratulerer, du har klart å fikse alle bugs-ene i koden!

Her er et forslag til hvordan koden til Snømann 1 kan se ut når du er ferdig:

```blocks
Når grønt flagg klikkes
sett størrelse til [100]%
si [Klar] i (2) sekunder
vent (4) sekunder
gjenta (4) ganger
endre [ghost v] effekt med (25)
vent (1) sekunder
endre størrelse med (-10)
```

## Utfordring {.challenge}

Animasjonene og funksjonaliteten i dette lille programmet er jo ganske enkle.

Her er noen tips til ting du kan prøve for å gi programmet litt mer kompleksitet:
- [ ] Lag en algoritme som får snømennene til å gå frem og tilbake på skjermen mens de snakker.

- [ ] Bytt ut "klar, ferdig, smelt!" med en dialog der snømennene for eksempel snakker sammen om hvor varmt det begynner å bli

- [ ] Få snømennene til å si "Hjelp, jeg smelter!" når ghost-effekten begynner.

Lykke til!
#

Når du er ferdig kan du klikke på "Legg ut"-knappen. Da vil det bli lagt ut på Scratch-hjemmesiden din slik at du enkelt
kan dele det med familien og vennene dine.

