class Frango():
    def __init__(self) -> None:
        self.item_type = 'frango'
        self.item_img_src = './assets/items/frango.png'
    
    def get_type(self):
        return self.item_type

    def get_img_src(self):
        return self.item_img_src