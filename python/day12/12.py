import json


def deepiter(obj, ignore_red=False):
    if isinstance(obj, list):
        for O in obj:
            yield from deepiter(O, ignore_red)
    elif isinstance(obj, dict):
        if ignore_red and ("red" in obj or "red" in obj.values()):
            yield 0
        else:
            for K, V in obj.items():
                yield from deepiter(K, ignore_red)
                yield from deepiter(V, ignore_red)
    elif isinstance(obj, int):
        yield obj
    else:
        yield 0

if __name__ == '__main__':
    with open('../../input/day12/input') as fh:
        input = json.load(fh)
    print(sum(deepiter(input)))
    print(sum(deepiter(input, True)))
