from PIL import Image, ImageDraw, ImageFont
import dccard.modules as modules
import io
from typing import Union, Tuple, List



class Canvas:

    def __init__(self,size:tuple=(100,100)) -> None:
        self._size = size
        self._image = Image.new('RGBA',size)
        self._draw = ImageDraw.Draw(self._image)
        self._spacing = 2
        self._frame = None
        self.allitems = []
        self.renditems = 0
        self.poss = []

    def _argcheck(self,args:dict) -> None:
        if 'position' in args:
            args['pos'] = args['position']
        elif 'pos' in args:
            args['pos'] = args['pos']
        else:
            args['pos'] = None

    def render(self) -> Image.Image:
        ...
        
    
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
        self._argcheck(args)
        imgclass = modules.M_image(self._image,self._draw,image,**args)
        self.allitems.append(imgclass)

    def group(self,**args) -> modules.Group:
        self._argcheck(args)
        groupclass = modules.Group(self._image,self._draw,**args)
        self.allitems.append(groupclass)