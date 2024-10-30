import io
import logging
from typing import Tuple, Union

from PIL import Image as Pilimage
from PIL import ImageDraw

from .modules import Displaylist, Group, Image, Levelline, Text
from .type import Direction, LayoutType

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Canvas:
    def __init__(
        self,
        size: Tuple[int, int] = (100, 100),
        display: Union[LayoutType, None] = None,
    ):
        self._size: Tuple[int, int] = size
        self._image: Pilimage.Image = Pilimage.new("RGBA", size)
        self._draw: ImageDraw.ImageDraw = ImageDraw.Draw(self._image)
        self._spacing: int = 2
        self._display: Union[LayoutType, None] = display
        self.root_group: Group = Group(display=display, direction=Direction.COLUMN)
        self.root_group.set_parent(self)
        self.root_group.spacing = self._spacing
        self.root_group.poss = (0, 0, self._size[0], self._size[1])
        self.root_group.draw = self._draw

    def add_component(
        self, component: Union[Text, Image, Group, Levelline, Displaylist]
    ):
        return self.root_group.add(component)

    def render(self) -> Pilimage.Image:
        logger.debug("Starting canvas render")
        self.root_group.render()
        logger.debug("Finished canvas render")
        return self._image

    def group(self, direction: Direction = Direction.ROW) -> Group:
        return Group(direction=direction)

    def text(self, content: str) -> Text:
        return Text(content)

    def image(self, image: Union[Pilimage.Image, io.BytesIO, str]) -> Image:
        return Image(self._image, image)

    def levelline(self, nowlevel: int, nextlevel: int, linestyle: str) -> Levelline:
        return Levelline(nowlevel, nextlevel, linestyle)

    def displaylist(
        self, images: list[Pilimage.Image | str], size: tuple[int, int]
    ) -> Displaylist:
        return Displaylist(self._image, images, size)

    def get_spacing(self) -> int:
        return self._spacing

    def get_poss(self) -> Tuple[int, int, int, int]:
        return (0, 0, self._size[0], self._size[1])

    def get_draw(self) -> ImageDraw.ImageDraw:
        return self._draw
