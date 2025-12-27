import pygame
from algoritmo_genetico import *
from random import randint
from math import sqrt

pygame.init()

# Configurações da tela
largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo Genético - Visualização")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
CINZA = (200, 200, 200)

# Fonte
font = pygame.font.SysFont(None, 24)

# Variáveis do algoritmo genético
objetivo = [50, 50]
populacao = iniciarIndividuos(num_individuos, num_genes)
geracao = 0

rastro = []

def desenhar_individuos(populacao, objetivo, geracao, rastro):
    tela.fill(BRANCO)

    pygame.draw.circle(tela, VERDE, (objetivo[0]*10, objetivo[1]*10), 15)

    for gen in rastro:
        for pos in gen:
            pygame.draw.circle(tela, CINZA, (pos[0]*10, pos[1]*10), 3)

    melhor_fitness = float('inf')
    melhor_individuo = None
    posicoes_atual = []

    for ind in populacao:
        pos = ind["posicao_final"]
        posicoes_atual.append(pos)
        if ind["fitness"] < melhor_fitness:
            melhor_fitness = ind["fitness"]
            melhor_individuo = pos

    for ind in populacao:
        pos = ind["posicao_final"]
        if pos == melhor_individuo:
            pygame.draw.circle(tela, VERMELHO, (pos[0]*10, pos[1]*10), 6)
        else:
            pygame.draw.circle(tela, AZUL, (pos[0]*10, pos[1]*10), 5)

    texto_geracao = font.render(f"Geração: {geracao}", True, PRETO)
    texto_fitness = font.render(f"Melhor fitness: {melhor_fitness:.2f}", True, PRETO)
    tela.blit(texto_geracao, (10, 10))
    tela.blit(texto_fitness, (10, 30))

    pygame.display.update()
    return posicoes_atual

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    populacao = executar_genes(populacao, objetivo)
    posicoes_atual = desenhar_individuos(populacao, objetivo, geracao, rastro)

    # Adicionar ao rastro
    rastro.append(posicoes_atual)
    if len(rastro) > 5:
        rastro.pop(0)

    # Verificar se algum indivíduo chegou ao objetivo (fitness = 0)
    melhor_fitness = min(ind["fitness"] for ind in populacao)
    if melhor_fitness == 0:
        # Mostrar mensagem na tela
        texto_objetivo = font.render("Objetivo alcançado!", True, VERMELHO)
        tela.blit(texto_objetivo, (largura//2 - 100, altura//2))
        pygame.display.update()
        pygame.time.delay(3000)  # esperar 3 segundos
        running = False
        break

    pygame.time.delay(250)
    populacao = populacao_nova(melhores(populacao))
    geracao += 1
