from PIL import Image, ImageDraw


class M_image:
    def __init__(self,image:Image,draw:ImageDraw,pastimage,**args) -> None:
        self.image = image 
        self.draw = draw
        self.pastimage = pastimage 
        self.group = None
        self.pos = args['pos']
        self.size = args['size'] if 'size' in args else (50,50)
        
    def render(self):
        self.image.paste(self.pastimage.resize(self.size),self.pos)