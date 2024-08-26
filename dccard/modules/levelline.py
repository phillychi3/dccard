from ..Component import BaseComponent

class Levelline(BaseComponent):
    def __init__(self, source):
        super().__init__()
        self.set_property("source", source)
