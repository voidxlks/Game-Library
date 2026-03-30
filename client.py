# client.py
import pygame
from code import App, Input

class Player:
    def __init__(self, x=100, y=100, size=50, color=(0, 200, 255)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 5

    def move(self):
        keys = Input.keys()

        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, app):
        app.draw.rect(self.color, (self.x, self.y, self.size, self.size))


class Client:
    def __init__(self):
        self.app = App(800, 600, "Client Demo")
        self.player = Player()

    def update(self, app):
        # Update player
        self.player.move()

        # Draw player
        self.player.draw(app)

        # Draw mouse pointer
        mx, my = Input.mouse_pos()
        app.draw.circle((255, 255, 0), (mx, my), 8)

    def run(self):
        self.app.run(self.update)


# Run client
if __name__ == "__main__":
    client = Client()
    client.run()
