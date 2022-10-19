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
from ItemsClasses.Seringa import Seringa

from Quadrante import Quadrant
from Placar import Placar

from SoundController import Sound

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
plataforma_height = 50


###############################################################
###############---CONTROLES DA FASE---########################
VOLUME_DO_JOGO = 0.7
VELOCIDADE_DO_PLAYER = 2.5
VELOCIDADE_DOS_ITENS = 1.3
NUMERO_DE_ITEMS_POR_FASE = 5
#...
###############################################################

#placar e número de falhas
score = 0
fails = 0

#variavel que seta as informações do texto que vai aparecer o placar
#Parâmetros = (nomeDaFonte, tamanho, negrito?, itálico?)
display_text = pygame.font.SysFont('arial', 25, True, True)

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
items_instances = [Halter(), Seringa(), Batata(), Frango(), Anilha()]
items_list = []
for instance in items_instances:
    items_list.append(Item(SCREEN_WIDTH,VELOCIDADE_DOS_ITENS, instance, quadrant),)
for item in items_list:
    items_sprites_group.add(item)

bakground_image = pygame.image.load("./assets/background2.png")


items_per_time = NUMERO_DE_ITEMS_POR_FASE
def down_items_controller(item_list):
    active_items = 0
    for item in item_list:
        if item.get_start_down():   
            active_items += 1
    items_be_placed = items_per_time - active_items
    if items_be_placed > 0:
        for i in range(items_be_placed):
            items_list[randint(0, len(items_list)-1)].set_start_down(True, 'MAIN')

down_items_controller(items_sprites_group)


#while padrão para um jogo do py game(deve ser infinito)
while True:
    #definindo framerate
    frame_rate.tick(500)

    #definindo a cor de fundo com rgb
    screen.fill((255,0,255))
    screen.blit(bakground_image, (0,0))
  

    #mensgem que irá aparecer na tela
    fails_message = f'Falhas = {fails}'

    #formatando a mensgem que vai apareer para o formato desejado
    #primeiro parametro é a mensagem, segundo é o anti-alinsign(algo assim)
    #e o tereiro é a cor da imagem
    fails_formated_message = display_text.render(fails_message, True, (255, 0, 0))
    #esse for irá captar todos os eventos que acontecerem
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #criando a plataforma(temporáro)
    #primeiro parâmetro é onde o nosso objeto será criando
    #segundo parâmetro é a cor
    #terceiro parâmetro é a posição
    #quarto parâmetro é altura e largura
    plataform = pygame.draw.rect(screen, (255, 0 ,0), (
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
    


  
    for item in items_sprites_group:
        if player.get_rect().colliderect(item.get_rect()):
            print('Coletou!')
            item.reset()
            score += 1
            player_bag.add_item(item.get_item_type())
            down_items_controller(items_sprites_group)

        if (item.item_fall()):
            print('Não pegou :/')
            item.reset()
            down_items_controller(items_sprites_group)
            fails +=1 
            if(fails >= 3):
                pass
            
    #verificando se a bolinha já chegou ao fim da tela
   

   
    #blit é para jogar nossa mensagem do score lá na tela
    #o primeiro parâmetro é a mensagem já formatada
    #e o segundo é a posição
    
    screen.blit(fails_formated_message, (140, 10))
    #esse flip é pra atualizar tudo a cada iteração
    pygame.display.flip()