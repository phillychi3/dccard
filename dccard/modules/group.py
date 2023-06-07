from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules
class Group(main_modules):

    def __init__(self,image:Image,draw:ImageDraw,**args) -> None:
        super().__init__(image,draw,**args)
        self.background = None
        self.frame = None # 邊框
        self.spacing = None # 間隔
        self.minheight = args['minheight'] # 最小高度
        self.items = []

    def add(self,item):
        item.group = self
        self.items.append(item)
    
    def remove(self,item):
        self.items.remove(item)

    def render(self):
        if self.background:
            self.draw.rectangle(self.background)
        for i in self.items:
            i.render()