from Dificuldade import Button
import pygame
import sys

button_surface = pygame.image.load("./assets/button.png")
button_surface = pygame.transform.scale(button_surface, (300, 60))

def jogar_novamente_fucao(tela, resultado):
	if resultado == "ganhou":
		bg_result = pygame.image.load('./assets/temp_bg_win.png')
		tela.blit(bg_result,(0,-60))
		pygame.mixer.music.load("./sounds/musics/music_win.mp3")
		pygame.mixer.music.play()
	else:
		bg_result = pygame.image.load('./assets/bg_lose.PNG')
		tela.blit(bg_result,(-25,-120))
		pygame.mixer.music.load("./sounds/musics/music_lose.mp3")
		pygame.mixer.music.play()

	button = Button(tela, button_surface, 320, 395, "Jogar novamente")
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