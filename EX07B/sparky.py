"""Simulation."""


def simulate(wmap: list, moves: list) -> list:
    """
    Simulate a robotic lawn mower.

    :param wmap: A list of strings indicating rows that make up the map.
                 The map is always rectangular and the minimum given size is 1x1.
                 Cut grass is indicated by the symbol ('-'), low grass by ('w') and high grass by ('W').
                 The robot position is indicated by the symbol ('X'). There is always one robot on the map.
                 Obstacles are indicated by the symbol ('#').

    :param moves: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the robot out of bounds or crash it into an obstacle.

    :return: A list of strings indicating rows that make up the map. Same format as the given wmap.

    Grass under Sparky's starting position is always cut grass ('-').
    If Sparky mows high grass, it first turns into low grass ('w') and then from low grass into cut grass ('-').
    """
    x, y = coordinates(wmap)
    wmap, x, y = moveset(wmap, moves, x, y)
    wmap[y] = wmap[y][:x] + 'X' + wmap[y][1 + x:]

    return wmap


def change_letters(letter: str):
    """Change letters if possible."""
    if letter == "W":
        return "w"
    elif letter == "w":
        return "-"
    return letter


def coordinates(wmap: list):
    """Getting beginning coordinates."""
    x = 0
    y = 0
    for i in range(len(wmap)):
        if 'X' in wmap[i]:
            y = i
            x = wmap[i].index('X')
    return x, y


def moveset(wmap: list, moves: list, x, y):
    """WAS sth."""
    grass = '-'
    for move in moves:
        wmap[y] = wmap[y][:x] + grass+ wmap[y][1 + x:]
        if move == 'N':
            if y == 0 or wmap[y - 1][x] == '#':
                continue
            y = y - 1
        elif move == 'S':
            if y == len(wmap) - 1 or wmap[y + 1][x] == '#':
                continue
            y = y + 1
        elif move == 'E':
            if x == len(wmap[0]) - 1 or wmap[y][x + 1] == '#':
                continue
            x = x + 1
            x = x - 1
        grass = change_letters(wmap[y][x])

    return wmap, x, y





if __name__ == '__main__':
    wmap1 = [
        "#www-",
        "wXw#-"
    ]

    moves1 = ["N", "E", "E", "S", "E"]
    print((simulate(wmap1, moves1)))

    # #---X
    # w-w#-

    # assert simulate(wmap1, moves1) == ["#---X", "w-w#-"]

    wmap2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    moves2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print((simulate(wmap2, moves2)))

    # wwwW
    # ---W
    # -X#W

    # assert simulate(wmap2, moves2) == ["wwwW", "---W", "-X#W"]
