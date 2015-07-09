import pygame.draw
import math
import random
import string

##################
# global constants

# total number of tries
TRIES = 7

# the available words
WORDS = ["koding", "kodeklubb", "python", "hangman"]

##################
# global variables

# contains the game state
state = {}


def create_display_string(secret_word, remaining_letters):
    """Creates the hidden word as it is displayed to the player"""

    # insert a space between each letter
    display_string = " ".join(list(secret_word))

    for letter in remaining_letters:
        display_string = display_string.replace(letter, '_')
    return display_string


def start_game():
    """Set the correct game state"""
    state["running"] = True
    state["used_tries"] = 0
    state["secret_word"] = random.choice(WORDS)
    state["pressed_button"] = ""
    state["help_text"] = "Guess a letter!"
    state["remaining_letters"] = []
    for i, letter in enumerate(string.ascii_letters):
        if i >= 26:
            break
        state["remaining_letters"].append(letter)
    state['display_string'] = create_display_string(state['secret_word'], state['remaining_letters'])


def main():
    """Runs every time the clock ticks"""
    letter = state["pressed_button"].lower()
    if letter in state["remaining_letters"]:
        state["remaining_letters"].remove(letter)
        if letter in state["secret_word"]:
            state['display_string'] = create_display_string(state['secret_word'], state['remaining_letters'])
        else:
            state["used_tries"] += 1

    if state["used_tries"] >= 7:
        state['help_text'] = "You lost!"
        game_over()
    elif state["display_string"].count("_") == 0:
        state['help_text'] = "You won!"
        game_over()


def game_over():
    """Runs when the game is over"""

    state["running"] = False
    state['display_string'] = create_display_string(state['secret_word'], [])


start_game()

###############################################################################
# Library code
###############################################################################
# The library declares the needed functions for drawing, and handling keyboard
# events.


# window height and window width
WIDTH = 1000
HEIGHT = 600

def update():
    if state.get("running", False):
        main()

def draw():
    """Draws the screen each time the clock ticks"""

    screen.clear()

    if state.get("running", None) is None:
        return

    # width of drawn line
    LINE_WIDTH = 3

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    ##################
    # helper functions
    def draw_head():
        screen.draw.filled_circle((250 - LINE_WIDTH // 2, 100), 25, WHITE),
        screen.draw.filled_circle(
            (250 - LINE_WIDTH // 2, 100), 25 - LINE_WIDTH, BLACK)

    def draw_body():
        screen.draw.filled_rect(
            Rect((250 - LINE_WIDTH // 2, 125), (LINE_WIDTH, 100)), WHITE)

    def draw_left_arm():
        pygame.draw.line(
            screen.surface, WHITE,
            (250, 150), (210, 120),
            LINE_WIDTH)

    def draw_right_arm():
        pygame.draw.line(
            screen.surface, WHITE,
            (250, 150), (290, 120),
            LINE_WIDTH)

    def draw_right_leg():
        pygame.draw.line(
            screen.surface, WHITE,
            (250, 225), (280, 290),
            LINE_WIDTH)

    def draw_left_leg():
        pygame.draw.line(
            screen.surface, WHITE,
            (250, 225), (220, 290),
            LINE_WIDTH)

    def draw_face():
        pygame.draw.arc(
            screen.surface, WHITE,
            Rect((225, 105), (50, 50)),
            math.pi / 3, 2 * math.pi / 3,
            LINE_WIDTH)
        pygame.draw.line(screen.surface, WHITE,
                         (237, 92), (245, 92),
                         LINE_WIDTH)
        pygame.draw.line(screen.surface, WHITE,
                         (255, 92), (263, 92),
                         LINE_WIDTH)

    def draw_base():
        hangman_base = (
            Rect((100, 50), (3, 300)),
            Rect((25, 350), (150 + LINE_WIDTH, LINE_WIDTH)),
            Rect((100, 50), (150, LINE_WIDTH)),
            Rect((250 - LINE_WIDTH, 50), (LINE_WIDTH, 25))
        )
        for rect in hangman_base:
            screen.draw.filled_rect(rect, WHITE)

    # end helper functions
    ######################

    # draw the base and body parts
    draw_base()
    body_parts = [draw_head, draw_body, draw_right_leg, draw_left_leg,
                  draw_left_arm, draw_right_arm, draw_face]
    for i in range(state['used_tries']):
        body_parts[i]()

    # fill the lower textbox
    screen.draw.text(state["display_string"], fontsize=100,
                     centerx=WIDTH//2, centery=5*HEIGHT//6)

    # display help text
    screen.draw.text(state["help_text"], fontsize=80, width=500,
                     centerx=WIDTH//2, centery=200)

    # display remaining letters
    screen.draw.text("Remaining letters:", fontsize=40, width=300,
                     centerx=850, top=50)
    screen.draw.text("   ".join(state["remaining_letters"]),
                     fontsize=50, width=250,
                     centerx=850, top=150)


def on_key_down(key):
    """Handles key presses"""
    if not state["running"]:
        return
    if key.name.isalpha():
        state["pressed_button"] = key.name
