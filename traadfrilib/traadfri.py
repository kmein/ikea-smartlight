from colors import color

import subprocess
import json
import enum
from typing import Optional


class LightColour(enum.Enum):
    WARM = 1
    NORMAL = 0
    COLD = -1


def print_group_info(group: dict):
    try:
        active = group["5850"] == 1
        group_id = group["9003"]
        group_name = group["9001"]
        print(
            "{} (#{}): {}",
            color(group_name, style="bold"),
            group_id,
            color("on", fg="green") if active else color("off", fg="red"),
        )
    except KeyError:
        pass


def print_bulb_info(bulb: dict):
    try:
        bulb_id = bulb["9003"]
        bulb_name = bulb["9001"]
        active = bulb["3311"][0]["5850"] == 1
        brightness = bulb["3311"][0]["5851"]
        try:
            warmth_raw = float(bulb["3311"][0]["5711"])
            warmth = round((warmth_raw - 250) / (454 - 250) * 100, 1)
        except KeyError:
            warmth = float("NaN")
        print(
            "{} (#{}): {}, bright {}%, warm {}%".format(
                color(bulb_name, style="bold"),
                bulb_id,
                color("on", fg="green") if active else color("off", fg="red"),
                brightness,
                color(warmth, fg="yellow")
                if warmth > 66.6
                else color(warmth, fg="blue")
                if warmth <= 33.3
                else warmth,
            )
        )
    except KeyError:
        pass


def traadfri_group(hub_ip: str, group_id: Optional[int]) -> str:
    """Builds a Trådfri group URI from gatewaay IP and group ID.
    If no group ID is given, the URI for the groups query endpoint is returned."""
    return "coaps://{}:5684/15004{}".format(hub_ip, f"/{group_id}" if group_id else "")


def traadfri_bulb(hub_ip: str, bulb_id: Optional[int]) -> str:
    """Builds a Trådfri lightbulb URI from gatewaay IP and lightbulb ID.
    If no lightbulb ID is given, the URI for the lightbulbs query endpoint is returned."""
    return "coaps://{}:5684/15001{}".format(hub_ip, f"/{bulb_id}" if bulb_id else "")


def light_toggle(active: bool) -> dict:
    """Returns the settings payload for toggling a light."""
    return {5850: int(active)}


def light_dim(brightness: float) -> dict:
    """Returns the settings payload for dimming a light."""
    return {5851: int(brightness * 2.55)}


def light_colour(colour: LightColour) -> dict:
    """Returns the settings payload for changing a light's colour."""
    if colour is LightColour.WARM:
        return {5709: 33135, 5710: 27211}
    elif colour is LightColour.NORMAL:
        return {5709: 30140, 5710: 26909}
    elif colour is LightColour.COLD:
        return {5709: 24930, 5710: 24684}
    else:
        raise ValueError()


def coap_put(user: str, key: str, uri: str, settings: dict) -> None:
    """Writes a settings payload to a CoAP URI (using the specified user and API key)."""
    payload = json.dumps({3311: [settings]})
    subprocess.run(["coap-client", "-m put", "-u", user, "-k", key, "-e", payload, uri])


def coap_get(user: str, key: str, uri: str, timeout: int = 5) -> dict:
    """Reads from a CoAP URI (using the specified user and API key)."""
    output = subprocess.run(
        ["coap-client", "-m get", "-u", user, "-k", key, "-B", str(timeout), uri],
        capture_output=True,
    ).stdout
    return json.loads(output.splitlines()[-1])
