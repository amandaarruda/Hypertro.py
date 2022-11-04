import pygame

class Tela_start:
    def __init__(self,tela) -> None:
        pygame.mixer.init()
        self.tela = tela
        self.fonte = pygame.font.match_font('arial')
        self.bg_start = pygame.image.load('./assets/background.png')      

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        #Exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def esperar_por_jogador(self, framerate):
        esperando = True
        while esperando:
            framerate.tick(500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    return False
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN:
                    esperando = False
                    self.tela.blit(self.bg_start,(0,0))   

    def mostrar_tela_start(self):
        pygame.mixer.music.load("./sounds/musics/music_start.mp3")
        pygame.mixer.music.play()

        self.tela.blit(self.bg_start,(0,0))

        self.mostrar_texto( 
            'Hypertro.py: Em busca do shape',
            40,
            (255,255,0),
            320,
            200
        )   

        self.mostrar_texto(
            'Pressione qualquer tecla para jogar',
            32,
            (255,255,0),
            320,
            320
        )   

        pygame.display.flip()
        self.esperar_por_jogador(pygame.time.Clock())

def iniciar_tela_start(screen):
    start = Tela_start(screen)
    start.mostrar_tela_start()