from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules

class Text(main_modules):
    def __init__(self,image,draw,**args) -> None:
        super().__init__(image,draw,**args)
        self.textsize = args['size'] if 'size' in args else (50,50)
        self.font = args['font'] if 'font' in args else None
        
    def render(self):
        self.draw.text(self.pos,self.text,font=self.font)
