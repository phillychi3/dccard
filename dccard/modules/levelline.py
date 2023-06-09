from PIL import Image, ImageDraw
from dccard.util.main_modules import main_modules


class Levelline(main_modules):
    def __init__(self,image,draw,nowlevel,nextlevel,**args) -> None:
        super().__init__(image,draw,**args)
        self.minheight = 50 if self.minheight == None else self.minheight
        self.nextlevel = nextlevel
        self.nowlevel = nowlevel

    def render(self,data):
        mainpos = data['poss']
        next=self.nextlevel/(mainpos[2]-mainpos[0])
        level=round(self.nowlevel/next)
        # 等級底色
        self.draw.rectangle((mainpos[0],mainpos[1],mainpos[2],mainpos[3]),fill=(0,0,0,0))
        # 等級條red color
        self.draw.rectangle((mainpos[0],mainpos[1],level,mainpos[3]),fill=(255,0,0,255))