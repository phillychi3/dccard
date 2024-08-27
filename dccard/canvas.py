from .modules import Text, Image, Group, Levelline
from typing import Union, Tuple
from PIL import Image as Pilimage, ImageDraw
from .type import LayoutType, Direction
import io

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Canvas:
    def __init__(
        self,
        size: Tuple[int, int] = (100, 100),
        display: Union[LayoutType, None] = None,
    ):
        self._size = size
        self._image = Pilimage.new("RGBA", size)
        self._draw = ImageDraw.Draw(self._image)
        self._spacing = 2
        self._display = display
        self.root_group = Group(display=display, direction=Direction.COLUMN)
        self.root_group.set_parent(self)
        self.root_group.spacing = self._spacing
        self.root_group.poss = (0, 0, self._size[0], self._size[1])
        self.root_group.draw = self._draw

    def add_component(self, component):
        return self.root_group.add(component)

    def render(self):
        logger.debug("Starting canvas render")
        self.root_group.render()
        logger.debug("Finished canvas render")
        return self._image

    def group(self, direction=Direction.ROW):
        return Group(direction=direction)

    def text(self, content:str):
        return Text(content)

    def image(self, image: Union[Pilimage.Image, io.BytesIO, str]):
        return Image(self._image, image)

    def levelline(self, nowlevel:int,nextlevel:int, linestyle):
        return Levelline(nowlevel, nextlevel, linestyle)

    def get_spacing(self):
        return self._spacing

    def get_poss(self):
        return (0, 0, self._size[0], self._size[1])

    def get_draw(self):
        return self._draw
