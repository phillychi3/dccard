from ..Component import BaseComponent
from ..type import Direction
import logging

logger = logging.getLogger(__name__)


class Group(BaseComponent):
    def __init__(self, display=None, direction=Direction.ROW):
        super().__init__()
        self.background = None
        self.frame = None
        self.spacing = 1
        self.display = display
        self.direction = direction
        self.items = []

    def add(self, item):
        if isinstance(item, list):
            for i in item:
                i.set_parent(self)
                self.items.append(i)
        else:
            item.set_parent(self)
            self.items.append(item)
        return item

    def _render(self):
        logger.debug(
            f"Rendering group: direction={self.direction}, items={len(self.items)}"
        )
        if not self.items:
            logger.debug("No items to render")
            return
        poss = self.get_poss()
        if not poss:
            logger.debug("No position information")
            return
        group_width = poss[2] - poss[0]
        group_height = poss[3] - poss[1]
        if self.direction == Direction.ROW:
            self._render_row(group_width, group_height)
        elif self.direction == Direction.COLUMN:
            self._render_column(group_width, group_height)

    def _render_row(self, group_width, group_height):
        x = self.get_poss()[0]
        item_width = (group_width - (len(self.items) - 1) * self.get_spacing()) // len(
            self.items
        )
        for i, item in enumerate(self.items):
            item.poss = (
                int(x),
                int(self.get_poss()[1]),
                int(x + item_width),
                int(self.get_poss()[3]),
            )
            item.draw = self.get_draw()
            logger.debug(f"Rendering item {i} in row: {item.poss}")
            item.render()
            x += item_width + self.get_spacing()

    def _render_column(self, group_width, group_height):
        y = self.get_poss()[1]
        item_height = (
            group_height - (len(self.items) - 1) * self.get_spacing()
        ) // len(self.items)
        for i, item in enumerate(self.items):
            item.poss = (
                int(self.get_poss()[0]),
                int(y),
                int(self.get_poss()[2]),
                int(y + item_height),
            )
            item.draw = self.get_draw()
            logger.debug(f"Rendering item {i} in column: {item.poss}")
            item.render()
            y += item_height + self.get_spacing()
