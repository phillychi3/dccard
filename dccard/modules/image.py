from PIL import Image, ImageDraw


class M_image:
    def __init__(self,image:Image,draw:ImageDraw,pastimage,**args) -> None:
        self.image = image
        self.draw = draw
        self.pastimage = pastimage
        self.pos = args['pos'] if 'pos' in args else (0,0)
        self.size = args['size'] if 'size' in args else (50,50)        
        
    def render(self):
        self.image.paste(self.pastimage.resize(self.size),self.pos)