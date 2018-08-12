---
title: "JS: Hei, JavaScript!"
author: Arve Seljebu
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

I denne oppgåva skal du møte programmeringsspråket JavaScript. Du skal gjere den
klassiske oppgåva *Hallo, verda* med ein katt.

![Bilete av ein ASCII-katt som seier "Mjau, Arve!" i konsollen](jsbin.png)


# Steg 1: Bruke JS Bin {.activity}

Du skal bruke ei nettside som heiter *JS Bin* for å løyse denne oppgåva. JS Bin
er ei nettside som let deg programmere JavaScript. Me kunne ha brukt nettlesaren
din direkte, men i JS Bin blir stega like for alle, uavhengig av om du brukar
Microsoft Edge, Mozilla Firefox, Chrome, Opera, Safari eller ein annan
nettlesar. I tillegg er det mogleg å gjere denne oppgåva på eit nettbrett ved å
bruke JS Bin.

## Tips {.tip}

Her er fleire måtar å køyre JavaScript-kode på:

- Lagre ei `.js`-fil i favoritt-teksteditoren din og åpne den i ein nettlesar.

- Skriv kode mellom `<script> </script>` i `<body>` eller `<head>` i ei
  HTML-fil, og åpne den i ein nettlesar.

- Skrive `<script src="fil_namn.js"></script>` i `<head>`.

## Sjekkliste {.check}

- [ ] Åpne JS Bin (http://jsbin.com/?js,console) i eit eige vindauge.

- [ ] Legg merke til at du får opp to faner; **JavaScript** og **Console**.

- [ ] Koden skal skrivast i **JavaScript**.

- [ ] I **Console** visast tekstbeskjedar som blir skrive ut.

- [ ] Skriv inn denne koden i fana **JavaScript**:

  ```js
  console.log("Hallo, verda");
  ```

- [ ] Trykk `ctrl + enter` (eller bruk knappen <button>Run</button>) og sjå kva
  som skjer i **Console**.

- [ ] Kan du endre koden til å skrive namnet ditt?

## Forklaring {.tip}

Her er ei forklaring til koden over:

- `console.log()` tyder at me ynskjer å køyre kommandoen med namnet
  `console.log`. Den skriv ut det som er mellom parentesene til `log()` i
  konsollen.

- `.log` er ein av fleire utskriftsmetodar. Prøv `console.error`. Ser du kva som
  skil den frå `console.log`?

- Tekst som blir skrive ut til konsollen ligg mellom hermeteikn (`"`), slik som
  `"Hallo, verda"`.

- `;` tyder at kodesetninga er ferdig.


# Steg 2: Lage ein funksjon {.activity}

Ein funksjon er nesten som ei oppskrift. Ein brukar funksjonar for å kunne bruke
same kode fleire gonger, eller bryte opp eit problem til mindre bitar. Ein
funksjon kan både ta imot og gi frå seg (returnere) data. Funksjonen din skal
heite `hei`, ta imot eit `namn` og skrive namnet til konsollen.

## Sjekkliste {.check}

- [ ] Slett koden din frå steg 1.

- [ ] Skriv inn denne koden:

  ```js
  function hei(namn) {
    console.log(namn);
  }
  ```

## Forklaring {.tip}

- `function hei` tyder at funksjonen skal heite `hei`.

- `(namn)` tyder at me kan sende inn data til funksjonen. `namn` blir ein
  variabel, og heldt på ein verdi som me kan endre. Me skal sjå meir på dette
  seinare.

- `{` markerer starten til funksjonen.

- `}` markerer slutten til funksjonen.

- Mellom `{` og `}` er det som funksjonen skal gjere.

## Sjekkliste {.check}

- [ ] Akkurat no gjer ikkje funksjonen så mykje, men la oss teste den likevel.
  Skriv dette etter funksjonen:

  ```js
  hei("Emma");
  hei("Jens");
  ```

- [ ] `hei("Emma")` tyder at me skal køyre funksjonen og sende inn `"Emma"`.

- [ ] Trykk `ctrl + enter` for å køyre koden.

- [ ] Ser du både `"Emma"` og `"Jens"` i konsollen?

Koden til no:

```js
function hei(namn){
    console.log(namn)
}

hei("Emma");
hei("Jens");
```

## Tips {.tip}

Du kan slette historia i **Console** ved å trykkje på knappen
<button>Clear</button>, eller leggje inn `console.clear();` i koden din.


# Steg 3: Hei, namn! {.activity}

I steg 2 gjorde me ikkje noko anna enn det som `console.log` gjer. No skal du få
`hei("Emma")` til å skrive ut `"Hei, Emma!"`.

## Sjekkliste {.check}

- [ ] I JavaScript kan me leggje saman tekst med `+`.

- [ ] La oss endre funksjonen `hei`:

  ```js
  function hei(namn) {
    console.log("Hei, " + namn + "!");
  }
  ```

- [ ] Her har me lagt saman `"Hei, "`, namnet som blir sendt inn og `"!"`

- [ ] Køyr koden din.

- [ ] Står det `"Hei, Emma!"` og `"Hei, Jens!"` i **Console**?

- [ ] Kan du endre koden slik at den skriv ut namnet ditt?

## Forklaring {.tip}

I funksjonen `hei` vil `namn` vere ein variabel. Den heldt på ein verdi, og
denne verdien kan endrast. Fyrst er `namn` det same som `Emma`, og så blir
`namn` til `Jens`. Variablar er veldig nyttig i programmering, og me kjem til å
bruke variablar mykje framover.


# Steg 4: Katten seier hei {.activity}

I dette siste steget skal du lage ein katt som seier hei.

## Sjekkliste {.check}

- [ ] Bytt ut `function hei` ved å kopiere koden under:

  ```js
  function hei(namn) {
    console.log("< Mjau, " + namn + "! >                 ");
    console.log("    \\                           ");
    console.log("      /\\___/\\                   ");
    console.log("     (  o o  )                  ");
    console.log("      \\ =0= /                   ");
  }
  ```

- [ ] Køyr `hei` med ditt eige namn.

- [ ] Er det ein katt som seier mjau til deg i konsollen?

- [ ] Klarar du å lage ein hund eller eit anna dyr?

## Bakoverstrek {.tip}

`\` brukast til spesielle bokstavar. Til dømes tyder `\n` *ny linje*. Difor må
du skrive `\\` viss du vil ha ein vanleg bakoverstrek.


# Steg 5: Dele prosjektet {.activity}

Kanskje hadde det vore kult å sende ei kattehelsing til nokre av dei beste
venene dine? La oss lage ei personleg helsing til kvar av dei!

## Sjekkliste {.check}

- [ ] Syt for at du køyrer `hei` med namnet til venen din:

  ```js
  hei("Namnet til venen din");
  ```

- [ ] Hald inne `ctrl + S` for å lagre.

- [ ] Legg merke til at det no står eit tal i adressa. Talet er versjonen av
  programmet ditt.

  **Versjon 9:** <img height="25" src="versjon.png" alt="Skjermbilete som viser
  at me har versjon 9">

  Kvar gong du endrar programmet og trykkar `ctrl + S` får programmet ein ny
  versjon. Slik kan du lage fleire variantar av same program, med ulike namn.

- [ ] Trykk på **JavaScript** slik at kodefana blir skjult:

  <img height="35" src="faner.png" alt="Bilete av fanene">

- [ ] Trykk på <button>Run</button> og sjekk at det ser riktig ut.

- [ ] Kopier nettaddressa og del med venen din.

- [ ] Gjenta stega for fleire av venene dine.

- [ ] Viss du vil åpne prosjektet att seinare kan du berre ta vare på ei av
  lenkene du sendte til venene dine.

## Ei anna måte å dele programmet {.tip}

Hugsar du oppgåva [HTML: Publiser nettsida di](../publiser/publiser_nn.html)?
Kanskje du kan laste opp JavaScript-koden til `GitHub`-sida di? Eit lite tips er
å leggje JavaScript-koden inn i `<head>`-taggen ved å bruke desse taggane:

```html
<script>
</script>
```

Du kan òg lagre JavaScript-koden i ei eiga `.js`-fil, til dømes `katt.js`. Så
kan du referere til den frå ei HTML-fil på denne måten:

```html
<head>
    <script src="katt.js"></script>
</head>
```

Hugs at `katt.js` må liggje i same mappe som HTML-fila. Dette skal me prøve ut
seinare.

For at dette skal fungere må me skrive om `console.log()` til:

```js
document.writeln();
```

Denne kommandoen skriv rett på HTML-sida og ikkje i `konsollen`. På denne måten
kan venene dine sjå koden utan å åpne `konsollen`. Problemet med
`document.writeln()` er at me ikkje får kvar utskrift på ei eiga linje, så me må
leggje til denne CSS-en:

```js
document.body.style.whiteSpace = "pre"; //gjer at du kan ha fleire mellomrom etter kvarandre
```

`document.writeln()` legg til eit linjeskift etter at den har skrive ut teksten.
Viss du ikkje ynskjer det kan du bruke `document.write()`.

No ser koden slik ut:

```js
function hei(namn) {
    document.writeln("< Mjau, " + namn + "! >                 ");
    document.writeln("    \\                           ");
    document.writeln("      /\\___/\\                   ");
    document.writeln("     ( o o  )                  ");
    document.writeln("      \\ =0= /                   ");
}
document.body.style.whiteSpace = "pre";
```


# Steg 6: Lagre prosjektet på datamaskina di {.activity}

Det er mogleg å laste ned prosjektet og lagre det på datamaskina di. La oss
gjere det.

## Sjekkliste {.check}

- [ ] Trykk på **File** > **Download**.

- [ ] Ei `.html`-fil blir lasta ned.

- [ ] Når fila er lastet ned åpnar du fila.

- [ ] Du får opp eit tomt vindauge, og utskrifta av katten blir sendt til
  konsoll. La oss åpne konsollen i nettlesaren din.

- [ ] **Chrome og Firefox:** Trykk på knappen **F12**. Vel **Console**.

- [ ] **Internet Explorer og Microsoft Edge:** Trykk på knappen **F12**. Vel
  **Konsoll**.

- [ ] I konsollen skal du sjå katten mjaue til deg.

  ![Bilete av ASCII-katten som mjauar til deg](konsoll.png)

  Viss du ikkje ser katten, gjer neste steg.

- [ ] Skriv inn `hei("Namnet ditt");` og trykk **Enter**.

- [ ] Kva skjer?

__Gratulerer!__ Du har skrive ditt fyrste JavaScript-program!
