---
title: Kuprat
author: Geir Arne Hjelle
translator: Emil Eldøen
language: en
---

# Introduction {.intro}

In this course we will introduce the programming language Python, which is very popular and used for many things. Python is used by many of the largest and most known companies in the world such as Google, NASA and CERN.

We will start simple by looking at how to make small programs in Python that can read and show text. We will do this by recreating a historical program called [Cowsay](http://www.cowsays.com/)) where a smart cow shares it's wisdom.

![Bilete av ei ASCII-ku som pratar!](kuprat.png)

Translator's note: The cow says "Python is fun!"

# Step 1: Hello world! {.activity}

To ensure Python is working properly we're making a super simple program. We just want to write a simple greeting on the screen.

## Checklist {.check}

- [] Open IDLE, the editor that comes with Python. We will use this to both write and run the programs we are writing.

**Windows**: Open IDLE from the start menu

**Mac**: Open the terminal.app, write `idle` and press ENTER.

**Linux**: Open a terminal, write `idle` and press enter.

This will open a window named "Python Shell". If you cannot find IDLE, or the window won't open, then Python might not be installed properly. If that is the case you can download the latest version of Python from [http://www.python.org/](http://www.python.org/). Do ask for help if needed.

- [ ] If the window `Python Shell` opened you will see the result of your program here. To write a new program we must open a programming window as well. To do this go to the menu, select `File` > `New File`. Make sure both windows are visible as you will be using this to write your actual program.

- [ ] In this new window we will write the following:

    ```python
    print("Hello world!")
    ```

- [ ] Now we save the program and run it. Select `File > Save`, and give your program the name `hello.py`. You can run your program by clicking `Run > Run Module`. You will see that Python has in the first window we opened.

Good job! You have just written, and run, your first Python-program!

## Error messages {.protip}

Python demands precision while programming, and if you write something Python can't understand it will write an error message for you when you try to run it (`Run > Run Module`). You may have already experienced this! If not, you can try to change `print` with `pint`in your code and run it again.

When you get an error message you have to fix your code, and double check you wrote everything correctly. This will be easier as you practice programming, so hang in there!

## Checklist {.check}

- [ ] Our first program only consisted of a single command, the function `print` which is used to tell Python we want to write something to the screen. We insert what we want to write between the parentheses. In this case we wanted Python to write the text `Hello World`. To tell Python that `Hello World` should be interpreted as pure text and not a commando we need to write in quotation marks similar to (")

- [ ] We can easily change what Python writes to the screen. Try changing your program to the following:

    ```python
    print("Hello, everyone!)
    ```

Save the file again and run the program.

## Python-files {.protip}

We have just made a Python-program called `hello` and saved it as a normal text file cwith the name `hello.py`. Python calls such a file for a `module`. You can decide what you want to name your programs, but the files must end with `.py` for Python to recognize them.

It is also a good idea to avoid using special letters (such as Æ Ø Å for Norwegian, or ß for german) and blank spaces in your program names. Instead of empty spaces, please use an underscore `_` instead, like in `hello_world.py`

## Step 2: What is your name? {.activity}

Now we will see how to make Python ask us questions. For this we use another fuction called `input`.

When you use the function `input` the program stops running the code and waits until you have written something and hit enter on your keyboard.

## Checklist {.check}

- [ ] Change your program to look like this:
    ```python
    name = input("what is your name? ")
    print ("Hello, " + name)
    ```

Save and run the program, then write your name or something else after Python asks, then hitt ENTER. Does Python greet you by what you wrote? How does it differ from our previous "Hello World!"?

- [ ] To make the text look better you need to make sure you use spaces. It looks better if you have a space between `?` and `"` in your input function, and a space between `Hello,` snf `"` in the print function. If you skip it you will get the result `Hello,Name`.

- [ ] Notice that in the program we are using something valled a variable, which is `name`. In this case the variable remembers what you wrote for your input, but you could also change it to be a static name or anything you like. We use variables a lot when programming, and are created automatically when we use the `=`
It is up to you to decide what the variables are called, and it is important to choose names that describe what the variable is remembering/used for.

- [ ] Try adding more lines to your program. Maybe Python can ask you other questions like where you live, who your best friend is or perhaps favourite colour? Use variables to remember these inputs so Python can write them back to you afterwards.

## Quick commands {.protip}

Instead of using File and Run to save/run the program, try clicking CTRL + S (cmd + S on mac) to save and F5 to run the program (`fn + F5` on Mac). It is very convenient to use these shortcuts and will save you a lot of time as you are running, testing and fixing (debugginig) code.

# Step 3: Cowtalk {.activity}

Now we are going to make a simple version of the classic program [Cowsay](http://www.cowsays.com), which was made by Tony Monroe, This program will allow us to write a cool cow and make it say whatever we want.

## Checklist {.check}

- [] We start with drawing the cow. Open a new IDLE-window by pressing CTRL + N (`File > New File`) and write the following program:

    ```python
    print('^__^')
    print('(oo)\_______')
    print('(__)\       )')
    print('    ||----W |')
    print('    ||     ||')
    ```

Save the program as `cowtalk.py` and run it. Cool cow isn't it?

- [ ] But now we must make the cow say something. Add and change the lines so it looks good:

    ```python
    print(' _____________________')
    print('< Python is fun! >')
    print(' ---------------------')
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')
    ```

- [ ] Now we can use what we learnt earlier to easily chnage the messages the cow is saying. By using `input` twe can ask what the Cow should say. Change your program to the following:

    ```python
    message = input('Kva skal kua seie? ')

    print(' ____________________')
    print('< ' + message + ' >')
    print(' --------------------')
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')
    ``` 

- [ ] How does the program work when running it now? Try different texts (maybe LONG texts?)

- [ ] As you might see, the cow's speech bubble does not match how long the cow's message actually is, and sometimes becomes too large. To fix this we use another function `len`. (`len` is short for *length*)
  This finds the legnth of a text, to test the function try adding this line right after the `input` line in your program:

    ```python
    print(len(melding))
    ```

- [ ] To draw the speech bubble we can use a Python-trick that can repeat text. We already know we can put together text via `+` like with `"Hello, " + name` To repeat text we must multiply the text with a number, so `"Hello" * 3` becomes `"HelloHelloHello"`. Therefore we can multiplty `"-"` with the length variable to draw it correctly.

- [ ] Change your program so it looks like this:

    ```python
    melding = input('Kva skal kua seie? ')
    boblelengde = len(melding) + 2

    print(' ' + '_' * boblelengde)
    print('< ' + melding + ' >')
    print(' ' + '-' * boblelengde)
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')
    ```

    Save and run the program, is the speech bubble correct?

### Test yourself {.challenge}

Try drawing other animals or figures that can also talk. Or, try changing the Cow's looks. You could try changing the eyes with `--` or add a tongue?

You can also add several unique figures in the same program, try making it look like they're talking together. Experiment and have fun!