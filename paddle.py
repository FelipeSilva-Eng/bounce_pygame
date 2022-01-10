from pygame.sprite import Sprite
from pygame import Surface
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Paddle(Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(
            self.image,
            color,
            [0,0, width, height]
        ) 

        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 500:
            self.rect.y = 500

    
