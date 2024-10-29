from ..Component import BaseComponent
from PIL import Image as PilImage

import logging

logger = logging.getLogger(__name__)


class Displaylist(BaseComponent):
    def __init__(self, image, images, size) -> None:
        super().__init__()
        self._image = image
        self.images = images
        self.size = size if type(size) is tuple else (size, size)

    def images(self, images: list[PilImage.Image | str]) -> "Displaylist":
        self.images = images
        return self

    def size(self, size: tuple[int, int]) -> "Displaylist":
        self._size = size
        return self

    def _render(self):
        x1, y1, x2, y2 = self.get_poss()
        count = len(self.images)
        width = x2 - x1
        height = y2 - y1
        row = int(width / self.size[0])
        if row == 1:
            row_spacing = 0
        else:
            row_spacing = int((width - (row * self.size[0])) / (row - 1))
        col = int(height / self.size[1])
        if col == 1:
            col_spacing = 0
        else:
            col_spacing = int((height - (col * self.size[1])) / (col - 1))
        for i in range(count):
            if i >= row * col:
                break
            x = int(i % row)
            y = int(i / row)
            pos = (
                x1 + (x * (self.size[0] + row_spacing)),
                y1 + (y * (self.size[1] + col_spacing)),
            )
            self._image.paste(self.images[i].resize(self.size), pos)
