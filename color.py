import pygame
import time
screen=pygame.display.set_mode()
while 1 :

    screen.fill((0,0,0))
    pygame.display.update()
    screen.fill((254,255,255))
    pygame.display.update()
    pygame.display.toggle_fullscreen()

