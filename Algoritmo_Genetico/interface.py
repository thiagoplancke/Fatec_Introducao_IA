import pygame
from algoritmo_genetico import *
from random import randint

pygame.init()


largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo Genético - Visualização")


BRANCO = (255,255,255)
PRETO = (0,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)


def desenhar_individuos(populacao, objetivo):
    tela.fill(BRANCO)  
    
    pygame.draw.circle(tela, VERDE, (objetivo[0]*10, objetivo[1]*10), 8)  

    
    for ind in populacao:
        pos = ind["posicao_final"]  
        pygame.draw.circle(tela, AZUL, (pos[0]*10, pos[1]*10), 5)

    pygame.display.update()



objetivo = [50,50]
populacao = iniciarIndividuos(num_individuos, num_genes)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    populacao = executar_genes(populacao, objetivo)
    desenhar_individuos(populacao, objetivo)

    pygame.time.delay(250)  

    populacao = populacao_nova(melhores(populacao))

