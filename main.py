import time
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import random
import numpy as np
from lander import Lander
from config import moon

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 700
BACKGROUND_COLOR = (255, 255, 255)
CHAR_COLOR = (0,0,0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luna Lander")

# initialize lander
l1 = Lander((0, 1735000), moon)
fuel = []
x = []
h = []

# fonts
pygame.font.init()
my_font = pygame.font.SysFont('Courier New', 10)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # lander
    l1.step(1.6,0,0,0,0)
    running = not l1.landed
    print(l1.h)

    text_surface1 = my_font.render("Height:"+str(l1.h), False, CHAR_COLOR)
    text_surface2 = my_font.render("x:"+str(l1.x), False, CHAR_COLOR)
    text_surface3 = my_font.render("fuel:"+str(l1.fuel), False, CHAR_COLOR)

    screen.blit(text_surface1, (10,10))
    screen.blit(text_surface2, (10,60))
    screen.blit(text_surface3, (10,110))
    # Update the display
    pygame_widgets.update(events)
    pygame.display.flip()


    time.sleep(1)

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()