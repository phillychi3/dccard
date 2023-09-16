from dccard.util.main_modules import main_modules
from dccard.modules.group import Group
from dccard.types import COLUMN
class metaclass(type):
    """
    read all user defining modules when init
    """
    def __new__(cls, name, bases, attrs):
        if name == "Template":
            return type.__new__(cls, name, bases, attrs)
        modules = {}
        for k,v in attrs.items():
            if '__' not in k:
                modules[k] = v
        attrs['modules'] = modules
        return type.__new__(cls, name, bases, attrs)


class Template(main_modules,metaclass=metaclass):
    """
    read all user defining modules when init

    use:

    class userclass(Template):
        def __init__(self,image1,image2):
        super().__init__()
        self.image1 = image1
        self.image2 = image2

        def image1(self):
            return cc.image(self.iimage1,group=True)

        def image2(self):
            return cc.image(self.iimage2,group=True)

    """
    modules = {}
    def __init__(self) -> None:
        super().__init__(None,None)

    def render(self,data=None):
        # add item to group
        group = Group(self.image,self.draw,direction=COLUMN)
        for k,v in self.modules.items():
            group.add(v(self))
        if data == None:
            data = {
                'spacing':2,
                'poss':(2,2,self.image.width-2,self.image.height),
            }
        group.render(data)