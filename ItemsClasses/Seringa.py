class Seringa():
    def __init__(self) -> None:
        self.item_type = 'seringa'
        self.item_img_src = './assets/items/seringa.png'
    
    def get_type(self):
        return self.item_type

    def get_img_src(self):
        return self.item_img_src