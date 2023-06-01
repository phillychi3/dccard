from PIL import Image, ImageDraw

class Group():

    def __init__(self,image:Image,draw:ImageDraw,**args) -> None:
        self.image = image
        self.draw = draw
        self.background = None
        self.frame = None
        self.spacing = None
        self.items = []

    def add(self,item):
        self.items.append(item)
    
    def remove(self,item):
        self.items.remove(item)

    def render(self):
        for i in self.items:
            i.render()