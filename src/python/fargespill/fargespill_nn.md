---
title: Fargespel
author: Omsett frå usingpython.com
translator: Stein Olav Romslo
language: nn
---


# Introduksjon

Hjernen vår er lett å lure, og det kan av og til vere vanskeleg for den å tolke
ulike intrykk samstundes. I spelet me skal lage no vil du både få testa hjernen
og skrivehastigheita di. Me skal lage eit fargespel!

![Illustrasjon av eit ferdig fargespel](fargespill.png)


# Steg 1: Klargjer og importerer biliotek {.activity}

I dette spelet skal me lage eit grafisk brukargrensesnitt (engelsk: Graphic User
Interface - GUI). Til dette brukar me eit bibliotek som heiter `tkinter`. Me
treng òg hjelp for å generere tilfeldige tal.

## Sjekkliste {.check}

- [ ] Åpne IDLE og lag ei ny fil.

- [ ] La oss importere biblioteka. Skriv inn følgjande kode:

  ```python
  import tkinter
  from random import randint
  ```

- [ ] Etter kvart vil me bruke bokstavar som *æøå*. For å gjere det må me leggje
  til noko øvst i koden vår. Gjer om koden din så den ser slik ut:

  ```python
  #!/usr/bin/python
  # -*- coding: UTF-8 -*-
  import tkinter
  from random import randint
  ```

## Kommentering av kode {.protip}

For å gjere koden lettare å forstå kan me leggje inn kommentarar som ikkje
påverkar programmet. Det gjer me ved å skrive inn teiknet `#`. All tekst som
kjem på same line etter dette teiknet blir ignorert av datamaskina, men er
veldig fint for å hjelpe oss menneske. Frå no brukar me dette for å forklare kva
som skjer, men du treng ikkje å skrive inn kommentarane viss du ikkje vil!


# Steg 2: Lage grafisk brukargrensesnitt {.activity}

No skal me starte på GUI. Les kommentarane for å forstå kva som skjer.

## Sjekkliste {.check}

- [ ] Me skal starte med å lage hovudvindauget. Dette kallar me `root`. Me
  kallar funksjonar frå `tkinter`-biblioteket for å hjelpe oss med dette. Legg
  til det følgjande nedst i koden:

  ```python
  root = tkinter.Tk()

  root.title("Fargespel")
  root.geometry("475x300")

  root.mainloop()
  ```

- [ ] No har me laga hovudvindauget. La oss leggje til nokre felt med tekst. Me
  kjem tilbake til kva me skal fylle dei med etter kvart, no skal me berre
  definere områda. Gjer om koden din så det ser slik ut:

  ```python
  #!/usr/bin/python
  # -*- coding: UTF-8 -*-

  import tkinter
  from random import randint

  root = tkinter.Tk()

  root.title("Fargespel")
  root.geometry("475x300")

  # Lagar ein label kalla instructions med tekst:
  instructions = tkinter.Label(root,
                               text="Skriv inn farga PÅ ordet, ikkje sjølve ordet!",
                               font=('Helvetica', 15))
  instructions.pack()

  points_label = tkinter.Label(root,
                               text="Trykk enter for å starte.",
                               font=('Helvetica', 30))
  points_label.pack()

  label = tkinter.Label(root, font=('Helvetica', 100))
  label.pack()

  box = tkinter.Entry(root)

  root.mainloop()
  ```

## I koden over skjer det mykje, la oss sjå på nokre delar {.protip}

Koden `tkinter.Label` lagar eit felt i vindauget vårt. I desse felta kan me
setje inn tekst eller tal. Koden `.pack` fortel programmet vårt at den skal
"teikne" desse felta slik at dei synast for oss, og kor den skal teikne dei.
Koden `tkinter.Entry(root)` lagar eit tekstfelt som spelaren kan skrive i.

## Test prosjektet {.flag}

- [ ] Køyr koden.

- [ ] Viser den et vindauge?

Det er framleis ganske lite som skjer, la oss gå vidare.


# Steg 3: Me lagar tidskontroll {.activity}

## Sjekkliste {.check}

- [ ] No skal me få programmet vårt til å telje 30 sekund. Me lagar ein funksjon
  `countdown()` som tek seg av det. Legg til dette i programmet ditt:

  ```python
  def countdown():
      global time_left

      if time_left > 0:
          # Tel ned eitt sekund
          time_left = time_left - 1
          time_label.config(text="Tid igjen: " + str(time_left))

          # Denne køyrer automatisk countdown() att etter 1 sekund
          time_label.after(1000, countdown)
      else:
          time_label.pack_forget()
          label.pack_forget()
          box.pack_forget()
  ```

- [ ] Denne funksjonen jobbar på ein global variabel `time_left`, me må lage
  den. No skal programmet ditt sjå slik ut:

  ```python
  #!/usr/bin/python
  # -*- coding: UTF-8 -*-

  import tkinter
  from random import randint

  time_left = 30

  def countdown():
      global time_left

      if time_left > 0:
          time_left = time_left - 1
          time_label.config(text="Tid igjen: " + str(time_left))
          time_label.after(1000, countdown)
      else:
          time_label.pack_forget()
          label.pack_forget()
          box.pack_forget()

  root = tkinter.Tk()

  root.title("Fargespel")
  root.geometry("475x300")

  # Lagar ein label kalla instructions med tekst:
  instructions = tkinter.Label(root,
                               text="Skriv inn farga PÅ ordet, ikkje sjølve ordet!",
                               font=('Helvetica', 15))
  instructions.pack()

  points_label = tkinter.Label(root,
                               text="Trykk enter for å starte.",
                               font=('Helvetica', 30))
  points_label.pack()


  label = tkinter.Label(root, font=('Helvetica', 100))
  label.pack()

  box = tkinter.Entry(root)

  root.mainloop()
  ```


# Steg 4: Definere fargane {.activity}

No må me definere fargane som programmet skal bruke.

## Sjekkliste {.check}

- [ ] Me legg til fargane som ei liste. Legg til denne koden under `from random
  import randint`

  ```python
  colours_eng = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                 'Yellow', 'Orange', 'Purple', 'Brown']
  ```

- [ ] Sidan me vil at programmet vårt skal skrive ut dei norske orda lagar me ei
  liste til, med dei norske namna. Legg til dette rett under den andre lista.

  ```python
  colours = ['Raud', 'Blå', 'Grøn', 'Rosa', 'Svart',
             'Gul', 'Oransje', 'Lilla', 'Brun']
  ```

- [ ] Me må lage ein variabel for å halde orden på kor mange poeng spelaren har,
  og ein variabel for å halde nummeret på farga som skal synast. Desse blir sett
  til eit tilfeldig tal etterpå. Legg til desse over `time_left`-variabelen.

  ```python
  # Brukast til å velje tilfeldig farge
  colour = 0
  points = 0
  ```

- [ ] No må me lage funksjonen som genererer ei tilfeldig farge og viser den til
  spelaren. Her er det mykje som skjer, så me skal ta det stegvis. Fyrst
  definerer me funksjonen og legg til variablane. Legg denne funksjonen over
  `countdown()`:

  ```python
  def next_color():
      # Hentar inn globale variablar:
      global points
      global colour
  ```

- [ ] Så skal me setje tekstboksen brukaren kan skrive i aktiv viss det er tid
  att på klokka. Legg til denne inne i `next_color()`:

  ```python
  if time_left > 0:
      box.focus_set()
  ```

- [ ] Så vil me samanlikne det brukaren skriv inn i tekstboksen med den norske
  fargelista vår. Koden `.lower()` gjer om alt til små bokstavar, slik at ein
  ikkje for feil for å skrive "Raud" i staden for "raud". Legg til dette under:

  ```python
  # Viss det spelaren skreiv er riktig farge.
  if box.get().lower() == colours[colour].lower():
      # Pluss på eitt poeng
      points = points + 1
  ```

- [ ] No vil me slette det som brukaren skreiv inn, slik at alt er klart for
  neste runde. Legg til dette under `points = points + 1`:

  ```python
  box.delete(0, tkinter.END)
  ```

- [ ] No skal me få `tkinter` til å vise farge og tekst. Til dette brukar me
  `randint()`-funksjonen. Den lagar eit tilfeldig tal mellom to ytterpunkt. Lag
  denne under `box.delete(0, tkinter.END)`

  ```python
  # Lagar tilfeldig tal mellom 0 og 8.
  colour = randint(0, len(colours)-1)

  # Lagar tilfeldig tal til teksten.
  text = randint(0, len(colours)-1)
  ```

- [ ] No står det berre att å vise teksten og farga i vindauget. Me oppdaterer
  felta og legg til ein poenglabel. Funksjonen skal sjå slik ut:

  ```python
  def next_color():
      global points
      global colour

      if time_left > 0:
          box.focus_set()

      if box.get().lower() == colours[colour].lower():
          points = points + 1

      box.delete(0, tkinter.END)

      colour = randint(0, len(colours)-1)
      text = randint(0, len(colours)-1)

      # Oppdaterer labels
      label.config(fg=str(colours_eng[colour]), text=str(colours[text]))
      points_label.config(text="Poeng: " + str(points))
  ```

## Test prosjektet {.flag}

- [ ] Køyr koden. Får du nokon feilmeldingar?

- [ ] Viss du får feilmeldingar: prøv å sjå etter kor dei er og fiks dei.


# Steg 5: La oss starte programmet! {.activity}

Det skjer framleis lite i spelet vårt, men det er fordi me ikkje har starta
sjølve speldelen. Det skal me gjere no!

## Sjekkliste {.check}

- [ ] Me lagar ein funksjon som startar spelet. Legg til denne funksjonen i
  programmet:

  ```python
  def start_game(event):
      if time_left == 30:
          countdown()
      next_color()
  ```

- [ ] Siste steg er å køyre denne funksjonen når spelaren trykkar *enter*. Legg
  til dette rett over `root.mainloop`:

  ```python
  # Køyrer funksjonen start_game() når enter blir trykka
  root.bind('<Return>', start_game)
  box.pack()
  box.focus_set()
  ```

- [ ] Programmet ditt skal no sjå slik ut:

  ```python
  #!/usr/bin/python # -*- coding: UTF-8 -*-
  import tkinter
  from random import randint


  colours_eng = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                 'Yellow', 'Orange', 'Purple', 'Brown']
  colours = ['Raud', 'Blå', 'Grøn', 'Rosa', 'Svart',
             'Gul', 'Oransje', 'Lilla', 'Brun']
  colour = 0

  points = 0

  time_left = 30


  def start_game(event):
      if time_left == 30:
          countdown()
      next_color()


  def next_color():
      global points
      global colour

      if time_left > 0:
          box.focus_set()

      if box.get().lower() == colours[colour].lower():
          points = points + 1

      box.delete(0, tkinter.END)

      colour = randint(0, len(colours)-1)
      text = randint(0, len(colours)-1)

      label.config(fg=str(colours_eng[colour]), text=str(colours[text]))
      points_label.config(text="Poeng: " + str(points))


  def countdown():
      global time_left

      if time_left > 0:
          time_left = time_left - 1
          time_label.config(text="Tid igjen: " + str(time_left))
          time_label.after(1000, countdown)
      else:
          time_label.pack_forget()
          label.pack_forget()
          box.pack_forget()


  root = tkinter.Tk()

  root.title("Fargespel")
  root.geometry("475x300")

  instructions = tkinter.Label(root,
                               text="Skriv inn farga PÅ ordet, ikkje sjølve ordet!",
                               font=('Helvetica', 15))
  instructions.pack()

  points_label = tkinter.Label(root,
                               text="Trykk enter for å starte.",
                               font=('Helvetica', 30))
  points_label.pack()

  time_label = tkinter.Label(root,
                             text="Tid igjen: " + str(time_left),
                             font=('Helvetica', 30))
  time_label.pack()

  label = tkinter.Label(root, font=('Helvetica', 100))
  label.pack()

  box = tkinter.Entry(root)

  root.bind('<Return>', start_game)
  box.pack()
  box.focus_set()

  root.mainloop()
  ```

## Test prosjektet {.flag}

- [ ] Startar spelet og nedteljinga når du trykkar enter?

- [ ] Får du ny farge etter at du har skrive inn eit svar?

- [ ] Får du poeng når du skriv riktig farge på ordet?

- [ ] Sluttar programmet etter 30 sekund?
