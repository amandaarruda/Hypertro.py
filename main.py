import pygame 
from pygame.locals import *
from sys import exit
from random import randint

from Item import Item
from Player import Player
from Mochila import Mochila

#importando itens: 
from ItemsClasses.Halter import Halter
from ItemsClasses.Anilha import Anilha
from ItemsClasses.Frango import Frango
from ItemsClasses.Batata import Batata
from ItemsClasses.Creatina import Creatina
from ItemsClasses.Seringa import Seringa

from StartScreen import iniciar_tela_start
from Dificuldade import continuar_dificuldade
from ScreenWinLose import jogar_novamente_fucao

from Quadrante import Quadrant
from Placar import Placar

from SoundController import Sound
from LifeController.LifeController import LifeController
#iniciando o  pygame
pygame.init()

player_bag = Mochila()

GAME_NAME = "Hypertro.py: Em busca do shape"
print(GAME_NAME)

#definindo o tamanho da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#definindo o nome da janela
pygame.display.set_caption(GAME_NAME)

#variavel que vai controlar o framerate
frame_rate = pygame.time.Clock()

#tamanho da plataforma
plataform_width = 640
plataforma_height = 20

##########################################################################

#ÁREA DA TELA DE START E ESCOLHA DE DIFICULDADE

num_jogos = 0

iniciar_tela_start(screen)

jogar_novamente = True
while jogar_novamente:

    if num_jogos != 0:

        jogar_novamente_fucao(screen, resultado)

        pygame.mixer.music.load("./sounds/musics/music_start.mp3")
        pygame.mixer.music.play()

        bg_start = pygame.image.load('./assets/background.png')
        screen.blit(bg_start,(0,0))

    bg_level = pygame.image.load('./assets/backgroundb.png')
    screen.blit(bg_level,(0,0))
    dificuldade = continuar_dificuldade(screen)

    ###############################################################
    ###############---CONTROLES DA FASE---########################
    VOLUME_DO_JOGO = 0.4

    if dificuldade == "Easy":    
        VELOCIDADE_DOS_ITENS = 0.5
        VELOCIDADE_DO_PLAYER = 1.8
        NUMERO_DE_ITEMS_POR_FASE = 3

    if dificuldade == "Medium":    
        VELOCIDADE_DOS_ITENS = 0.7
        VELOCIDADE_DO_PLAYER = 1.7
        NUMERO_DE_ITEMS_POR_FASE = 4

    if dificuldade == "Hard":    
        VELOCIDADE_DOS_ITENS = 1.0
        VELOCIDADE_DO_PLAYER = 1.6
        NUMERO_DE_ITEMS_POR_FASE = 5
        
    #...
    ###############################################################

    #placar e número de falhas
    score = 0
    fails = 0
    life_controller = LifeController(screen)
    #variavel que seta as informações do texto que vai aparecer o placar
    #Parâmetros = (nomeDaFonte, tamanho, negrito?, itálico?)
    display_text = pygame.font.SysFont('MS Sans Serif', 30, True, True)

    background_music = Sound('./sounds/musics/musica_ambiente.mp3', VOLUME_DO_JOGO)
    background_music.play()

    #instanciando grupo de sprites do projeto
    player_sprites_group = pygame.sprite.Group()
    items_sprites_group = pygame.sprite.Group()
    screen_log_sprites_group = pygame.sprite.Group()

    placar = Placar(screen, player_bag)

    screen_log_sprites_group.add(placar)
    #Instanciando o objeto player
    player = Player(VELOCIDADE_DO_PLAYER, SCREEN_HEIGHT, SCREEN_WIDTH, plataforma_height)
    #adicionando o player ao grupo de sprites 
    player_sprites_group.add(player)

    quadrant = Quadrant(SCREEN_WIDTH, 4)
    items_instances = [Halter(), Creatina(), Batata(), Frango(), Anilha(), Seringa()]
    items_list = []
    for instance in items_instances:
        items_list.append(Item(SCREEN_WIDTH,VELOCIDADE_DOS_ITENS, instance, quadrant),)
    for item in items_list:
        items_sprites_group.add(item)

    bakground_image = pygame.image.load("./assets/background2.png")

    #ativando o mecanismo da seringa
    seringa_down = False
    items_per_time = NUMERO_DE_ITEMS_POR_FASE
    def down_items_controller(item_list):
        active_items = 0
        for item in item_list:
            if item.get_start_down():   
                active_items += 1
        items_be_placed = items_per_time - active_items
        if items_be_placed > 0:
            for i in range(items_be_placed):
                while True:
                    item_down = items_list[randint(0, len(items_list)-1)]
                    if seringa_down:
                        item_down.set_start_down(True, 'MAIN')
                        break
                    else:
                        if item_down.get_item_type() != 'seringa':
                            item_down.set_start_down(True, 'MAIN')
                            break

    down_items_controller(items_sprites_group)

    #while padrão para um jogo do py game(deve ser infinito)
    rodar_jogo = True
    while rodar_jogo:
        #definindo framerate
        frame_rate.tick(500)

        #definindo a cor de fundo com rgb
        screen.fill((255,0,255))
        screen.blit(bakground_image, (0,0))

        #esse for irá captar todos os eventos que acontecerem
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        #criando a plataforma
        #primeiro parâmetro é onde o nosso objeto será criando
        #segundo parâmetro é a cor
        #terceiro parâmetro é a posição
        #quarto parâmetro é altura e larguraa
        plataform = pygame.draw.rect(screen, (87,73,71), (
                                            SCREEN_WIDTH-plataform_width, 
                                            SCREEN_HEIGHT-plataforma_height, 
                                            plataform_width, 
                                            plataforma_height))


        #colocando todos os sprites do nosso grupo de sprites na tela
        screen_log_sprites_group.draw(screen)
        player_sprites_group.draw(screen)
        items_sprites_group.draw(screen)

        #dando update neles a cada iteração do while
        screen_log_sprites_group.update()
        player_sprites_group.update()
        items_sprites_group.update()
        
        life_controller.update()

        #CONTROLE DE COLETA E QUEDA
        for item in items_sprites_group:
            if player.get_rect().colliderect(item.get_rect()):
                print('Coletou!')
                if item.get_item_type() != 'seringa':
                    player_bag.add_item(item.get_item_type())
                else:
                    life_controller.heal()
                item.reset()
                down_items_controller(items_sprites_group)

            if (item.item_fall()):
                print('Não pegou :/')
                if item.get_item_type() != 'seringa':
                    life_controller.damage()
                item.reset()
                down_items_controller(items_sprites_group)
            
            seringa_down = False if life_controller.is_full_life() else True

            if player_bag.atingiu_meta(dificuldade):
                print("Ganhou!!")
                num_jogos += 1
                resultado = "ganhou"
                rodar_jogo = False
                player_bag.__init__()

            if life_controller.get_life() <= 0 :
                print("Perdeu!!")
                num_jogos += 1
                resultado = "perdeu"
                rodar_jogo = False
                player_bag.__init__()
                
        ###############################################      

        #esse flip é pra atualizar tudo a cada iteração
        pygame.display.flip()