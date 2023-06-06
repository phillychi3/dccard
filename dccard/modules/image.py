from PIL import Image, ImageDraw
from dccard.types import AUTO

class M_image:
    def __init__(self,image:Image,draw:ImageDraw,pastimage,**args) -> None:
        self.image = image 
        self.draw = draw
        self.minheight = None
        self.pastimage = pastimage 
        self.group = None

        self.pos = args['pos']
        self.proportion = args['proportion']
        self.size = args['size'] if 'size' in args else AUTO
        
    def render(self):
        self.image.paste(self.pastimage.resize(self.size),self.pos)