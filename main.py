from paddle import Paddle
from ball import Ball

import pygame
from pygame.transform import scale

pygame.init()

# colors to use into the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (800, 600)

# set_mode é o que cria a superficie (screen) em si
screen = pygame.display.set_mode(size, vsync=0)
fundo = scale(
    pygame.image.load('images/background.png'), 
    size
) # faz resize da imagem para caber na tela do jogo
pygame.display.set_caption('Pong')


paddleA = Paddle(WHITE, 15, 100)
paddleA.rect.x = 5
paddleA.rect.y = 250

paddleB = Paddle(WHITE, 15, 100)
paddleB.rect.x = 780
paddleB.rect.y = 250

ball = Ball(WHITE, 15, 15)
ball.rect.x = 400
ball.rect.y = 300

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while True:

    # espaço de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Move paddles
    keys = pygame.key.get_pressed()
    # moves paddleA
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    # moves paddleB    
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    # bouncing the ball
    if ball.rect.x > 785:
        scoreA += 1
        ball.reset_ball_song()
        ball.reset()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.reset_ball_song()
        ball.reset()
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 585:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # colision between ball and paddle
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.play_music()
        ball.bounce()

    # espaço do display
    screen.blit(
        fundo,
        (0, 0)
    ) # atualiza o buffer de memoria, junta varias imagens em uma

    # desenha na tela nossos paddles e atualiza eles
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # desenhar pontuação na screen
    font = pygame.font.Font(None, 74)

    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))

    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (450, 10))


    pygame.display.update() # buffer de video

    clock.tick(60)