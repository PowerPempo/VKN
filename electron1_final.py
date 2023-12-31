import pygame
import sys
import random

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Натисніть 'SPACE' для запуску/зупинки")

electron_color = (0, 0, 255)  # Синій
cathode_color = (255, 0, 0)   # Червоний

anode_x, anode_y = 50, height // 2
cathode_x, cathode_y = width - 50, height // 2
electron_x, electron_y = anode_x, anode_y
electron_direction = 1

running = True
paused = False

def reset_electron():
    global electron_x, electron_y, electron_direction
    electron_x = anode_x
    electron_y = anode_y
    electron_direction = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        if electron_x < cathode_x and electron_direction == 1:
            electron_x += 2
        elif electron_x > anode_x and electron_direction == -1:
            electron_x -= 2

        if electron_x >= cathode_x:
            reset_electron()

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 0), (anode_x, anode_y), 10)
    pygame.draw.circle(screen, cathode_color, (cathode_x, cathode_y), 10)

    if not paused:
        pygame.draw.circle(screen, electron_color, (electron_x, electron_y), 5)

    pygame.display.flip()

    pygame.time.delay(5)

pygame.quit()
sys.exit()
