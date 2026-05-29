from enum import Enum


class GameState(Enum):
    MAIN_CAFE   = "main_cafe"
    CASHIER_POV = "cashier_pov"
    MAKE_DRINK  = "make_drink"


class BaristaState(Enum):
    IDLE    = "idle"
    WALKING = "walking"
    SERVING = "serving"
    MAKING  = "making"


class CustomerState(Enum):
    WALKING  = "walking"
    WAITING  = "waiting"
    ORDERING = "ordering"
    LEAVING  = "leaving"