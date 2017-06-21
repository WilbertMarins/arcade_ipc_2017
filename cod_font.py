import pygame,sys,funcoes,time
from pygame.locals import*

# Abre a tela de trabalho para o jogo
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Beta !!!")
graphic = funcoes.grafica()

# Variaveis
mode = 0
option_menu = 0
guindance = 0
item = (200, 200)
punctuation = 0

# Opcoes do jogo
while True:

    if mode == 0:
        graphic.bottom()
        graphic.title(option_menu)
        graphic.wall()

    elif mode == 1:
        time.sleep(0.09)
        graphic.bottom()
        item, punctuation = graphic.snake(guindance, item, punctuation)
        graphic.item(item)
        graphic.scoreboard(punctuation)
        graphic.wall()
        pass

    elif mode == 2:
        graphic.bottom()
        graphic.about()
        graphic.wall()
        pass

    elif mode == 3:
        graphic.bottom()
        graphic.instrution()
        graphic.wall()

    elif mode == 4:
        graphic.bottom()
        graphic.pause()
        graphic.wall()


    # Corpo de eventos
    for event in pygame.event.get():

        # Verifica se botao de fechar foi acionado
        if event.type == pygame.QUIT:
            pygame.quit()
            pass

        # Da seguimento ao jogo
        elif event.type == pygame.KEYDOWN:

            # Menu iniciar
            if mode == 0:

                if event.key == pygame.K_j:
                    mode = 1

                if event.key == pygame.K_s:
                    mode = 2

                if event.key == pygame.K_i:
                    mode = 3

            # Roda o jogo
            elif mode == 1:

                if event.key == pygame.K_DOWN and guindance != 90:
                    guindance = 270

                if event.key == pygame.K_UP and guindance != 270:
                    guindance = 90

                if event.key == pygame.K_LEFT and guindance != 0:
                    guindance = 180

                if event.key == pygame.K_RIGHT and guindance != 180:
                    guindance = 0

                if event.key == pygame.K_v:
                    mode = 0

                if event.key == pygame.K_p:
                    mode = 4

            # Abre as instruções
            elif mode == 2:
                if event.key == pygame.K_v:
                    mode = 0

            # Abre o sobre o jogo
            elif mode == 3:
                if event.key == pygame.K_v:
                    mode = 0

            # Modo de pause enquanto esta jogando
            elif mode == 4:
                if event.key == pygame.K_p:
                    mode = 1


        elif event.type == KEYUP:
            pass


    pygame.display.update()
    pass
