from PIL import ImageDraw
class ComponentMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                attrs[attr_name] = cls.chainable(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def chainable(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            return self if result is None else result

        return wrapper


class BaseComponent(metaclass=ComponentMeta):
    def __init__(self):
        self.pos = None
        self.proportion = None
        self.minheight = None
        self.minwidth = None
        self.group = None
        self.parent = None
        self.spacing = None
        self.poss = None
        self.draw = None

    def set_pos(self, pos):
        self.pos = pos

    def set_proportion(self, prop):
        self.proportion = prop

    def set_minheight(self, minheight):
        self.minheight = minheight

    def set_minwidth(self, minwidth):
        self.minwidth = minwidth

    def set_parent(self, parent):
        self.parent = parent

    def get_spacing(self):
        if self.spacing is not None:
            return self.spacing
        elif self.parent:
            return self.parent.get_spacing()
        return None

    def get_poss(self):
        if self.poss is not None:
            return self.poss
        elif self.parent:
            return self.parent.get_poss()
        return None

    def get_draw(self) -> ImageDraw.ImageDraw:
        if self.draw is not None:
            return self.draw
        elif self.parent:
            return self.parent.get_draw()
        return None

    def render(self):
        self._render()

    def _render(self):
        raise NotImplementedError("Subclasses must implement _render method")
