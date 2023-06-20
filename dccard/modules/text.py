from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules

class Text(main_modules):
    def __init__(self,image,draw,text,**args) -> None:
        super().__init__(image,draw,**args)
        self.textsize = args['size'] if 'size' in args else (50,50)
        self.font = args['font'] if 'font' in args else None
        self.fill = args['fill'] if 'fill' in args else "#000"
        self.xalign = args['xalign'] if 'xalign' in args else "left"
        self.yalign = args['yalign'] if 'yalign' in args else "top"
        self.text = text
        
    def render(self,data):
        dpos = data['poss']
        pos = (0,0)
        if self.xalign == "left":
            pos = (dpos[0],pos[1])
        elif self.xalign == "center":
            w,_ = self.draw.textsize(self.text,font=self.font)
            pos = (dpos[0]+(dpos[2]-dpos[0])/2-w/2,pos[1])
        elif self.xalign == "right":
            pos = (dpos[2],pos[1])
        if self.yalign == "top":
            pos = (pos[0],dpos[1])
        elif self.yalign == "center":
            _,h = self.draw.textsize(self.text,font=self.font)
            pos = (pos[0],dpos[1]+(dpos[3]-dpos[1])/2-h/2)
        elif self.yalign == "bottom":
            pos = (pos[0],dpos[3])
            
        self.draw.text((pos[0],pos[1]),self.text,font=self.font,fill=self.fill)
