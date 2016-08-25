--- 
title: "JS: Partikkel-fest"
level: 3
---

# Introduksjon {.intro}
Denne oppgaven bygger på koden du skrev i oppgaven [Partikkel-animasjon](../partikkel_animasjon/partikkel_animasjon.html). Så dersom du ikke har gjort den, så anbefaler vi å gjøre [Partikkel-animasjon](../partikkel_animasjon/partikkel_animasjon.html) før du fortsetter på denne oppgaven. 

Her skal vi videreutvikle `partikkel`-animasjonen vår slik at den blir noe sånt: 

<canvas id="canvas" width="500" height="500"></canvas>

<script>


        var canvas, ctx;
        var partikkelListe = [];
        
        var drawInterval = setInterval(function(){draw()}, 30);


        
        

        window.onload = function(){
            canvas = document.getElementById("canvas");
            ctx = canvas.getContext("2d");
            drawInterval;
        };


        //Tegner og skyter particle opp
        function draw(){
            
            var particle = {
                x: 250,
                y: 250,
                xSpeed: Math.floor(Math.random()*20 - Math.random()*20),
                ySpeed: Math.floor(Math.random()*20 - Math.random()*20),
                size: 10

            };
            
            partikkelListe.push(particle);
            
            ctx.clearRect(0,0,500,500);

            
            for (var i=0; i<partikkelListe.length; i++) {
                particle = partikkelListe[i];
            

                
                ctx.fillStyle = 'red';
                ctx.fillRect(particle.x, particle.y,particle.size,particle.size);;
            
                particle.x = particle.x + particle.xSpeed;
                particle.y = particle.y + particle.ySpeed;
            
                particle.size = particle.size * 0.96;
            }

        }
</script>

# Steg 1: Hva må gjøres? {.activity} 
I denne oppgaven får du kun små eksmepler på kode for å hjelpe deg til å komme frem til resultatet. Dersom skal vi nå gå gjennom tankemåten å presentere en liste over ting som må gjøres for å få animasjonen til å bli som den er vist over.

La oss studere animasjonen litt og analysere hva den inneholder:
+ Et partikkel i midten av skjermen som alltid er der
+ Partiklene som går ut fra midten og blir mindre og mindre jo lengre ut de går
+ Hastigheteni til hvert partikkel varierer
+ Retningen varierer, men et partikkel har en reiser i en rett linje
+ Det er mange partikler som blir til hvert sekund

La oss analysere punktene over, starter fra toppen:
+ Siden partiklene går ut fra midten må jo alle starte der, derfor må vi setter `x`- og `y`-posisjonen til å være det samme for hvert parikkel. 
+ Siden partiklene blir mindre og mindre, men starter med samme størrelse, må vi endre på `størrelser`-attributtet til partiklet på samme måte som vi gjør når vi skal flytte på det. Tips: bruk ganging (`*`) for å få en jevnere minskning
+ Siden hastigheten varierer kan vi bruke `Math.random` til `xSpeed` og `ySpeed`, her er et forslag til hvordan det kan se ut:
```js
xSpeed: Math.floor(Math.random()*20 - Math.random()*20));
```
Dette vil gjøre at du får et positivt eller negativt tall med varierende hastighet fra -20 til 20 i `x`-retning. Gjør det samme for `y`-retningen for å få partiklene til å gå over alt! 

+ For å få dem til å følge en rett linje bruker vi bare endringer i `x`- og `y`-retning fra forrige oppgave: `particle.x = particle.x + particle.xSpeed;`.
+ Siden det er mange som blir laget på engang må vi for hver gang `draw()` blir kalt på legge et nytt partikkel i en `liste` og bruke en `for`-løkke som endrer hvert partikkel sine attributter for hvert element i `for`-løkken. 


#### Prøv selv først! Dersom du ikke får det til kan du benytte deg av hintene under.

# Hint {.activity}
## For-løkke {.tip}
+ En `for`-løkke som skal gå gjennom en liste vil se slik ut:
```js
for(var i = 0; i<listeNavn.length; i++){
    //kode
    element = listeNavn[i] // element blir nå det i-te elementet i listen, "i" blir her et tall fra 0 til lengden av listen. 
}
```
##



