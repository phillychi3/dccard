from ..Component import BaseComponent

class Image(BaseComponent):
    def __init__(self, source):
        super().__init__()
        self.source = source

    def render(self, context):
        if context['poss']:
            x1, y1, x2, y2 = context['poss']
            img = Image.open(self.source)
            img = img.resize((x2 - x1, y2 - y1))
            context['draw'].bitmap((x1, y1), img)