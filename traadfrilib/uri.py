from typing import Optional


def group(hub_ip: str, group_id: Optional[int]) -> str:
    """Builds a Trådfri group URI from gatewaay IP and group ID.
    If no group ID is given, the URI for the groups query endpoint is returned."""
    return "coaps://{}:5684/15004{}".format(hub_ip, f"/{group_id}" if group_id else "")


def bulb(hub_ip: str, bulb_id: Optional[int]) -> str:
    """Builds a Trådfri lightbulb URI from gatewaay IP and lightbulb ID.
    If no lightbulb ID is given, the URI for the lightbulbs query endpoint is returned."""
    return "coaps://{}:5684/15001{}".format(hub_ip, f"/{bulb_id}" if bulb_id else "")
