from colors import color


def group(group: dict):
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


def bulb(bulb: dict):
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
