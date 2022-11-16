"""
Brandon Treu
assign_level.py
"""


def switch_average(letter):
    min_score = {'A': 500,'E': 300,'B': 150,'N': 50}

    switch = min_score.get(letter, lambda: 'Not a Valid Entry')
    return switch


if __name__ == '__main__':
    switch_average('H')