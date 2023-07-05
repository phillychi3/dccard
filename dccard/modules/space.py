from dccard.util.main_modules import main_modules


class Space(main_modules):
    def __init__(self,image,draw,**args) -> None:
        super().__init__(image,draw,**args)

    def render(self,data):
        ...