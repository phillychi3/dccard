from ..Component import BaseComponent


class Levelline(BaseComponent):
    def __init__(self, nowlevel,nextlevel,linestyle):
        super().__init__()
        self.minheight = 50 if self.minheight == None else self.minheight
        self._nextlevel = nextlevel
        self._nowlevel = nowlevel
        self._color = "red"
        self._bg_color = "black"
        self.linestype = linestyle if linestyle != None else 'rectangle'

    def nextlevel(self, nextlevel):
        self._nextlevel = nextlevel

    def nowlevel(self, nowlevel):
        self._nowlevel = nowlevel

    def style(self, linestyle):
        self.linestype = linestyle

    def color(self, color):
        self._color = color

    def bg_color(self, bg_color):
        self._bg_color = bg_color

    def _render(self):
        x1,y1,x2,y2 = self.get_poss()
        next=self.nextlevel/(x2-x1)
        level=round(self.nowlevel/next)
        draw = self.get_draw()
        if self.linestype == 'rectangle':
            # 等級底色
            draw.rectangle((x1,y1,x2,y2),fill=self._bg_color)
            if level <= x2:
                draw.rectangle((x1,y1,level+x1,y2),fill=self._color)
            else:
                draw.rectangle((x1,y1,level,y2),fill=self._color)
        elif self.linestype == 'oval':
            draw.rounded_rectangle((x1,y1,x2,y2),fill=self._bg_color,radius=10)
            if level <= x2:
                draw.rounded_rectangle((x1,y1,level+x1,y2),fill=self._color,radius=10)
            else:
                draw.rounded_rectangle((x1,y1,level,y2),fill=self._color,radius=10)

