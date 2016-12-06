def are_valid(tris):
    for tri in tris:
        s1, s2, s3 = sorted(map(int, tri.split()))
        yield s1 + s2 > s3

with open('../../input/day03/input') as tris:
    print(list(are_valid(tris)).count(True))

new_list = []
with open('../../input/day03/input') as tris:
    try:
        while True:
            l1 = map(int, next(tris).split())
            l2 = map(int, next(tris).split())
            l3 = map(int, next(tris).split())
            new_list.extend(' '.join(map(str, sides)) for sides in zip(l1, l2, l3))
    except StopIteration:
        pass

print(list(are_valid(new_list)).count(True))
