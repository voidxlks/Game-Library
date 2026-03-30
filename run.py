# run.py
import pygame
from code import App, Input

# Player settings
player_x = 400
player_y = 300
speed = 5

def update(app):
    global player_x, player_y

    keys = Input.keys()

    # Movement (WASD)
    if keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_s]:
        player_y += speed
    if keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_d]:
        player_x += speed

    # Draw player
    app.draw.rect((0, 200, 255), (player_x, player_y, 50, 50))

    # Draw mouse circle
    mx, my = Input.mouse_pos()
    app.draw.circle((255, 255, 0), (mx, my), 10)


# Create app
app = App(800, 600, "My Pygame Library Demo")

# Run game
app.run(update)
