class Mochila():
    def __init__(self) -> None:
        self.bag = {
            "halter": 0,
            "creatina": 0,
            "frango": 0,
            "batata_doce": 0,
            "anilha": 0
        }
    
    def get_bag(self):
        return self.bag

    def display_items(self):
        output = ''
        nth_child = 'halter'
        for item in self.bag:
            number = str(self.bag[item])
            if self.bag[item] >= 10 or (item != nth_child and self.bag[nth_child] >= 10):
                number = str(self.bag[item])
            else:
                number =  str(self.bag[item]) + " "
            output += f"{number}         "
            nth_child = item
        return output

    def add_item(self, item_name):
        self.bag[item_name] += 1
        print(f'{item_name} adicionado com sucesso a mochila, agora você possui {self.bag[item_name]} {item_name}(s)')

    def atingiu_meta(self, dificuldade):
        if dificuldade == "Easy":
            meta = 1
        elif dificuldade == "Medium":
            meta = 30
        elif dificuldade == "Hard":
            meta = 40

        atingiu = True
        for i in self.bag.values():
            if i < meta:
                atingiu = False

        return atingiu
