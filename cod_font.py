import pygame,sys,funcoes,time
from pygame.locals import*

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Beta !!!")
grafico = funcoes.grafica()

# variaveis
modo = 0
opcao_menu = 0
orientacao = 0
comidinha = (200, 200)
pontuacao = 0

som = pygame.mixer.Sound("ben.ogg")
som.set_volume(0.4)


# ciclo do jogo
while True:
    if modo == 0:
        grafico.fundo()
        grafico.titulo(opcao_menu)
        grafico.parede()
    elif modo == 1:
        time.sleep(0.09)
        grafico.fundo()
        comidinha, pontuacao = grafico.cobra(orientacao, comidinha, pontuacao)
        grafico.comida(comidinha)
        grafico.placar(pontuacao)
        grafico.parede()
        pass
    elif modo == 2:
        som.play()
        grafico.fundo()
        grafico.sobre()
        grafico.parede()
        pass
    elif modo == 3:
        grafico.fundo()
        grafico.instrucao()
        grafico.parede()
    elif modo == 4:
        grafico.fundo()
        grafico.pause()
        grafico.parede()



    # corpo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            pass
        elif evento.type == pygame.KEYDOWN:
            if modo == 0:
                if evento.key == pygame.K_j:
                    modo = 1
                if evento.key == pygame.K_s:
                    modo = 2
                if evento.key == pygame.K_i:
                    modo = 3
            elif modo == 1:
                if evento.key == pygame.K_DOWN and orientacao != 90:
                    orientacao = 270
                if evento.key == pygame.K_UP and orientacao != 270:
                    orientacao = 90
                if evento.key == pygame.K_LEFT and orientacao != 0:
                    orientacao = 180
                if evento.key == pygame.K_RIGHT and orientacao != 180:
                    orientacao = 0
                if evento.key == pygame.K_v:
                    modo = 0
                if evento.key == pygame.K_p:
                    modo = 4
            elif modo == 2:
                if evento.key == pygame.K_v:
                    som.stop()
                    modo = 0
            elif modo == 3:
                if evento.key == pygame.K_v:
                    modo = 0
            elif modo == 4:
                if evento.key == pygame.K_p:
                    modo = 1




        elif evento.type == KEYUP:
            pass

    pygame.display.update()
    pass

