import pygame

import random

pygame.init()

sw,sh = 400,400

screen = pygame.display.set_mode((sw,sh))

pygame.display.set_caption('Welcome to coler changing game')

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  
color = random_color()

sc = pygame(200,200,30,30)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if sc.collidepoint(event.pos):

                color = random_color()

    screen.fill((255,255,255))

    pygame.draw.circle(screen,color,sc)

    pygame.display.flip()

pygame.quit()
