import pygame
import random
from pygame.locals import*
pygame.init()
window = pygame.display.set_mode((780, 580))

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

title2 = font("Arial black", 72)
font_pattern = font("Impact", 30)
font_text = font("Times New Roman", 15)


# textos que aparecerão na tela#
title = title2.render("Snake", 1, (RED))
play = font_pattern.render("Jogar (aperte 'J')", 1, (WHITE))
credit = font_pattern.render("Sobre (aperte 'S')", 1, (WHITE))
instruction = font_pattern.render("Instruções (aperte 'I')", 1, (WHITE))
instruction2 = font_pattern.render("Voltar ao menu (aperte 'V') ", 1, (WHITE))
#no sobre#
team = font_pattern.render("Equipe de Desenvolvimento:", 1, (WHITE))
name1 = font_pattern.render("Fang Yao", 1, (WHITE))
name2 = font_pattern.render("Ian Gabriel", 1, (WHITE))
name3 = font_pattern.render("Wilbert Luís", 1, (WHITE))
name4 = font_pattern.render("Yuri Leandro", 1, (WHITE))
commands = font_pattern.render("Orientação:", 1, (WHITE))
advisor = font_pattern.render("Prof.Dr. Jucimar Jr", 1, (WHITE))

#no jogar#
scoreboard = font_text.render("Score: ",1, YELLOW)
class graphic(object):
    def __init__(self):
        print("e começa o jogo")
        pass
    def background(self):
        window.fill(WHITE)
        face = pygame.Surface((780, 580))  # criei uma "máscara' com dimensão menor q a tela
        face.fill(BLUE)
        window.blit(face, [10, 10])

    def title (self, opcoes):
        window.blit(title, (280, 250))
        window.blit(play, (100, 400))
        window.blit(instruction, (100, 450))
        window.blit(credit, (100, 500))

        pass

    def instruction(self):
        image = pygame.image.load('inst.PNG')
        window.blit(image,[175,110])

def pause(self):
        image = pygame.image.load('pause.PNG')
        window.blit(image,[175,110])

    def credit(self):
        window.blit(team, (30, 70))
        window.blit(name1, (50, 100))
        window.blit(name2, (50, 150))
        window.blit(name3, (50, 200))
        window.blit(name4, (50, 250))
        window.blit(commands, (30, 300))
        window.blit(advisor, (50, 350))
        window.blit(instruction2, (30, 550))


    def snake(self, orientation, item, punctuation):
        for i in option:
            pygame.draw.rect(window,GREEN, (i[0]+1, i[1]+1, 18 , 18))
            if option.index(i) == len(option)-1:
                if orientation  == 0:
                    option.append((i[0] + 20, i[1]))
                if orientation == 90:
                    option.append((i[0],i[1]-20))
                if orientation == 270:
                    option.append((i[0], i[1]+20))
                if orientation == 180:
                    option.append((i[0] - 20, i[1]))
                if i != item:
                    del option[0]
                    return (item, punctuation)
                else:
                    punctuation += 1
                    return ((random.randint(0, 39)*20, random.randint(0, 29)*20), punctuation)
                break

    def food(self, item):
        pygame.draw.rect(window, RED, (item[0], item[1], 18, 18))

    def scoreboard(self, punctuation):
        window.blit(scoreboard, (10, 10))
        point = font_text.render(str(punctuation), 1, PINK)
        window.blit(point, (50, 30))

    def wall(self):
        high=pygame.Rect(0,0,1,600)
        high2=pygame.Rect(799,0,1,600)
        large=pygame.Rect(0,0,799,1)
        large2=pygame.Rect(0,599,800,1)
        pygame.draw.rect(window, RED,high )
        pygame.draw.rect(window, RED,high2 )
        pygame.draw.rect(window, RED,large )
        pygame.draw.rect(window, RED, large2)

    
