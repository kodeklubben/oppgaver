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

# Steg 1: 
