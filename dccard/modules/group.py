from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules
from dccard.types import PROPORTION, FLEX, GRID ,ROW,COLUMN
class Group(main_modules):

    def __init__(self,image,draw,**args) -> None:
        super().__init__(image,draw,**args)
        self.background = None
        self.frame = None # 邊框
        self.spacing = None # 間隔
        self.display = args['display']
        if self.display != (None or PROPORTION or FLEX or GRID):
            raise TypeError("Display type must be 'None' or 'PROPORTION' or 'FLEX' or 'GRID'")
        self.direction = args['direction'] if args.get('direction',None) else ROW
        self.groupheight = self.pos[3]-self.pos[1]
        self.groupwidth = self.pos[2]-self.pos[0]
        self.items = []

    def add(self,item):
        item.group = self
        self.items.append(item)
    
    def remove(self,item):
        self.items.remove(item)

    def render(self):
        if self.background:
            ...
        if self.items == []:
            return
        if self.display == None:
            """
            等高模式
            """
            if self.direction == ROW:
                minwidth = 0
                for item in self.items:
                    if item.minwidth != None:
                        minwidth += item.minwidth
                minwidth = self.groupwidth-minwidth-(self.spacing*len(self.items))/minwidth
                flagpos = self.pos[0]
                for item in self.items:
                    if item.minwidth == None:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(flagpos,self.pos[1],flagpos+minwidth,self.pos[3])    
                        })
                        flagpos += minwidth+self.spacing
                    else:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(flagpos,self.pos[1],flagpos+item.minwidth,self.pos[3])    
                        })
                        flagpos += item.minwidth+self.spacing

            elif self.direction == COLUMN:
                ...
