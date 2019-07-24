import sys,pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

class Color:
    def __init__(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

    def equal(self, color):
        return color.r == self.r and color.g == self.g and color.b == self.b

    def change(self, color):
        if self.r < color.r:
            self.r += 1
        if self.g < color.g:
            self.g += 1
        if self.b < color.b:
            self.b += 1

        if self.r > color.r:
            self.r -= 1
        if self.g > color.g:
            self.g -= 1
        if self.b > color.b:
            self.b -= 1

currentColor = Color()
screen.fill((currentColor.r, currentColor.g, currentColor.b))
while True:
    nextColor = Color()


    while not currentColor.equal(nextColor):
        currentColor.change(nextColor)
        screen.fill((currentColor.r,currentColor.g,currentColor.b))
        pygame.display.update()
        time.sleep(0.0001)
        pass
