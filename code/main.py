import renderer
import client
import pygame
import sys

#Setup Window
window = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Pygame')
clock = pygame.time.Clock()

#Server
username = "DangerMaster451"
client.initialize()

#Create Objects
p = renderer.Player(window)
b = renderer.Block(window)

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

    #Client
    
    client.send(str({"username":username, "pos":[p.x, p.y]}))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()