from PIL import Image, ImageDraw


class text:
    def __init__(self,image:Image,draw:ImageDraw,**args) -> None:
        self.image = image
        self.draw = draw
        self.minheight = None
        self.pos = args['pos']
        self.textsize = args['size'] if 'size' in args else (50,50)
        self.font = args['font'] if 'font' in args else None
        
    def render(self):
        self.draw.text(self.pos,self.text,font=self.font)
