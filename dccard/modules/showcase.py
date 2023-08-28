from dccard.util.main_modules import main_modules


class Showcase(main_modules):
    def __init__(self,image,draw,images,row,**args) -> None:
        super().__init__(image,draw,**args)
        self.images = images
        self.row = row

    def render(self,data):
        # showcase，在範圍內展示多張圖片
        # 自動調整排與列的數量
        # 每張圖片大小為64px
        mainpos = data['poss']
        count = len(self.images)
        width = mainpos[2]-mainpos[0]
        height = mainpos[3]-mainpos[1]
        space = 2

        # 計算列數
        row = self.row
        if row == None:
            row = int(height/64)
        # 計算行數
        col = int(count/row)
        if count % row != 0:
            col += 1
        # 計算每張圖片的大小
        size = 64
        # 計算每張圖片的位置
        poss = []
        for i in range(col):
            for j in range(row):
                poss.append((mainpos[0]+(size+space)*j,mainpos[1]+(size+space)*i,mainpos[0]+(size+space)*j+size,mainpos[1]+(size+space)*i+size))
        # 貼上圖片
        for i,j in enumerate(self.images):
            self.image.paste(j.resize((size,size)),poss[i])





