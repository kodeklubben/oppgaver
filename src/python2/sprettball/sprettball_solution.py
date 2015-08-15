
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
    dx = 3
    dy = 3

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Check for wall collisions, bounce of wall
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.dx = -self.dx
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.dy = -self.dy

    def on_key_down(self, key):
        if key == keys.LEFT:
            self.dx -= 1
        elif key == keys.RIGHT:
            self.dx += 1
        elif key == keys.UP:
            self.dy -= 1
        elif key == keys.DOWN:
            self.dy += 1
        elif key == keys.SPACE:
            self.dy = self.dx = 0




ball1 = Ball()


def draw():
    screen.clear()
    ball1.draw()

def update():
    ball1.update()

def on_key_down(key):
    ball1.on_key_down(key)
