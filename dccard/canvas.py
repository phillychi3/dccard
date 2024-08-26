from .modules import Text, Image, Group
from typing import Union, Tuple
from PIL import Image as Pilimage, ImageDraw
from .type import LayoutType, Direction

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Canvas:
    def __init__(self, size: Tuple[int, int] = (100, 100), display: Union[LayoutType, None] = None):
        self._size = size
        self._image = Pilimage.new('RGBA', size)
        self._draw = ImageDraw.Draw(self._image)
        self._spacing = 2
        self._display = display
        self.root_group = Group(display=display, direction=Direction.COLUMN)

    def add_component(self, component):
        self.root_group.add(component)
        return component

    def render(self):
        logger.debug("Starting canvas render")
        context = {
            'spacing': self._spacing,
            'poss': (0, 0, self._size[0], self._size[1]),
            'draw': self._draw
        }
        logger.debug(f"Root context: {context}")
        self.root_group.render(context)
        logger.debug("Finished canvas render")
        return self._image

    def group(self, direction=Direction.ROW):
        return Group(direction=direction)

    def text(self, content):
        return Text(content)

    def image(self, source):
        return Image(source)