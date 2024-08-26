from ..Component import BaseComponent

import logging
logger = logging.getLogger(__name__)

class Text(BaseComponent):
    def __init__(self, content):
        super().__init__()
        self.content = content
        self._font = None
        self._color = "black"

    def font(self, font):
        self._font = font

    def color(self, color):
        self._color = color

    def render(self, context):
        logger.debug(f"Rendering text: {self.content}")
        logger.debug(f"Context: {context}")
        if context['poss'] and 'draw' in context:
            x, y, _, _ = context['poss']
            context['draw'].text((x, y), self.content, font=self._font, fill=self._color)
        else:
            logger.warning("Invalid context for text rendering")