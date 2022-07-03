import time
import pygame
from MapTools.Map import Map
from InputTools.InputManager import InputManager

pygame.init()

#Map configuration
map = Map((255, 247, 235), pygame.display.set_mode((600, 600)))
pygame.display.set_caption("Wordle")
map.build()

#Input configuration
input = InputManager(map)

while True:

    if not(input.go):
        map.build()

        input.check_events()
    
        input.write_rects()

        pygame.display.flip()

        time.sleep(1)
        break

    map.build()

    input.check_events()
    
    input.write_rects()

    pygame.display.flip()