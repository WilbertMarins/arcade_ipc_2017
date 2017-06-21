import pygame
import random
from pygame.locals import*
pygame.init()
janela = pygame.display.set_mode((780, 580))

#sistema de cores
WHITE =(255,255,255)
BLUE = (15,171,247)
RED = (255, 0, 0)
GREEN = (36, 217, 46)
YELLOW=(255,255,0)
PINK =(236,19,182)

opcao = [(80, 80), (80, 100)]

# fonte de texto
font=pygame.font.SysFont

title = font("Arial black", 72)
font_pattern = font("Impact", 30)
font_text = font("Times New Roman", 15)


# textos que aparecerão na tela#
titulo = title.render("Snake", 1, (RED))
jogar = font_pattern.render("Jogar (aperte 'J')", 1, (WHITE))
sobre = font_pattern.render("Sobre (aperte 'S')", 1, (WHITE))
instrucao = font_pattern.render("Instruções (aperte 'I')", 1, (WHITE))
instrucao2 = font_pattern.render("Voltar ao menu (aperte 'V') ", 1, (WHITE))
#no sobre#
equipe = font_pattern.render("Equipe de Desenvolvimento:", 1, (WHITE))
nome1 = font_pattern.render("Fang Yao", 1, (WHITE))
nome2 = font_pattern.render("Ian Gabriel", 1, (WHITE))
nome3 = font_pattern.render("Wilbert Luís", 1, (WHITE))
nome4 = font_pattern.render("Yuri Leandro", 1, (WHITE))
comando = font_pattern.render("Orientação:", 1, (WHITE))
orientador = font_pattern.render("Prof.Dr. Jucimar Jr", 1, (WHITE))

#no jogar#
placar = font_text.render("Score: ",1, YELLOW)
class grafica(object):
    def __init__(self):
        print("e começa o jogo")
        pass
    def fundo(self):
        janela.fill(WHITE)
        face = pygame.Surface((780, 580))  # criei uma "máscara' com dimensão menor q a tela
        face.fill(BLUE)
        janela.blit(face, [10, 10])

    def titulo(self, opcoes):
        janela.blit(titulo, (280, 250))
        janela.blit(jogar, (100, 400))
        janela.blit(instrucao, (100, 450))
        janela.blit(sobre, (100, 500))

        pass

    def instrucao(self):
        imagem = pygame.image.load('inst.PNG')
        janela.blit(imagem,[175,110])

def pause(self):
        imagem = pygame.image.load('pause.PNG')
        janela.blit(imagem,[175,110])

    def sobre(self):
        janela.blit(equipe, (30, 70))
        janela.blit(nome1, (50, 100))
        janela.blit(nome2, (50, 150))
        janela.blit(nome3, (50, 200))
        janela.blit(nome4, (50, 250))
        janela.blit(comando, (30, 300))
        janela.blit(orientador, (50, 350))
        janela.blit(instrucao2, (30, 550))


    def cobra(self, orientacao, comidinha, pontuacao):
        for i in opcao:
            pygame.draw.rect(janela,GREEN, (i[0]+1, i[1]+1, 18 , 18))
            if opcao.index(i) == len(opcao)-1:
                if orientacao == 0:
                    opcao.append((i[0] + 20, i[1]))
                if orientacao == 90:
                    opcao.append((i[0],i[1]-20))
                if orientacao == 270:
                    opcao.append((i[0], i[1]+20))
                if orientacao == 180:
                    opcao.append((i[0] - 20, i[1]))
                if i != comidinha:
                    del opcao[0]
                    return (comidinha, pontuacao)
                else:
                    pontuacao += 1
                    return ((random.randint(0, 39)*20, random.randint(0, 29)*20), pontuacao)
                break



    
