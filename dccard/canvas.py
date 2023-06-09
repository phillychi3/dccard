from PIL import Image, ImageDraw, ImageFont
import dccard.modules as modules
from dccard.types import PROPORTION, FLEX, GRID , AUTO
import io
from typing import Union, Tuple, List
import requests


def modules_decorator(func):
    def wrapper(self, *args, **kwargs):
        if kwargs.get('group', False):
            return func(self, *args, **kwargs)
        else:
            obj = func(self, *args, **kwargs)
            self.allitems.append(obj)
            return obj
    return wrapper

class Canvas:

    def __init__(self,size:tuple=(100,100),display:Union[PROPORTION,FLEX,GRID]=None) -> None:
        self._size = size
        self._image = Image.new('RGBA',size)
        self._draw = ImageDraw.Draw(self._image)
        self._spacing = 2
        self._display = display
        self._frame = None
        self.allitems = []
        self.efficientitems = 0
        self.poss = []

    def _argcheck(self,args:dict) -> None:
        # 如果位置是None，則計算進排版
        if 'position' in args:
            args['pos'] = args['position']
        elif 'pos' in args:
            args['pos'] = args['pos']
        else:
            args['pos'] = None
        # 如果是比例模式
        if 'proportion' in args:
            args['proportion'] = args['proportion']
        elif 'prop' in args:
            args['proportion'] = args['prop']
        else:
            args['proportion'] = None
        # 如果已經設定minheight
        if 'minheight' in args:
            args['minheight'] = args['minheight']
        else:
            args['minheight'] = None
        if args['pos'] == None and args['minheight'] == None and args.get('group',False) == False:
            self.efficientitems += 1


    def flex(self,**args) -> None:
        ...
    
    def grid(self,**args) -> None:
        ...

    def render(self) -> Image.Image:
        """
        排版模式:
        - 有pos: 為獨立元件，不計算進排版
        - 沒pos: 以間距為準
        - 比例模式: 以比例為準，捨棄間距
        - flex模式: css flex排版
        - grid模式: css grid排版
        """
        if self._display == None:
            """
            模式: 沒有排版模式
            所有元素等寬等高
            """
            allminheight = 0
            for i in self.allitems:
                if self.efficientitems == 0:
                    break
                if i.minheight != None:
                    allminheight += i.minheight
            oneitemheight = int((self._image.height-allminheight-(self._spacing*self.efficientitems))/self.efficientitems)  # noqa: E501
            startpos = 0
            for i in self.allitems:
                if self.efficientitems == 0:
                    break
                if i.minheight == None and i.pos == None: # noqa: E711
                    # 加入起始位置 結束位置
                    # poss = (x1,y1,x2,y2)
                    self.poss.append((self._spacing,startpos+self._spacing,self._image.width-self._spacing,startpos+oneitemheight))
                    startpos += oneitemheight
                elif i.minheight != None and i.pos == None:  # noqa: E711
                    self.poss.append((self._spacing,startpos+self._spacing,self._image.width-self._spacing,startpos+i.minheight))  # noqa: E501
                    startpos += i.minheight
                else:
                    self.poss.append(None)
            for i,j in enumerate(self.allitems):
                j.render({
                    'spacing':self._spacing,
                    'poss':self.poss[i],
                })

        elif self._display == PROPORTION:
            """
            模式: 比例模式
            如果沒有proporiton , prop = 1
            """
            ...



        return self._image

        
        
    
    def background(self,background: Union[str,io.BytesIO]) -> None:
        """
        background: str  = color hex
        background: io.BytesIO = image
        """
        if isinstance(background,str):
            self._draw.rectangle([(0,0),self._size],fill=background)
        else:
            self._image.paste(background.resize(self._size))
    @modules_decorator
    def image(self, image: Union[Image.Image, io.BytesIO, str], **args) -> modules.M_image:
        self._argcheck(args)
        imgclass = modules.M_image(self._image, self._draw, image, **args)
        return imgclass
    @modules_decorator
    def group(self,**args) -> modules.Group:
        self._argcheck(args)
        groupclass = modules.Group(self._image,self._draw,**args)
        return groupclass
    @modules_decorator
    def levelline(self,nowlevel:int,nextlevel:int,**args) -> modules.Levelline:
        args['minheight'] = 50 if args.get('minheight',None) == None else args['minheight']
        self._argcheck(args)
        levellclass = modules.Levelline(self._image,self._draw,nowlevel,nextlevel,**args)
        return levellclass