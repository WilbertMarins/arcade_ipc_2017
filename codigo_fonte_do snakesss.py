import pygame,sys,funcoes,time
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snakesss !!!")
graph = funcoes.grafica()

# variaveis fundamentais
mode = 0
option_menu = 0
guindace = 0
item = (200, 200)
pontuacao = 0


# partes do jogo
while True:
    if mode == 0:
        graph.background()
        graph.title(option_menu)
        graph.wall()
    elif mode == 1:
        time.sleep(0.09) #quanto menor ,melhor o tempo de resposta
        graph.background()
        item, pontuacao = graph.viper(guindace, item, pontuacao)
        graph.food(item)
        graph.scoreboard(pontuacao)
        graph.wall()
        pass
    elif mode == 2:
        graph.background()
        graph.credits()
        graph.wall()
        pass
    elif mode == 3:
        graph.background()
        graph.instruction()
        graph.wall()
    elif mode == 4:
        graph.background()
        graph.pause()
        graph.wall()



    # codicionais dos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pass
        elif event.type == pygame.KEYDOWN:
            if mode == 0:
                if event.key == pygame.K_j:
                    mode = 1
                if event.key == pygame.K_s:
                    mode = 2
                if event.key == pygame.K_i:
                    mode = 3
            elif mode == 1:
                if event.key == pygame.K_DOWN and guindace != 90:
                    guindace = 270
                if event.key == pygame.K_UP and guindace != 270:
                    guindace = 90
                if event.key == pygame.K_LEFT and guindace != 0:
                    guindace = 180
                if event.key == pygame.K_RIGHT and guindace != 180:
                    guindace = 0
                if event.key == pygame.K_v:
                    mode = 0
                if event.key == pygame.K_p:
                    mode = 4
            elif mode == 2:
                if event.key == pygame.K_v:
                    mode = 0
            elif mode == 3:
                if event.key == pygame.K_v:
                    mode = 0
            elif mode == 4:
                if event.key == pygame.K_p:
                    mode = 1




        elif event.type == KEYUP:
            pass

    pygame.display.update()
    pass

