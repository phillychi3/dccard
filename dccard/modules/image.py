from PIL import Image, ImageDraw
from dccard.types import AUTO
from dccard.util.zoom import zoom_extent
from dccard.util.main_modules import main_modules
import io
import requests

class M_image(main_modules):
    def __init__(self,image,draw,pastimage,**args) -> None:
        super().__init__(image,draw,**args)
        if type(pastimage) == str and "http" in pastimage:
            self.pastimage = Image.open(io.BytesIO(requests.get(pastimage).content))
        elif Image.isImageType(pastimage):
            self.pastimage = pastimage
        else:
            self.pastimage = Image.open(pastimage)
        self.size = args['size'] if 'size' in args else AUTO
        self.showmod = args['showmod'] if 'showmod' in args else "normal"
        self.mask = args['mask'] if 'mask' in args else None
        if self.mask != None and self.showmod != "square":
            raise Exception("mask can only be used in square mode")
        
    def render(self,data):
        mainpos = data['poss']
        if self.size == AUTO:
            if self.showmod == "normal":
                if self.pastimage.width > self.pastimage.height and mainpos[2]-mainpos[0] > mainpos[3]-mainpos[1]:
                    self.size = zoom_extent(self.pastimage,"width",mainpos[2]-mainpos[0])
                    if self.size[1] > mainpos[3]-mainpos[1]:
                        self.pastimage = self.pastimage.resize(self.size)
                        self.pastimage = self.pastimage.crop((0,0,self.pastimage.width,self.pastimage.height-(self.pastimage.height-(mainpos[3]-mainpos[1]))))
                        self.size = self.pastimage.size
                        
                else:
                    self.size = zoom_extent(self.pastimage,"height",mainpos[3]-mainpos[1])
                    if self.size[0] > mainpos[2]-mainpos[0]:
                        self.pastimage = self.pastimage.resize(self.size)
                        self.pastimage = self.pastimage.crop((0,0,self.pastimage.width-(self.pastimage.width-(mainpos[2]-mainpos[0])),self.pastimage.height))
                        self.size = self.pastimage.size

            elif self.showmod == "fill":
                self.size = (mainpos[2]-mainpos[0],mainpos[3]-mainpos[1])
            elif self.showmod == "showall":
                # 如果圖片比例大於區域比例，則以寬為準
                if self.pastimage.width/self.pastimage.height > (mainpos[2]-mainpos[0])/(mainpos[3]-mainpos[1]):
                    self.size = zoom_extent(self.pastimage,"width",mainpos[2]-mainpos[0])
                else:
                    self.size = zoom_extent(self.pastimage,"height",mainpos[3]-mainpos[1])
            elif self.showmod == "square":
                if self.pastimage.width > self.pastimage.height:
                    self.size = (mainpos[3]-mainpos[1],mainpos[3]-mainpos[1])
                else:
                    self.size = (mainpos[2]-mainpos[0],mainpos[2]-mainpos[0])

        self.image.paste(self.pastimage.resize(self.size),(mainpos[0],mainpos[1]),mask=self.mask(self.size[0]) if self.mask else None)