class main_modules:
    def __init__(self, image, draw, **args):
        self.pos = args['pos']
        self.proportion = args['proportion']
        self.minheight = args['minheight']
        self.group = None
        self.image = image 
        self.draw = draw


    def __str__(self):
        pass