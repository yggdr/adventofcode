orientation = 1j
spot = 0
visited = [spot]
visited_twice = []
with open('../../input/day01/input') as inp:
    directions = inp.readline().strip().split(', ')

for LR, *howfar in directions:
    howfar = int(''.join(howfar))
    orientation *= 1j if LR == 'L' else -1j
    for i in range(howfar):
        spot += orientation
        if spot in visited:
            visited_twice += [spot]
        visited += [spot]

print(abs(spot.real) + abs(spot.imag))
print(abs(visited_twice[0].real) + abs(visited_twice[0].imag))
