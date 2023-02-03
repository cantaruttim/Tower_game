import pygame
import os
import random
import neat

ai_jogando = True
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

