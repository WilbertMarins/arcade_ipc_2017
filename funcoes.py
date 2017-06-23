import pygame
import random
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((800, 600))

#sistema de cores
WHITE =(255,255,255)
BLUE = (15,171,247)
RED = (255, 0, 0)
GREEN = (36, 217, 46)
YELLOW=(255,255,0)
PINK =(236,19,182)

option = [(80, 80), (80, 100)]

# fonte de texto
font=pygame.font.SysFont

title = font("Arial black", 72)
font_pattern = font("Impact", 30)
font_text = font("Times New Roman", 15)


# textos que aparecerão na tela inicial
title = title.render("Snake", 1, (RED))
game = font_pattern.render("Jogar (aperte 'J')", 1, (WHITE))
credits = font_pattern.render("Sobre (aperte 'S')", 1, (WHITE))
instruction = font_pattern.render("Instruções (aperte 'I')", 1, (WHITE))
instruction2 = font_pattern.render("Voltar ao menu (aperte 'V') ", 1, (WHITE))
#no sobre#
team = font_pattern.render("Equipe de Desenvolvimento:", 1, (WHITE))
name1 = font_pattern.render("Fang Yao", 1, (WHITE))
name2 = font_pattern.render("Ian Gabriel", 1, (WHITE))
name3 = font_pattern.render("Wilbert Luís", 1, (WHITE))
name4 = font_pattern.render("Yuri Leandro", 1, (WHITE))
command = font_pattern.render("Orientação:", 1, (WHITE))
advisor = font_pattern.render("Prof.Dr. Jucimar Jr", 1, (WHITE))

#no jogar#
scoreboard = font_text.render("Score: ",1, YELLOW)

class grafica(object):
    def __init__(self):
        print("e começa o jogo")
        pass
    def background(self):
        screen.fill(WHITE)
        face = pygame.Surface((780, 580))  # criei uma "máscara' com dimensão menor q a tela
        face.fill(BLUE)
        screen.blit(face, [10, 10])

    def title(self, opcoes):
        screen.blit(title, (280, 250))
        screen.blit(game, (100, 400))
        screen.blit(instruction, (100, 450))
        screen.blit(credits, (100, 500))
        pass

    def instruction(self):
        imagem = pygame.image.load('inst.PNG')
        screen.blit(imagem,[175,110])

    def pause(self):
        imagem = pygame.image.load('pause.PNG')
        screen.blit(imagem,[175,110])

    def credits(self):
        screen.blit(team, (30, 70))
        screen.blit(name1, (50, 100))
        screen.blit(name2, (50, 150))
        screen.blit(name3, (50, 200))
        screen.blit(name4, (50, 250))
        screen.blit(command, (30, 300))
        screen.blit(advisor, (50, 350))
        screen.blit(instruction2, (30, 550))


    def viper(self, guindace, item, pontuacao):
        for i in option:
            pygame.draw.rect(screen,GREEN, (i[0]+1, i[1]+1, 18 , 18))
            if option.index(i) == len(option)-1:
                if guindace == 0:
                    option.append((i[0] + 20, i[1]))
                if guindace == 90:
                    option.append((i[0],i[1]-20))
                if guindace == 270:
                    option.append((i[0], i[1]+20))
                if guindace == 180:
                    option.append((i[0] - 20, i[1]))
                if i != item:
                    del option[0]
                    return (item, pontuacao)
                else:
                    pontuacao += 1
                    return ((random.randint(0, 39)*20, random.randint(0, 29)*20), pontuacao)
                break



    def food(self, item):
        pygame.draw.rect(screen, RED, (item[0], item[1], 18, 18))

    def scoreboard(self, pontuacao):
        screen.blit(scoreboard, (10, 10))
        score = font_text.render(str(pontuacao), 1, PINK)
        screen.blit(score, (50, 30))

    def wall(self):
        alto=pygame.Rect(0,0,1,600)
        alto2=pygame.Rect(799,0,1,600)
        largo=pygame.Rect(0,0,799,1)
        largo2=pygame.Rect(0,599,800,1)
        pygame.draw.rect(screen, RED,alto )
        pygame.draw.rect(screen, RED,alto2 )
        pygame.draw.rect(screen, RED,largo )
        pygame.draw.rect(screen, RED, largo2)


