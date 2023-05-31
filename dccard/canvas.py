from PIL import Image, ImageDraw, ImageFont
import dccard.modules as modules
import io
class Canvas:

    def __init__(self,size:tuple) -> None:
        self.size = size
        self.spacing = ...
        self.image = Image.new('RGBA',size)
        self.draw = ImageDraw.Draw(self.image)
        
    
    def background(self,background:str | io.BytesIO) -> None:
        """
        background: str  = color hex
        background: io.BytesIO = image
        """
        if isinstance(background,str):
            self.draw.rectangle([(0,0),self.size],fill=background)
        else:
            self.image.paste(background.resize(self.size))
            
    def secondbg(self):
        modules.Secondbg(self.image,self.draw)