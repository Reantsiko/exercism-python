resistor_colors = {"black": 0, "brown": 1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8,"white":9}

def value(colors):
    return int(f'{resistor_colors[colors[0]]}{resistor_colors[colors[1]]}')
