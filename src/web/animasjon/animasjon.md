---
title: "CSS: Animasjon"
level: 3
language: nb-NO
---

# Introduksjon {.intro}
I denne oppgaven skal du lære å animerer HTML-objekter ved hjelp av CSS. Under ser du hvordan resultatet til slutt vil bli: 

![](ressurser/out.gif)

Men før vi starter å lage animasjonen over må vi lære litt om hvordan animasjon fungerer ved hjelp av CSS. 

# Steg 1: Animasjons-attributtet {.activity}

Animasjon i CSS er ganske enkelt, i utgangspunktet har animasjonen 2 stadier: `start` og `slutt`. Mellom `start` og `slutt` kan du legge inn forskjellige faser, som vi skal se på litt senere. Animasjonen vil heller ikke gå i `loop` (altså gjenta seg selv) med mindre du forteller at den skal gjøre det. 

Før vi skal se på et enkelt eksempel skal vi se på `animation`-attributtet (property). Dette attributtet inneholder følgende:

- `name`: navnet på animasjonen
- `duration`: hvor lang(i sekunder) skal animasjonen være
- `timing-function`: hvordan mellom-fasene er kalkulert
- `delay`: hvor mye forsinkelse det skal være før animasjonen starter
- `iteration-count`: hvor mange ganger skal animasjonen gjentas
- `direction`: bestemmer om animasjonen skal gå baklengs eller ikke
- `fill-mode`: hvilke stiler som er lagt til før og etter start av animasjonen

Her er et enkelt eksempel på en boks som går fra venstre til høyre:

<style>
    
    #boks{
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        
        animation: frem_og_tilbake 2s 0s infinite alternate both;
    }
    
    
    @keyframes frem_og_tilbake{
        0%{
            left: 0px;
            top: 0px;
        }
        100%{
            left:100px; 
            top: 0px;
        }
        
    }

</style>

<div id="boks"></div>
<br>


```html
<!DOCTYPE html>
<html>
<head>
<style>
    
    #boks{
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        
        animation: frem_og_tilbake 2s 0s infinite alternate both;
    }
    
    
    @keyframes frem_og_tilbake{
        0%{
            left: 0px;
            top: 0px;
        }
        100%{
            left:100px; 
            top: 0px;
        }
        
    }

</style>
</head>
<body>
    <div id="boks"></div>
</body>
</html>

```

__La oss se nærmere på koden over:__

Vi har en `<div>` med ID `boks`, den er 50x50px med blå bakgrunnsfarge. Posisjonen er `relative` som vil si at vi kan flytte på den.

`Animation`-attributtet:
- `name`: frem_og_tilbake
- `duration`: 2s (sekunder)
- `timing-function`: blank, siden vi ikke trenger den
- `delay`: 0s
- `iteration-count`: infinite (uendelig, så den vil ikke stoppe)
- `direction`: alternate (for at den skal gå frem og tilbake)
- `fill-mode`: both (samme stil på start og slutt)

`@keyframes navn_på_animasjonen` er det vi bruker for å spesifisere hva som skal skje under animasjonen. I dette tilfellet heter heter animasjonen `frem_og_tilbake`. Siden det står `0%` betyr dette når animasjonen starter og `100%` betyr når animasjonen er ferdig. Derfor vil animasjonen vår starte i `left: 0px; top: 0px;` og ende i `left: 100px; top 0px;`. 

__NB!__ Verdiene i `animation`-attributtet kan også skrives som et eget attributt på denne måten: 
```css
#boks{
    animation-name: frem_og_tilbake;
    animation-duration: 2s;
    animation-delay: 0s;
    ...
}
```

## Utfordring {.challenge}
- Få animasjonen til å bytte farge fra blå til rød underveis.
- Klarer du å få boksen til å flytte seg nedover og oppover?
- Prøv å få boksen til å bevege seg i en firkant


# Steg 2: @keyframes {.activity}

La oss nå se litt nærmere på `@keyframes` og hva vi trenger å gjøre for å få animasjon.

`@keyframes` forteller CSS at vi skal starte en animasjon, måten vi kan animere på er å legge inn CSS i `@keyframes`.

Her kommer noen eksempler:
<style>
    
    #diagonalt{
        height: 50px;
        width: 50px;
        background-color: green;
        position: relative;
        
        animation: diagonalt 2s 0s infinite;
    }
    
    
    @keyframes diagonalt{
        from{top: 0px; left: 0px; }
        to{top: 100px; left: 100px; }  
    }

</style>

<div id="diagonalt"></div>
<br>
<br>
<br>
<br>
<br>

```css
@keyframes diagonalt{
    from{top: 0px; left: 0px; }
    to{top: 100px; left: 100px; }
}
```
Dette eksempelet får et objekt til å gå diagonalt siden det skal starte på `top: 0px; left: 0px` og ende på `top: 100px; left: 100px;`. 

<style>
    
    #ned{
        height: 50px;
        width: 50px;
        background-color: red;
        position: relative;
        
        animation: ned 2s 0s infinite;
    }
    
    
    @keyframes ned{
        from{top: 0px;}
        to{top: 100px;}  
    }

</style>

<div id="ned"></div>
<br>
<br>
<br>
<br>
<br>

```css
@keyframes ned{
    0%{top: 0px}
    100%{top: 100px}
}
```
Her går vil HTML-objektet går nedover. 


<style>
    
    #skifte_farge{
        height: 50px;
        width: 50px;
        background-color: blue;
        position: relative;
        
        animation: skifte_farge 5s 0s infinite;
    }
    
    
    @keyframes skifte_farge{
        0%{background-color: blue}
        50%{background-color:yellow}
        100%{background-color:red} 
    }

</style>

<div id="skifte_farge"></div>
<br>

```css
@keyframes skift_farge{
    0%{background-color: blue}
    50%{background-color:yellow}
    100%{background-color:red}
}
```
Merk at i dette eksempelet har vi lagt inn en `50%`. Dette er et eksempel på at du kan dele inn animasjonen faser mellom `0%` og `100%`.

__MERK!__ Dersom du ikke får til animasjonen kan det hende at du har en litt for __gammel nettleser__. Dette kan løses ved å installere den nyeste versjonen av nettleseren eller skrive følgende foran alt som har med animasjonen å gjøre:

```css
-webkit-animation-name: ...;
-webkit-animation: name 0s ...;
...

@-webkit-keyframes{

}
```

Det kan være lurt å ha begge deler også slik at absolutt alle nettlesere vil kunne kjøre animasjonen:

```css
@-webkit-keyframes{
    from{...}
    to{...}
}
@keyframes{
    from{...}
    to{...}
}
```
# Steg 3: Minecraft {.activity}
Nå skal vi begynne å animere den animasjonen du så på starten av oppgaven.

+ Last ned [minecraft_animasjon.zip](minecraft_animasjon.zip)
+ Åpne `index.html` i din favoritt teksteditor
+ Åpne `index.html` i nettleseren

Du vil nå ha en nettside som ser noe sånt ut:

![minecraft](ressurser/minecraft_1.png){width=100%}

I koden til `index.html` har vi 3 div-er med følgende ID: `pickaxe`, `minecraft` og `block`. Alle disse ID-ene er et bilde på siden, bakgrunnsbildet ligger under `body` i CSSen. 

La oss nå prøve å få litt animasjon på bildene, men hva vil vi? 

1. Vi vil at `pickaxe`-en skal komme flyvende inn å treffe blokkene
2. Når den har truffet blokkene vil vi at logoen skal komme inn

# Steg 4: Flyvende øks {.activity}

Nå skal vi få `pickaxe`-en til å fly.

Legg til følgende under `#pickaxe`:
+ Legg til `move_pickaxe` som animasjonsnavn
+ Legg til `duration` på `2s`
+ Legg til et `delay` på `1s`
+ Sett `timing-function` til `linear`
+ Sett `fill-mode` til `forwards`

Nå skal vi lage `keyframes`: 
+ Lag en `@keyframes` med samme animasjonsnavn som du satte over
+ La figuren starte utenfor skjermen (Hint: bruk en negativ verdi av `left`)
+ La `pickaxe`-bildet bevege seg bort til blokkene. Klarer du å finne ut hvor langt det er? (Hint: positiv verdi av `left`)
+ Legg til rotasjon `transform: rotate(antall grader)`. Kan du tenke deg hvor du bør ha rotasjonen? I `0%` eller `100%`?
+ Prøv deg frem med hvor mange grader du trenger for at den skal bli riktig. Husk: 360 grader er én gang rundt seg selv. 

<style>
    
    #pickaxe {
        background-image: url("ressurser/pickaxe.png");
        z-index: 1;
        width: 150px;
        height: 150px;
        position: relative;

        
        animation: move_pickaxe 2s;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        animation-iteration-count: infinite;
    }
    
    
     @keyframes move_pickaxe{
        0%{
            left:0px;
        }
        100%{
            left: 800px;
            transform: rotate(720deg);
        }
    }

</style>

<div id="pickaxe"></div>


<toggle>
<strong>Forslag til kode sålangt</strong>
<hide>

    #pickaxe {
        background-image: url("pickaxe.png");
        z-index: 1;
        width: 150px;
        height: 150px;
        position: absolute;
        bottom: 150px;
        left: -150px;
        
        animation: move_pickaxe 2s;
        animation-delay: 1s;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
    }

    @keyframes move_pickaxe{
        0%{
            left:-150px;
        }
        100%{
            left: 800px;
            transform: rotate(720deg);
        }
    }
    
</hide>
</toggle>

# Steg 5: Flyvende logo {.activity}
Nå som du har klart å få `pickaxe` til å fly inn med rotasjon er oppgaven din nå å få `#minecraft` til komme flyvende inn etter at `pickaxe` har stoppet. 

+ Bruk det du har lært i oppgaven til å og prøv få logoen til å komme inn når `pickaxe` er ferdig med sin animasjon.


<style>
    
    #minecraft{
        background-image: url("ressurser/minecraft.png");
        z-index: 1;
        width: 616px;
        height: 154px;
        position: absolute;
        left: -900px;
        
        animation: move_minecraft 4s; /* Chrome, Safari, Opera */
        animation-delay: 1s;
        animation-fill-mode: forwards;
        animation-iteration-count: infinite;
    }
    
    
    @keyframes move_minecraft{
        0%{
            left: -900px;
        }
        100%{
            left:250px; 
        }
        
    }
</style>


<div id="minecraft"></div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<toggle>
<strong>Forslag til kode for Minecraft-logo</strong>
<hide>

    #minecraft{
        background-image: url("minecraft.png");
        z-index: 1;
        width: 616px;
        height: 154px;
        position: absolute;
        left: -900px;
        
        animation: move_minecraft 4s;
        animation-delay: 3s;
        animation-fill-mode: forwards;
    }

    @keyframes move_minecraft{
        0%{
            left: -900px;
        }
        100%{
            left:400px; 
        }
        
    }
    
</hide>
</toggle>