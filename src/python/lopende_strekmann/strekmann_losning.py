WIDTH = 550
HEIGHT = 250
SCORE = 0
JUMP_TIME = 0.25

class Box:
    def __init__(self, x=WIDTH, y=HEIGHT, size=50, color=(255,0,0)):
        x = x
        y = y-size
        self.color = color
        self.rect = Rect(x, y, size, size)

    def draw(self):
        screen.draw.filled_rect(self.rect, self.color)


box = Box(color=(0,0,255))
stick_man = Actor('running_man')
stick_man.bottomleft = 50, HEIGHT
stick_man.hit = False

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    stick_man.draw()
    box.draw()
    screen.draw.text("Poeng: " + str(SCORE), (400, 30), color=(0,0,0))


def update():
    global SCORE
    box.rect.x -= 10

    # ute av bildet
    if box.rect.x < -box.rect.width:
        if not stick_man.hit:
            SCORE += 10
        stick_man.hit = False
        box.rect.x = WIDTH

    # boks treffer strekmann
    if (box.rect.left < stick_man.right and
            box.rect.right > stick_man.left and
            box.rect.top < stick_man.bottom):
        SCORE = 0
        stick_man.hit = True
        

def on_key_down(key):

    if (key == keys.SPACE and
            stick_man.bottom == HEIGHT):
        jump_height = HEIGHT - box.rect.height*1.5
        jump = animate(stick_man, 'decelerate', duration=JUMP_TIME, bottom=jump_height)
        jump.on_finished = back_down

def back_down():
    animate(stick_man, 'accelerate', duration=JUMP_TIME, bottom=HEIGHT)

