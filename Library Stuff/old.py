# old.py
# VERY OLD VERSION - VOID / ETERNAL EARLY BUILD

import pygame
pygame.init()

# --- GLOBALS (messy old style) ---
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Old Void Engine")

clock = pygame.time.Clock()

x = 100
y = 100
speed = 5

running = True

# --- MAIN LOOP (no structure at all) ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill((0, 0, 0))

    # input (very basic)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    # draw player (hardcoded)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

    # update screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
