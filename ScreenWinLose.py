from Dificuldade import Button
import pygame
import sys

button_surface = pygame.image.load("./assets/display/button.png")
button_surface = pygame.transform.scale(button_surface, (300, 90))

def jogar_novamente_fucao(tela, resultado):
	if resultado == "ganhou":
		bg_lose = pygame.image.load('./assets/temp_bg_win.png')
		tela.blit(bg_lose,(0,0))
		pygame.mixer.music.load("./sounds/musics/music_win.mp3")
		pygame.mixer.music.play()
	else:
		bg_lose = pygame.image.load('./assets/temp_bg_lose.png')
		tela.blit(bg_lose,(0,0))
		pygame.mixer.music.load("./sounds/musics/music_lose.mp3")
		pygame.mixer.music.play()

	button = Button(tela, button_surface, 320, 350, "Jogar novamente")
	continuar = True
	while continuar:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				retorno = button.checkForInput(pygame.mouse.get_pos())
				if retorno:
					#continuar = False
					return True

		button.update()
		button.changeColor(pygame.mouse.get_pos())

		pygame.display.update()