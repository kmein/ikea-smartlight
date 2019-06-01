import enum
from decimal import Decimal, getcontext


class LightColour(enum.Enum):
    WARM = 1
    NORMAL = 0
    COLD = -1


def toggle(active: bool) -> dict:
    """Returns the settings payload for toggling a light."""
    return {5850: int(active)}


def dim(brightness: int) -> dict:
    """Returns the settings payload for dimming a light."""
    getcontext().prec = 3
    return {5851: int(brightness * Decimal(2.55))}


def colour(colour: LightColour) -> dict:
    """Returns the settings payload for changing a light's colour."""
    if colour is LightColour.WARM:
        return {5709: 33135, 5710: 27211}
    elif colour is LightColour.NORMAL:
        return {5709: 30140, 5710: 26909}
    elif colour is LightColour.COLD:
        return {5709: 24930, 5710: 24684}
    else:
        raise ValueError()
