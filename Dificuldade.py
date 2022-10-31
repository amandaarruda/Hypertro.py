import pygame
import sys

main_font = pygame.font.SysFont("arial", 40)

class Button():
    def __init__(self, tela, image, x_pos, y_pos, text_input):
        self.tela = tela
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.tela.blit(self.image, self.rect)
        self.tela.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return self.text_input

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "red")
        else:
            self.text = main_font.render(self.text_input, True, "white")


def continuar_dificuldade(tela):

    button_surface = pygame.image.load("./assets/display/button.png")
    button_surface = pygame.transform.scale(button_surface, (300, 90))

    button1 = Button(tela, button_surface, 320, 150, "Easy")
    button2 = Button(tela, button_surface, 320, 250, "Medium")
    button3 = Button(tela, button_surface, 320, 350, "Hard")

    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                retorno1 = button1.checkForInput(pygame.mouse.get_pos())
                retorno2 = button2.checkForInput(pygame.mouse.get_pos())
                retorno3 = button3.checkForInput(pygame.mouse.get_pos())

                if retorno1:
                    continuar = False
                    return "Easy"

                elif retorno2:
                    continuar = False
                    return "Medium"

                elif retorno3:
                    continuar = False
                    return "Hard"

        button1.update()
        button1.changeColor(pygame.mouse.get_pos())

        button2.update()
        button2.changeColor(pygame.mouse.get_pos())

        button3.update()
        button3.changeColor(pygame.mouse.get_pos())

        pygame.display.update()