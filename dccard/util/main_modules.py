from PIL import Image, ImageDraw
class main_modules:
    def __init__(self, image, draw, **args):
        self.pos = args['pos'] # 位置
        self.proportion = args['proportion'] # 比例
        self.minheight = args['minheight'] # 最小高度3
        self.minwidth = args['minwidth'] # 最小寬度
        self.group = None
        self.image:Image.Image = image 
        self.draw:ImageDraw.ImageDraw = draw


    def __str__(self):
        pass