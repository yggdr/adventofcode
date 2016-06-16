totalwrapping, totalribbon = 0, 0
with open('../../input/day02/input') as fh:
    for line in fh:
        dim = [int(i) for i in line.split('x')]
        dim.sort()
        ribbon = 2 * (dim[0] + dim[1]) + dim[0] * dim[1] * dim[2]
        wrapping = 3 * dim[0] * dim[1] + 2 * (dim[1] * dim[2] + dim[0] * dim[2])
        totalwrapping += wrapping
        totalribbon += ribbon
print(totalwrapping)
print(totalribbon)
