# code.py
import pygame
import sys

# Initialize pygame
pygame.init()

class Window:
    def __init__(self, width=800, height=600, title="My Game"):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (30, 30, 30)

    def set_background(self, color):
        self.bg_color = color

    def clear(self):
        self.screen.fill(self.bg_color)

    def update(self, fps=60):
        pygame.display.flip()
        self.clock.tick(fps)

    def quit(self):
        pygame.quit()
        sys.exit()


class Draw:
    def __init__(self, surface):
        self.surface = surface

    def rect(self, color, rect):
        pygame.draw.rect(self.surface, color, rect)

    def circle(self, color, pos, radius):
        pygame.draw.circle(self.surface, color, pos, radius)

    def line(self, color, start, end, width=1):
        pygame.draw.line(self.surface, color, start, end, width)


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


class App:
    def __init__(self, width=800, height=600, title="App"):
        self.window = Window(width, height, title)
        self.draw = Draw(self.window.screen)

    def run(self, update_func):
        while self.window.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.running = False

            self.window.clear()

            # Call user update function
            update_func(self)

            self.window.update()

        self.window.quit()
