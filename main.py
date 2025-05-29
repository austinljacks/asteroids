#Imports
import pygame as pyg
from constants import *
from circleshape import *
from player import *

#Screen Resolution
s_height = SCREEN_HEIGHT
s_width = SCREEN_WIDTH

#Game loop initiailization with clock and delta to improve performance
def main():
    pyg.init()
    clock = pyg.time.Clock()
    dt = 0
    

    screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#Logic to exit, update display, and update delta.
    running = True

    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return  # this will break the loop
        screen.fill((0,0,0))
        pyg.display.flip()
        dt = clock.tick(60) / 1000

main()
