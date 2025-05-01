import pygame, sys
from pygame.math import Vector2
from UI import *

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = Font("FreeSansBold.ttf", 24)

button = Button(Vector2(80,90),(150,150,150),("Hello",16,"FreeSansBold.ttf",(0,0,0)),print,runArgs=["Hello!"])

slider = Slider(Vector2(250,90),0,99,(0,100),(80,80,80),(180,180,180))

textbox = TextBox(font,Vector2(150,150),Vector2(150,30),(0,0,0),(200,200,200),8)

checkbox = Checkbox(Vector2(400,200),Vector2(30,30),(85,85,200),(200,200,200),(255,255,255),checked=True,borderRadius=10)

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
    Box(Vector2(30,104),Vector2(60,40),(150,150,150),center=True).Draw(screen)

    font.Draw(screen, "Buttons", Vector2(80,60), (0,0,0))
    button.Draw(screen)
    button.Update(events, pygame.mouse.get_pos())

    font.Draw(screen, f"Sliders: {slider.get()}", Vector2(200,60), (0,0,0))
    slider.Draw(screen)
    slider.Update(events, pygame.mouse.get_pos())

    font.Draw(screen, "Textbox", Vector2(150,100), (0,0,0))
    textbox.Draw(screen)
    textbox.Update(events, pygame.mouse.get_pos())

    checkbox.Draw(screen)
    checkbox.Update(events, pygame.mouse.get_pos())

    pygame.display.update()
    clock.tick(60)