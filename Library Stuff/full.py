# full.py
# VOID XLKS - FULL ENGINE (ALL-IN-ONE)

import pygame
import sys

pygame.init()

# -----------------------------
# WINDOW
# -----------------------------
class Window:
    def __init__(self, width=800, height=600, title="Void Full"):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (15, 15, 20)

    def clear(self):
        self.screen.fill(self.bg_color)

    def update(self, fps=60):
        pygame.display.flip()
        self.clock.tick(fps)

    def stop(self):
        self.running = False

    def quit(self):
        pygame.quit()
        sys.exit()


# -----------------------------
# DRAW
# -----------------------------
class Draw:
    def __init__(self, surface):
        self.surface = surface

    def rect(self, color, rect, radius=0):
        pygame.draw.rect(self.surface, color, rect, border_radius=radius)

    def circle(self, color, pos, radius):
        pygame.draw.circle(self.surface, color, pos, radius)

    def text(self, text, pos, size=24, color=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", size)
        render = font.render(text, True, color)
        self.surface.blit(render, pos)


# -----------------------------
# INPUT
# -----------------------------
class Input:
    @staticmethod
    def keys():
        return pygame.key.get_pressed()

    @staticmethod
    def mouse_pos():
        return pygame.mouse.get_pos()


# -----------------------------
# GAME OBJECT SYSTEM
# -----------------------------
class GameObject:
    def __init__(self):
        self.active = True

    def update(self, app):
        pass

    def draw(self, app):
        pass


# -----------------------------
# PLAYER
# -----------------------------
class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.x = 375
        self.y = 275
        self.size = 50
        self.speed = 5
        self.color = (0, 200, 255)

    def update(self, app):
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
        app.draw.rect(self.color, (self.x, self.y, self.size, self.size), radius=10)


# -----------------------------
# APP CORE
# -----------------------------
class App:
    def __init__(self):
        self.window = Window()
        self.draw = Draw(self.window.screen)
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def run(self):
        while self.window.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.stop()

            self.window.clear()

            for obj in self.objects:
                if obj.active:
                    obj.update(self)
                    obj.draw(self)

            # UI text
            self.draw.text("VOID ENGINE FULL VERSION", (10, 10), 20)

            self.window.update()

        self.window.quit()


# -----------------------------
# RUN GAME
# -----------------------------
if __name__ == "__main__":
    app = App()

    player = Player()
    app.add(player)

    app.run()
