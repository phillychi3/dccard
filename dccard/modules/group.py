from PIL import Image, ImageDraw

class Group:

    def __init__(self,image:Image,draw:ImageDraw,**args) -> None:
        self.image = image
        self.draw = draw
        self.background = None
        self.frame = None # 邊框
        self.spacing = None # 間隔
        self.minheight = None # 最小高度
        self.items = []
        self.group = None
        self.proportion = args['proportion']
        self.pos = args['pos']

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