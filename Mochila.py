class Mochila():
    def __init__(self) -> None:
        self.bag = {
            "halter": 0,
            "anilha": 0,
            "frango": 0,
            "seringa": 0,
            "batata_doce": 0
        }
    
    def get_mochila(self):
        output = 'Mochila: '
        for item in self.bag:
            output += f'\n {item}: {self.bag[item]}'
        output += '\n'
        return output

    def add_item(self, item_name):
        self.bag[item_name] += 1
        print(f'{item_name} adicionado com sucesso a mochila, agora você possui {self.bag[item_name]} {item_name}(s)')
