# Spillelister
Inkluder en tekstfil (.txt) i denne mappen med filnavn til markdown-filene som
skal inkluderes i spillelisten. Filnavnet til markdown-filene som inkluderes
skal være relativ `..`, altså fra roten av det spesifikke programmeringsspråk.

Navnet på spillelisten blir hentet fra navnet på tekstfilen minus `.txt`.

**Eksempel**
Vi ønsker å lage en spilleliste for Scratch som heter *Roboter er kule* og har
`oppgave1/robot.md` og `oppgave2/robot_med_vinger.md` i scratch-katalogen. Da
lager vi en fil `Roboter er kule.txt` med innholdet:

```
oppgave1/robot.md
oppgave2/robot_med_vinger.md
```
