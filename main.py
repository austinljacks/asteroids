import pygame as pyg
from constants import *

s_height = SCREEN_HEIGHT
s_width = SCREEN_WIDTH

def main():
    pyg.init()
    screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return  # this will break the loop
        screen.fill((0,0,0))
        pyg.display.flip()
main()
