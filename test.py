import pygame, sys
from pygame.math import Vector2
from UI import *

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = Font("FreeSansBold.ttf", 24)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    font.Draw(screen, "Text", Vector2(0,0), (0,0,0))
    font.Draw(screen, "Text can be centered on a Vector2\nVector2(300,30)", Vector2(300,30), (0,0,0), True)
    pygame.draw.circle(screen,(255,0,0),Vector2(300,30),3)

    font.Draw(screen, "Boxes", Vector2(0,60), (0,0,0))
    Box(Vector2(30,104),Vector2(60,40),(150,150,150),5,center=True).Draw(screen)

    pygame.display.update()
    clock.tick(60)