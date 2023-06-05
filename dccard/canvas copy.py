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

    def render(self) -> Image.Image:
        allminheight = 0
        # 計算所有最小高度
        for i in self.allitems:
            if self.renditems == 0:
                break
            if i.minheight != None:  # noqa: E711
                allminheight += i.minheight
        oneitemheight = int((self._image.height-allminheight-(self._spacing*self.renditems))/self.renditems)  # noqa: E501

        # 計算所有位置
        for i in self.allitems:
            if self.renditems == 0:
                break            
            if i.minheight == None and i.pos == None: # noqa: E711
                self.poss.append(oneitemheight)
            elif i.minheight != None and i.pos == None:  # noqa: E711
                self.poss.append(i.minheight)
            else:
                self.poss.append(None)

        for i,j in enumerate(self.allitems):
            if self.poss[i] != None:  # noqa: E711
                j.pos = (self._spacing,sum(self.poss[:i])+self._spacing)
                if 'size' in j.__dict__:
                    if i == len(self.allitems)-1:
                        j.size = (self.poss[i],self.poss[i])
                    else:
                        j.size = (self.poss[i],self.poss[i]-self._spacing)
            j.render()

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

    def image(self,image: Union[Image.Image,io.BytesIO,str],**args) -> modules.M_image:
        if 'position' in args:
            args['pos'] = args['position']
        elif 'pos' in args:
            args['pos'] = args['pos']
        else:
            args['pos'] = None
            self.renditems += 1
        imageclass = modules.M_image(self._image,self._draw,image,**args)
        self.allitems.append(imageclass)
        return imageclass

    def group(self,**args) -> modules.Group:
        if 'position' in args:
            args['pos'] = args['position']
        elif 'pos' in args:
            args['pos'] = args['pos']
        else:
            args['pos'] = None
            self.renditems += 1   
        groupclass = modules.Group(self._image,self._draw,**args)
        self.allitems.append(groupclass)
        return groupclass