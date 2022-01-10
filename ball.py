import pygame
from random import randint

from pygame.surface import Surface

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(
            self.image,
            color,
            [0, 0, width, height]
        )

        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)

    def reset(self):
        self.rect.x = 400
        self.rect.y = 300

    def play_music(self):
        pygame.mixer.music.load('musics/blipSelect.wav')
        pygame.mixer.music.play()

    def reset_ball_song(self):
        pygame.mixer.music.load('musics/pickupCoin.wav')
        pygame.mixer.music.play()