from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules
from dccard.types import PROPORTION, FLEX, GRID ,ROW,COLUMN
class Group(main_modules):

    def __init__(self,image,draw,**args) -> None:
        super().__init__(image,draw,**args)
        self.background = None
        self.frame = None # 邊框
        self.spacing = 1 # 間隔
        self.display = args['display'] if 'display' in args else None
        # if type(self.display) != None or type(self.display) != PROPORTION or type(self.display) != FLEX or type(self.display) != GRID:
        #     raise TypeError("Display type must be 'None' or 'PROPORTION' or 'FLEX' or 'GRID'")
        self.direction = args['direction'] if args.get('direction',None) else ROW
        self.groupheight = 0
        self.groupwidth = 0
        self.items = []

    def add(self,item):
        item.group = self
        self.items.append(item)
        #詭異寫法
        return self
    
    def remove(self,item):
        self.items.remove(item)

    def render(self,data):
        if self.background:
            ...
        self.groupheight = data['poss'][3]-data['poss'][1]
        self.groupwidth = data['poss'][2]-data['poss'][0]
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
                minwidth = (self.groupwidth-minwidth-(self.spacing*len(self.items)))/len(self.items)
                flagpos = data['poss'][0]
                for item in self.items:
                    if item.minwidth == None:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(int(flagpos),int(data['poss'][1]),int(flagpos+minwidth),int(data['poss'][3]))    
                        })
                        flagpos += minwidth+self.spacing
                    else:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(int(flagpos),int(data['poss'][1]),int(flagpos+item.minwidth),int(data['poss'][3]))    
                        })
                        flagpos += item.minwidth+self.spacing

            elif self.direction == COLUMN:
                minheight = 0
                for item in self.items:
                    if item.minheight != None:
                        minheight += item.minheight
                minheight = (self.groupheight-minheight-(self.spacing*len(self.items)))/len(self.items)
                flagpos = data['poss'][1]
                for item in self.items:
                    if item.minheight == None:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(int(data['poss'][0]),int(flagpos),int(data['poss'][2]),int(flagpos+minheight))    
                        })
                        flagpos += minheight+self.spacing
                    else:
                        item.render({
                            'spacing':self.spacing,
                            'poss':(int(data['poss'][0]),int(flagpos),int(data['poss'][2]),int(flagpos+item.minheight))    
                        })
                        flagpos += item.minheight+self.spacing
