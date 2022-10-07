import pygame 
from pygame.locals import *
from sys import exit
from random import randint

#iniciando o  pygame
pygame.init()

GAME_NAME = "Hypertro.py: Em busca do shape"

#definindo o tamanho da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#definindo o nome da janela
pygame.display.set_caption(GAME_NAME)

#variavel que vai controlar o framerate
frame_rate = pygame.time.Clock()

#posição da bolinha (temporário)
object_position_x = 0
object_position_y = 0

#tamanho da plataforma
plataform_width = 640
plataforma_height = 50

#posição do player
player_position_x = 0
player_position_y = SCREEN_HEIGHT - plataforma_height - 61 * 1.5

#placar e número de falhas
score = 0
fails = 0

#variavel que seta as informações do texto que vai aparecer o placar
#Parâmetros = (nomeDaFonte, tamanho, negrito?, itálico?)
display_text = pygame.font.SysFont('arial', 40, True, True)

#função que gera um valor aleatório pra bolinha(temporário)
def generate_random_position():
    global object_position_x
    global object_position_y
    object_position_y = 0
    object_position_x = randint(1, SCREEN_WIDTH)

#class player (posteriormente será separada do arquivo main.py)
class Player(pygame.sprite.Sprite):
    #construtor da classe
    def __init__(self):
        #iniciando o contrutor da classe sprite que está dentro do pygame
        pygame.sprite.Sprite.__init__(self)

        #variavel que contém as sprites do player
        #(é um array pois quando tivermos animação será várias imagens)
        self.sprites = [pygame.image.load('assets/player/cariani.png')]

        #variavel que guarda a posição da imagem atual
        self.current_sprite = 0

        #instanciando nosso player
        self.image = self.sprites[self.current_sprite]
        #mudando a escala dele para 1.5x
        self.image = pygame.transform.scale(self.image, (50*1.5, 61*1.5))

        #colocando nosso player como um objeto em cena e definindo sua posição
        self.rect = self.image.get_rect()
        self.rect.topleft = player_position_x, player_position_y

    #função que roda a cada frame
    def update(self):
        #atualizando a posição do player, aso tenha mudado
        self.rect.topleft = player_position_x, player_position_y

        #verificando se há colisão com a bolinha
        if(self.rect.colliderect(object)):
            print('Pegou!')
            global score
            score += 1
            generate_random_position()

#instanciando grupo de sprites do projeto
sprites_group = pygame.sprite.Group()

#Instanciando o objeto player
player = Player()
#adicionando o player ao grupo de sprites 
sprites_group.add(player)

#while padrão para um jogo do py game(deve ser infinito)
while True:
    #definindo framerate
    frame_rate.tick(500)

    #definindo a cor de fundo com rgb
    screen.fill((255,0,255))

    #variavel que vai guardar a velocidade do player
    #é nada mais que a quantidade de px que ele vai andar por ação
    player_velocity = 2

    #mensgem que irá aparecer na tela
    score_message = f'Coletados: {score}'
    fails_message = f'Falhas = {fails}'

    #formatando a mensgem que vai apareer para o formato desejado
    #primeiro parametro é a mensagem, segundo é o anti-alinsign(algo assim)
    #e o tereiro é a cor da imagem
    score_formated_message = display_text.render(score_message, True, (255, 255, 255))
    fails_formated_message = display_text.render(fails_message, True, (255, 0, 0))
    #esse for irá captar todos os eventos que acontecerem
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #ações realizadas ao manter a tecla pressionada
    if pygame.key.get_pressed()[K_a]: 
        player_position_x -= player_velocity
    if pygame.key.get_pressed()[K_d]: 
        player_position_x += player_velocity    
     

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

    circle_radius = 10
    #criando nossa bolinha(temporário)
    #a mesma coisa da plataforma acima, mas ao invés da altura e largura, dá-se o raio
    object = pygame.draw.circle(screen, (0,200,0),(object_position_x, -50 + object_position_y),(circle_radius))

    #colocando todos os sprites do nosso grupo de sprites na tela
    sprites_group.draw(screen)
    #dando update neles a cada iteração do while
    sprites_group.update()

    #verificando se a bolinha já chegou ao fim da tela
    if (object_position_y > SCREEN_HEIGHT):
        generate_random_position()
        print('Não pegou :/')
        fails +=1 
        if(fails >= 3):
            pass
            #aqui o usuário perderia
    else:
        object_position_y += 1

   
    #blit é para jogar nossa mensagem do score lá na tela
    #o primeiro parâmetro é a mensagem já formatada
    #e o segundo é a posição
    screen.blit(score_formated_message, (370, 40))
    screen.blit(fails_formated_message, (100, 40))
    #esse flip é pra atualizar tudo a cada iteração
    pygame.display.flip()