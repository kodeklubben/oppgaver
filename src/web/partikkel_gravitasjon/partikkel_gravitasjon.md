---
title: "JS: Partikkel-gravitasjon"
level: 3
---

# Introduksjon {.intro}
I denne oppgaven skal vi ta utgangspunkt i animasjone vi lagde i  oppgaven (Partikkel-animasjon)[../partikkel_animasjon/partikkel_animasjon.html]. Dersom du ikke har gjort denne oppgaven anbefaler vi deg om å gå tilbake å gjøre den før du fortsetter her.

Oppgaven i dag går ut på å legge til gravitasjon på `Partikkel`-objektet. Til slutt kommer det til å se noe slik ut: 

<script>


        var canvas, ctx;
        
        var drawInterval = setInterval(function(){draw()}, 30);


        var particle = {
            x: 125,
            y: 0,
            gravity: 0.05,
            gravitySpeed: 0,
            size: 10

        };

        window.onload = function() {
            canvas = document.getElementById("canvas");
            ctx = canvas.getContext("2d");
        };


        function draw() {
            ctx.clearRect(0,0,250,250);

            ctx.fillStyle = 'red';
            ctx.fillRect(particle.x, particle.y,particle.size,particle.size);
            
            particle.gravitySpeed += particle.gravity;
            particle.y = particle.y + particle.gravitySpeed;
            
            kant = canvas.height - particle.size;
            if(particle.y > kant){
                particle.y = kant; 
                particle.gravitySpeed = 0;
            
                setTimeout(function() { particle.y = 0; }, 2000);
            }
            
        }

</script>

<canvas id="canvas" width="250" height="250"></canvas>

