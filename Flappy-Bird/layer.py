from enum import IntEnum, auto

# Order of the different layers
class Layer(IntEnum):
    BACKGROUND = auto()
    OBSTACLE = auto()
    FLOOR = auto()
    UI = auto()
    PLAYER = auto()
    
    