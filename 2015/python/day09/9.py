from itertools import permutations


def calcdistance(way, distances):
    total = 0
    for pos, city in enumerate(way):
        if pos + 1 == len(way):
            break
        try:
            total += distances[(city, way[pos + 1])]
        except KeyError:
            total += distances[(way[pos + 1], city)]
    return total

with open('../../input/day09/input') as input:
    distances = {}
    for line in input:
        from_, _, to, _, distance = line.split()
        distances[(from_, to)] = int(distance)

for way in permutations({i for i, _ in distances} | {i for _, i in distances}):
    d = calcdistance(way, distances)
    try:
        if d < shortestway[1]:
            shortestway = (way, d)
    except (NameError, IndexError):
        shortestway = (way, d)
    try:
        if d > longestway[1]:
            longestway = (way, d)
    except (NameError, IndexError):
        longestway = (way, d)

print(shortestway)
print(longestway)
