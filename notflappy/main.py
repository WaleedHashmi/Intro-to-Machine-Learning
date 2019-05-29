import pygame
import random

# GAME CLASSES
class Bird ():
    def __init__(self):
        self.r = 20;
        self.y = height/2;
        self.x = 100;
        self.g = 1;
        self.v = 0;
        self.v_max = -10;

    def show (self):
        pygame.draw.circle(screen, WHITE, (int(self.x),int(self.y)), self.r)


    def update (self):
        self.y += self.g
        # print (self.y)

    # def checkCollision(self):
    #     for i in range (len(pipes.length)):
    #         if

class Pipe ():
    def __init__ (self):
        self.pos = random.randint(200,height-200)
        self.offset = 100
        self.top = self.pos - self.offset
        self.bottom = self.pos + self.offset
        self.x = width
        self.w = 20
        self.v = 2

class Game():
    def __init__ (self):
        self.state="none"

    def update(self):
        b.update()

    def display(self):
        b.show()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (width,height) = (400, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy bird machine learning")

# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()

b = Bird()
g = Game()


while not done:
    clock.tick(100)
    g.update()
    g.display()


    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.display.flip()

    print(clock.get_fps())

# Close the window and quit.
pygame.quit()
