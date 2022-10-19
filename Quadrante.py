# Classe que vai gerar um range para o nosso item cair
#A tela será dividida em quadrantes e cada parte do quadrante será um range

#Motivo: Como nosso randint não é gerado aleatóriamente e sim pela contagem em milissegundos
#os itens estavam caindo muito próximos, já que os milissegundos eram parecidos, gerando ranges parecidos
#com cada range definido em um quadrante diferente, não ocorrerá mais esse problema

from random import randint

class Quadrant():
    def __init__(self, SCREEN_WIDTH, quadrant_qnt) -> None:
        self.quadrant = quadrant_qnt
        item_width_in_px = 52
        quadrant_width = (SCREEN_WIDTH-item_width_in_px)/self.quadrant
        self.quadrant_ranges = [(0, quadrant_width)]
        for i in range(1, self.quadrant):
            self.quadrant_ranges.append((self.quadrant_ranges[i-1][1], quadrant_width*(i+1)))
        self.current_quadrant = randint(0, self.quadrant-1)

    def generate_new_range(self):
        old_quadrant = self.current_quadrant
        while old_quadrant == self.current_quadrant:
            self.current_quadrant = randint(0, self.quadrant-1)


    def get_quadrant_range(self):
        self.generate_new_range()
        selected_range = self.quadrant_ranges[self.current_quadrant]
        return selected_range