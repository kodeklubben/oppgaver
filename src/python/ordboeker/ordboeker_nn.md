---
title: Ordbøker
author: Ole Kristian Pedersen, Kodeklubben Trondheim
translator: Stein Olav Romslo
language: nn
---


# Introduksjon {.intro}

Dette er ei kort oppgåve som viser korleis ein brukar *ordbøker*.


# Nøklar og verdiar {.activity}

Ei ordbok (*dictionary* på engelsk) blir brukt for å lagre *nøkkel/verdi*-par.
Tenk deg at du skal ha ei norsk-engelsk ordbok. Då vil *nøkkelen* vere ordet du
slår opp på, til dømes det norske ordet. *Verdien* er den engelske omsetjinga av
det norske ordet. Til dømes kan nøkkelen vere `"ost"` og verdien vere
`"cheese"`. I Python skriv me ordbøker med krøllparentesar, `{}`, slik som
dette:

```python
>>> d = {'ost':'cheese', 'brød':'bread'}
>>> d
{'ost': 'cheese', 'brød': 'bread'}
```

I dømet over laga me ei norsk-engelsk ordbok til variabelen `d`. Nøkkel og verdi
har eit `:` mellom seg, og `'nøkkel':'verdi'`-para skil me med komma, `,`. For å
slå opp på ein nøkkel brukar me `[nøkkel]`, slik som dette:

```python
>>> d['ost']
'cheese'
```

Me kan bruke den same skrivemåten for å lage ny nøkkel/verdi-par eller endre
verdien som er knytta til ein nøkkel.

```python
>>> d['farge'] = 'colour'

# legg til ein ny verdi
>>> d
{'ost': 'cheese', 'brød': 'bread', 'farge': 'colour'}
>>> d['farge'] = 'color'

# endrar verdien
>>> d
{'ost': 'cheese', 'brød': 'bread', 'farge': 'color'}
```

Du kan opprette ei tom ordbok slik:

```python
>>> d = {}
>>> d
{}
```

**Merk:** Det er berre tekst og tal som kan brukast som nøklar, men verdiane kan
vere kva som helst: strengar, tal, lister, ordbøker, funksjonar, osb.


# Prøv sjølv {.check}

No skal me skrive eit program som let ein brukar lage ei ordbok. Programmet skal
ta imot 3 nøkkel/verdi-par, og så be om ein nøkkel å slå opp på, for så å vise
verdien som høyrer til nøkkelen. Det skal fungere slik:

<pre>
Skriv inn ein nøkkel: <font color="green">ost</font>
Skriv inn ein verdi: <font color="green">cheese</font>
Skriv inn ein nøkkel: <font color="green">brød</font>
Skriv inn ein verdi: <font color="green">bread</font>
Skriv inn ein nøkkel: <font color="green">farge</font>
Skriv inn ein verdi: <font color="green">color</font>
Kva nøkkel vil du slå opp på? <font color="green">brød</font>
Tilhøyrande verdi er bread
</pre>

Dette må du gjere:

- [ ] Lag ei tom ordbok.

- [ ] Bruk ei løkke for å hente inn 3 nøkkel/verdi-par.

- [ ] Lagre nøkkel/verdi-para i ordboka.

- [ ] Spør om ein nøkkel.

- [ ] Skriv ut verdien som høyrer til nøkkelen.


# Gå gjennom ordbøker {.activity}

Du kan bruke ei løkke til å hente ut nøklane til ei ordbok:

```python
>>> d = {'brød': 3, 'ost': 1}
>>> for key in d:
...     print("Nøkkel:", key)
...     print("Verdi:", d[key])
...
Nøkkel: ost
Verdi: 1
Nøkkel: brød
Verdi: 3
```

Viss du berre treng verdiane kan du bruke `d.values()`:

```python
>>> for val in d.values():
...     print("Verdi:", val)
...
Verdi: 1
Verdi: 3
```

Viss du vil få tilgang til både nøkkel og verdi kan du bruke `d.items()`:

```python
>>> for key, value in d.items():
...     print(key, value)
...
ost 1
brød 3
```

## Handleliste {.check}

No skal me lage eit handlelisteprogram som let brukaren velje kva og kor mykje
som skal vere på handlelista. Programmet skal sjå slik ut:

<pre>
Skriv inn ein gjenstand: <font color="green">brød</font>
Kor mange? <font color="green">2</font>
Skriv inn ein gjenstand: <font color="green">tomat</font>
Kor mange? <font color="green">5</font>
Skriv inn ein gjenstand:
Her er handlelista:
2 brød
5 tomat
</pre>

Dette må du gjere:

- [ ] Ta imot input for gjenstand.

- [ ] Så lenge gjenstanden ikkje er ein tom streng `""`:

  - Be om antal.

  - Lagre til ei ordliste.

  - Bruk gjenstanden som nøkkel og antalet som verdi.

- [ ] Skriv ut handlelista.

  **Hint:** Gå gjennom nøklane.
