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

    def set_pos(self, pos):
        self.pos = pos

    def set_proportion(self, prop):
        self.proportion = prop

    def set_minheight(self, minheight):
        self.minheight = minheight

    def set_minwidth(self, minwidth):
        self.minwidth = minwidth

    def render(self, context):
        raise NotImplementedError