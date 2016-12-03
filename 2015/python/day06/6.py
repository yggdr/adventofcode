from collections import namedtuple


def point(x, y):
    return Point(int(x), int(y))
Point = namedtuple('Point', ['x', 'y'])


def on(grid, i, j):
    grid[(i, j)] = 1


def off(grid, i, j):
    grid[(i, j)] = 0


def toggle(grid, i, j):
    grid[(i, j)] = 0 if grid[(i, j)] else 1


def on_corrected(grid, i, j):
    grid[(i, j)] += 1


def off_corrected(grid, i, j):
    grid[(i, j)] -= 1
    grid[(i, j)] = max(0, grid[(i, j)])


def toggle_corrected(grid, i, j):
    grid[(i, j)] += 2


def luminosity(on, off, toggle):
    grid = {(x, y): 0 for x in range(1000) for y in range(1000)}
    with open('../../input/day06/input') as fh:
        for instruction in fh:
            head, endrange = instruction.split(' through ')
            if head.startswith('turn on'):
                spliton = 'turn on '
                action = on
            elif head.startswith('turn off'):
                spliton = 'turn off '
                action = off
            elif head.startswith('toggle'):
                spliton = 'toggle '
                action = toggle
            else:
                raise ValueError('Illegal Input')
            start = point(*head.split(spliton)[1].split(','))
            end = point(*endrange.split(','))
            for x in range(start.x, end.x + 1):
                for y in range(start.y, end.y + 1):
                    action(grid, x, y)

    return sum(grid.values())

print(luminosity(on, off, toggle))
print(luminosity(on_corrected, off_corrected, toggle_corrected))
