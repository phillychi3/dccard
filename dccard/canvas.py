from PIL import Image, ImageDraw, ImageFont
import dccard.modules as modules
import io
from typing import Union, Tuple, List



class Canvas:

    def __init__(self,size:tuple=(100,100)) -> None:
        self._size = size
        self._spacing = ...
        self._image = Image.new('RGBA',size)
        self._draw = ImageDraw.Draw(self._image)
        
    
    def background(self,background: Union[str,io.BytesIO]) -> None:
        """
        background: str  = color hex
        background: io.BytesIO = image
        """
        if isinstance(background,str):
            self._draw.rectangle([(0,0),self._size],fill=background)
        else:
            self._image.paste(background.resize(self._size))

    def image(self,image: Union[Image.Image,io.BytesIO,str],**args) -> modules.M_image:
        imageclass = modules.M_image(self._image,self._draw,image,**args)
        return imageclass

    def group(self,**args) -> modules.Group:
        groupclass = modules.Group(self._image,self._draw,**args)
        return groupclass