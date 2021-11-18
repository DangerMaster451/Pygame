import pygame
import math
import sys

#classes
class Player:
    def __init__(self):
        self.x = 20
        self.y = -20
        self.speed = 10
        self.size = 20

    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed
        elif keys[pygame.K_UP]:
            self.y -= self.speed
        elif keys[pygame.K_DOWN]:
            self.y += self.speed

        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.x -= self.speed / 2
            self.y -= self.speed / 2 
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.x -= self.speed / 2
            self.y += self.speed / 2
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
           self.x += self.speed / 2
           self.y -= self.speed / 2
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.x += self.speed / 2
            self.y += self.speed / 2
        
    def render(self):
        pygame.draw.rect(window, (13, 170, 255), (self.x, self.y, self.size, self.size))

class Block:
    def __init__(self):
        self.x = 375
        self.y = 375
        self.speed = 10
        self.size = 20
    
    def render(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.size, self.size))




#Setup Window
window = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Pygame')
clock = pygame.time.Clock()

#Create Objects
p = Player()
b = Block()
  
#Game Loop
while True:
    #Refresh
    pygame.display.update()
    msElapsed = clock.tick(30)

    #Player
    window.fill((0, 0, 0))
    p.move()
    p.render()
    b.render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

