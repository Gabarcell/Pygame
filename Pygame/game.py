import pygame
pygame.init()
x = 400
y = 300
veloc = 10
fundo = pygame.image.load('rua.png')
carro = pygame.image.load('carro_menor.png')

janela = pygame.display.set_mode((750,550))

pygame.display.set_caption("Criando um Pygame...")

open_window = True

while open_window:
    pygame.time.delay(50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    command = pygame.key.get_pressed()
    if command[pygame.K_UP]:
        y -= veloc
    if command[pygame.K_DOWN]:
        y += veloc
    if command[pygame.K_RIGHT]:
        x += veloc
    if command[pygame.K_LEFT]:
        x -= veloc

    janela.blit(fundo, (0,0))
    janela.blit(carro,(x,y))
    #pygame.draw.circle(janela, (0,255,0),(x,y), 30)
    pygame.display.update()

pygame.quit()