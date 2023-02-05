resistor_colors = {"black": 0, "brown": 1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8,"white":9}

def color_code(color: str) -> int:
    return resistor_colors[str.lower(color)]


def colors() -> list:
    return list(resistor_colors.keys())
