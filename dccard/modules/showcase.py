from dccard.util.main_modules import main_modules


class Showcase(main_modules):
    def __init__(self,image,draw,images,size,**args) -> None:
        super().__init__(image,draw,**args)
        self.images = images
        self.size = size if type(size) == tuple else (size,size)

    def render(self,data):
        mainpos = data['poss']
        count = len(self.images)
        width = mainpos[2]-mainpos[0]
        height = mainpos[3]-mainpos[1]
        row = int(width/self.size[0])
        row_spacing = int((width-(row*self.size[0]))/(row-1))
        col = int(height/self.size[1])
        col_spacing = int((height-(col*self.size[1]))/(col-1))
        for i in range(count):
            #如果超出範圍，則不顯示
            if i >= row*col:
                break
            x = int(i%row)
            y = int(i/row)
            pos = (mainpos[0]+(x*(self.size[0]+row_spacing)),mainpos[1]+(y*(self.size[1]+col_spacing)))
            self.image.paste(self.images[i].resize(self.size),pos)
            



