import enum


class LightColour(enum.Enum):
    White = "f5faf6"
    Warm = "f1e0b5"
    Glow = "efd275"

    Blue = "4a418a"
    LightBlue = "6c83ba"
    SaturatedPurple = "8f2686"
    Lime = "a9d62b"
    LightPurple = "c984bb"
    Yellow = "d6e44b"
    SaturatedPink = "d9337c"
    DarkPeach = "da5d41"
    SaturatedRed = "dc4b31"
    ColdSky = "dcf0f8"
    Pink = "e491af"
    Peach = "e57345"
    WarmAmber = "e78834"
    LightPink = "e8bedd"
    CoolDaylight = "eaf6fb"
    Candlelight = "ebb63e"
    WarmGlow = "efd275"
    WarmWhite = "f1e0b5"
    Sunrise = "f2eccf"
    CoolWhite = "f5faf6"


def toggle(active: bool) -> dict:
    """Returns the settings payload for toggling a light."""
    return {5850: int(active)}


def dim(brightness: int) -> dict:
    """Returns the settings payload for dimming a light."""
    return {5851: int(brightness * 2.55)}


def colour(colour: LightColour) -> dict:
    """Returns the settings payload for changing a light's colour."""
    return {5706: colour.value}
