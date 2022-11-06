class Batata():
    def __init__(self) -> None:
        self.item_type = 'batata_doce'
        self.item_img_src = './assets/items/batata_doce.png'
    
    def get_type(self):
        return self.item_type

    def get_img_src(self):
        return self.item_img_src