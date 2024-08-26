from enum import Enum


class LayoutType(Enum):
    PROPORTION = "proportion"
    FLEX = "flex"
    GRID = "grid"


class Direction(Enum):
    ROW = "row"
    COLUMN = "column"
