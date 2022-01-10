from ball import Ball
from paddle import Paddle
import pygame


# Inicializa todos os módulos que precisam ser inicializados
pygame.init()

# Definição de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# abrindo uma nova janela
size = (700, 500)
screen = pygame.display.set_mode(size, vsync=1)
pygame.display.set_caption('Pong')

# vai controlar a taxa de atualização dos elementos da tela por segundo
clock = pygame.time.Clock()


paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


# game score
scoreA = 0
scoreB = 0

# game loop
while True:
    # main loop do game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    # logica do jogo vai aqui
    all_sprites_list.update()
    
    # desenhando a linha que separa os players
    screen.fill(BLACK)

    # desenha a linha
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 2)

    # desenha todos os sprites de uma vez
    all_sprites_list.draw(screen)

    # mostrar scores na tela
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))
    

    # atualiza a tela com o que desenhamos
    pygame.display.update()

    # bouncing algorithm
    if ball.rect.x >= 690:
        scoreA += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x < 0:
        scoreB += 1
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Bounce when the ball hits the paddle
    if pygame.sprite.collide_mask(
        ball, paddleA
    ) or pygame.sprite.collide_mask(
        ball, paddleB
    ):
        ball.bounce()

    # limita para 60 frames por segundo
    clock.tick(60)

    