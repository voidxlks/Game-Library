# eternal-library.py
# OLD VERSION - ETERNAL XLKS GAME LIBRARY

import pygame
import sys

pygame.init()

# Global screen (old style)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eternal XLKS Library")

clock = pygame.time.Clock()
running = True
bg_color = (0, 0, 0)

# --- BASIC FUNCTIONS (no classes, old design) ---

def set_bg(color):
    global bg_color
    bg_color = color

def clear():
    screen.fill(bg_color)

def update(fps=60):
    pygame.display.update()
    clock.tick(fps)

def quit():
    pygame.quit()
    sys.exit()

# --- DRAWING (very basic) ---

def draw_rect(color, x, y, w, h):
    pygame.draw.rect(screen, color, (x, y, w, h))

def draw_circle(color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)

# --- INPUT (simpler, no class) ---

def get_keys():
    return pygame.key.get_pressed()

def get_mouse():
    return pygame.mouse.get_pos()

# --- MAIN LOOP (old style, user passes function) ---

def run(update_func):
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clear()

        # User logic
        update_func()

        update()

    quit()
