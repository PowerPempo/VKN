import pygame
pygame.init()

vel_x = 2
vel_y = -1 
FPS = 60
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Electrone by 2Pizza")

class Paddle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

class Electrone:
    def __init__(self, x, y, radius, color, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (self.x, self.y), self.radius)

electron = Electrone(10, HEIGHT // 2, 10, (0, 0, 255), vel_x, vel_y)

def draw():
    WIN.fill((255, 255, 255))
    paddle = Paddle(0, 0, WIDTH, 20, (0, 0, 0))
    paddle.draw(WIN)
    electron.move()
    electron.draw(WIN)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if electron.x >= HEIGHT:
            electron.velocity_x = 0
            electron.velocity_y = 0  
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()