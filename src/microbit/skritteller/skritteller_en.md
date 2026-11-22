---
title: Step Counter
author: Erik Sagatun
translator: Claude
language: en
---
# Introduction {.intro}

Did you know that your phone can count your steps? It uses a sensor called an **accelerometer**, which notices when it is shaken or moved. The micro:bit has exactly the same sensor! In this project we will make a step counter that you can attach to your shoe or keep in your pocket.

When you are done, you can take a walk around the schoolyard and see how many steps you have taken.

# Step 1: Count steps {.activity}

Every time you take a step, the micro:bit is shaken a little. We will use that to count.

## Checklist {.check}

- [ ] Open [MakeCode for micro:bit](https://makecode.microbit.org){target=_blank} and create a new project called `Step Counter`.

- [ ] Go to `Variables`{.microbitvariables} and make a variable called `steps`.

- [ ] Get the `on shake`{.microbitinput} block from `Input`{.microbitinput}.

- [ ] Inside it, put `change steps by 1`{.microbitvariables} and `show number`{.microbitbasic}, like this:

```microbit
let steps = 0
input.onGesture(Gesture.Shake, function () {
    steps += 1
    basic.showNumber(steps)
})
```

## Test your project {.flag}

**Download the code to your micro:bit, or test it in the simulator by clicking the SHAKE button.**

- [ ] Does the number go up by 1 every time you shake the micro:bit?

- [ ] What happens when the number gets bigger than 9? Do you notice that it takes longer to show it?

# Step 2: Only show the number when you want to {.activity}

When the number gets big, the micro:bit spends a long time scrolling it across the screen. While it does that, it might miss some steps! Instead, we will make it blink briefly for every step, and only show the number when you press button A.

## Checklist {.check}

- [ ] Remove `show number`{.microbitbasic} from `on shake`{.microbitinput}.

- [ ] Add `plot`{.microbitled}, a short `pause`{.microbitbasic} and `unplot`{.microbitled} instead. Use x = 2 and y = 2, which is the light in the middle.

- [ ] Make a new `on button A pressed`{.microbitinput} block that shows how many steps you have taken:

```microbit
let steps = 0
input.onGesture(Gesture.Shake, function () {
    steps += 1
    led.plot(2, 2)
    basic.pause(50)
    led.unplot(2, 2)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(steps)
})
```

## Test your project {.flag}

- [ ] Does the light in the middle blink for every step?

- [ ] Does the micro:bit show the right number of steps when you press A?

# Step 3: Reset the counter {.activity}

Before a new walk, it is a good idea to start from zero again.

## Checklist {.check}

- [ ] Add `on button B pressed`{.microbitinput}.

- [ ] Inside it, use `set steps to 0`{.microbitvariables} and show an icon, so you can see that it worked:

```microbit
let steps = 0
input.onButtonPressed(Button.B, function () {
    steps = 0
    basic.showIcon(IconNames.Yes)
    basic.pause(500)
    basic.clearScreen()
})
```

## Test your project {.flag}

- [ ] Shake a few times, press B, and then press A. Does it show 0?

# Step 4: Set yourself a goal {.activity}

Now the step counter will celebrate when you reach a goal, for example 100 steps.

## Checklist {.check}

- [ ] Make a new variable called `goal`, and set it to 100 in `on start`{.microbitbasic}.

- [ ] In `on shake`{.microbitinput}, use `if`{.microbitlogic} to check whether `steps` is equal to `goal`.

- [ ] Play a tune with `start melody`{.microbitmusic} and show a happy face:

```microbit
let steps = 0
let goal = 100
input.onGesture(Gesture.Shake, function () {
    steps += 1
    led.plot(2, 2)
    basic.pause(50)
    led.unplot(2, 2)
    if (steps == goal) {
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        basic.showIcon(IconNames.Happy)
        basic.pause(1000)
        basic.clearScreen()
    }
})
```

## Test your project {.flag}

- [ ] Change `goal` to 5 while you are testing, so you don't have to shake 100 times.

- [ ] Does the micro:bit play a tune and show a happy face when you reach the goal?

- [ ] Attach the micro:bit and battery pack to your shoe and walk exactly 20 steps. How many steps does it show?

## Challenge {.challenge}

Can you make the step counter show how far you have walked in metres? One step is about 0.6 metres for a child aged 10 to 12. Can you also use `radio`{.microbitradio} to send your steps to another micro:bit, so your class can have a step competition?

## Tip {.protip}

Does the micro:bit count too many or too few steps? Try using `acceleration (mg)`{.microbitinput} instead of `on shake`{.microbitinput}, and only count when the value is bigger than a limit you choose yourself, for example 1500.

## Save your project {.save}

Well done! You have made your own step counter. Remember to save your project in MakeCode. Attach the micro:bit to your shoe or keep it in your pocket, and see how many steps you take during one break!
