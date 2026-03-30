# void-library.py
# MODERN VERSION - VOID XLKS GAME LIBRARY

import pygame
import sys

pygame.init()

# -----------------------------
# WINDOW SYSTEM
# -----------------------------
class Window:
    def __init__(self, width=800, height=600, title="Void Library"):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (15, 15, 20)

    def set_background(self, color):
        self.bg_color = color

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
# DRAW SYSTEM
# -----------------------------
class Draw:
    def __init__(self, surface):
        self.surface = surface

    def rect(self, color, rect, border_radius=0):
        pygame.draw.rect(self.surface, color, rect, border_radius=border_radius)

    def circle(self, color, pos, radius):
        pygame.draw.circle(self.surface, color, pos, radius)

    def line(self, color, start, end, width=2):
        pygame.draw.line(self.surface, color, start, end, width)

    def text(self, text, pos, size=24, color=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", size)
        render = font.render(text, True, color)
        self.surface.blit(render, pos)


# -----------------------------
# INPUT SYSTEM
# -----------------------------
class Input:
    @staticmethod
    def keys():
        return pygame.key.get_pressed()

    @staticmethod
    def mouse_pos():
        return pygame.mouse.get_pos()

    @staticmethod
    def mouse_pressed():
        return pygame.mouse.get_pressed()


# -----------------------------
# OBJECT SYSTEM (NEW)
# -----------------------------
class GameObject:
    def __init__(self):
        self.active = True

    def update(self, app):
        pass

    def draw(self, app):
        pass


# -----------------------------
# APP / ENGINE CORE
# -----------------------------
class App:
    def __init__(self, width=800, height=600, title="Void App"):
        self.window = Window(width, height, title)
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

            # Update & Draw objects
            for obj in self.objects:
                if obj.active:
                    obj.update(self)
                    obj.draw(self)

            self.window.update()

        self.window.quit()


# -----------------------------
# BUILT-IN PLAYER OBJECT
# -----------------------------
class Player(GameObject):
    def __init__(self, x=100, y=100, size=50, color=(0, 200, 255)):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 5

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
        app.draw.rect(self.color, (self.x, self.y, self.size, self.size), border_radius=8)
