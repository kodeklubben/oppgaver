
import pgzrun

HEIGHT = 400
WIDTH = 600

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'white': (255, 255 ,255),
    'black': (0, 0, 0)
}

class Ball:
    radius = 20
    color = COLORS['red']
    x = WIDTH // 2
    y = HEIGHT // 2
    speed_x = 3
    speed_y = 3

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Check for wall collisions, bounce of wall
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.speed_x = -self.speed_x
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.speed_y = -self.speed_y

    def on_key_down(self, key):
        if key == keys.LEFT:
            self.speed_x -= 1
        elif key == keys.RIGHT:
            self.speed_x += 1
        elif key == keys.UP:
            self.speed_y -= 1
        elif key == keys.DOWN:
            self.speed_y += 1
        elif key == keys.SPACE:
            self.speed_y = self.speed_x = 0




ball1 = Ball()


def draw():
    screen.clear()
    ball1.draw()

def update():
    ball1.update()

def on_key_down(key):
    ball1.on_key_down(key)

pgzrun.go()
