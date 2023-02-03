import pygame
import os

ai_jogando = False
geracao = 0

TELA_LARGURA = 500
TELA_ALTURA = 800


IMAGEM_TOWER = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'Tower.png')))
IMAGEM_ENEMY = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'enemy.png')))
IMAGEM_ENEMYFIRE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'enemy fire.png')))
IMAGEM_ENEMYCHEFE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'enemy chefe.png')))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Tower:
    IMGS = IMAGEM_TOWER
    ROTACAO_MAXIMA = 360
    VELOCIDADE_ROTACAO = 20
    TEMPO = 5


    def __init__(self, attack, defense, shooting_speed, money, coins):
        self.attack = attack
        self.defense = defense
        self.shooting_speed = shooting_speed
        self.money = money
        self.coins = coins


    def shoot(self):
        self.shooting_speed = self.shooting_speed
        self.attack = self.attack
        self.fire = 50



    def desenhar_tela(tela):
        tela.blit(0, 0)

        for torre in torres:
            torre.desenhar(tela)

        pygame.display.update()



"""

        texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
        tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))


"""
"""

    if ai_jogando:
        texto = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 10))

"""