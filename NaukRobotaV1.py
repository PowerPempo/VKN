import pygame
import sys

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Натисніть 'SPACE' для запуску/зупинки")

electron_color = (0, 0, 255)  # Синій
cathode_color = (255, 0, 0)   # Червоний

anode_x, anode_y = 50, height // 2
cathode_x, cathode_y = width - 50, height // 2

electron_x, electron_y = anode_x, anode_y

running = True
paused = False  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused  

    if not paused:  
        if electron_x < cathode_x:
            electron_x += 2  

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 0), (anode_x, anode_y), 10)
    pygame.draw.circle(screen, cathode_color, (cathode_x, cathode_y), 10)
    pygame.draw.circle(screen, electron_color, (electron_x, electron_y), 5)

    pygame.display.flip()

    pygame.time.delay(10)

pygame.quit()
sys.exit()
