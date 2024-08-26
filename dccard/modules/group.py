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
                i.group = self
                self.items.append(i)
        else:
            item.group = self
            self.items.append(item)
        return item

    def render(self, context):
        logger.debug(f"Rendering group: direction={self.direction}, items={len(self.items)}")
        logger.debug(f"Context: {context}")

        if not self.items:
            logger.debug("No items to render")
            return

        poss = context['poss']
        if not poss:
            logger.debug("No position information")
            return

        group_width = poss[2] - poss[0]
        group_height = poss[3] - poss[1]

        if self.direction == Direction.ROW:
            self._render_row(context, group_width, group_height)
        elif self.direction == Direction.COLUMN:
            self._render_column(context, group_width, group_height)

    def _render_row(self, context, group_width, group_height):
        logger.debug(f"Rendering row: width={group_width}, height={group_height}")
        x = context['poss'][0]
        item_width = (group_width - (len(self.items) - 1) * self.spacing) // len(self.items)

        for i, item in enumerate(self.items):
            item_context = {
                'spacing': self.spacing,
                'poss': (int(x), int(context['poss'][1]), int(x + item_width), int(context['poss'][3])),
                'draw': context['draw']
            }
            logger.debug(f"Rendering item {i} in row: {item_context}")
            item.render(item_context)
            x += item_width + self.spacing

    def _render_column(self, context, group_width, group_height):
        logger.debug(f"Rendering column: width={group_width}, height={group_height}")
        y = context['poss'][1]
        item_height = (group_height - (len(self.items) - 1) * self.spacing) // len(self.items)

        for i, item in enumerate(self.items):
            item_context = {
                'spacing': self.spacing,
                'poss': (int(context['poss'][0]), int(y), int(context['poss'][2]), int(y + item_height)),
                'draw': context['draw']
            }
            logger.debug(f"Rendering item {i} in column: {item_context}")
            item.render(item_context)
            y += item_height + self.spacing