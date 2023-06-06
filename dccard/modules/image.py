from PIL import Image, ImageDraw
from dccard.types import AUTO
from dccard.util.zoom import zoom_extent
import io
import requests

class M_image:
    def __init__(self,image:Image,draw:ImageDraw,pastimage,**args) -> None:
        self.image = image 
        self.draw = draw
        self.minheight = None
        self.group = None
        if type(pastimage) == str and "http" in pastimage:
            self.pastimage = Image.open(io.BytesIO(requests.get(image).content))
        elif Image.isImageType(pastimage):
            self.pastimage = pastimage
        else:
            self.pastimage = Image.open(pastimage)
        self.pos = args['pos']
        self.proportion = args['proportion']
        self.size = args['size'] if 'size' in args else AUTO
        
    def render(self,data):
        mainpos = data['poss']
        if self.size == AUTO:
            if self.pastimage.width > self.pastimage.height:
                self.size = zoom_extent(self.pastimage,"width",mainpos[2]-mainpos[0])
            else:
                self.size = zoom_extent(self.pastimage,"lenght",mainpos[3]-mainpos[1])
        self.image.paste(self.pastimage.resize(self.size),(mainpos[0],mainpos[1]))