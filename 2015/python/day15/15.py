# This all feels very brute-force...

from itertools import permutations, tee
from functools import reduce
from collections import namedtuple

Ingredient = namedtuple(
    "Ingredient", 'capacity, durability, flavor, texture, calories')


def score(combination, ingredients, cal=None):
    weighted_ingredients = map(
        lambda x: [x[0] * int(i) for i in x[1]], zip(combination, ingredients))
    capacity, durability, flavor, texture, calories = [], [], [], [], []
    for wi in weighted_ingredients:
        capacity.append(wi[0])
        durability.append(wi[1])
        flavor.append(wi[2])
        texture.append(wi[3])
        calories.append(wi[4])
    if cal and sum(calories) != cal:
        return 0
    return reduce(lambda x, acc: x * acc, (max(0, sum(stuff)) for stuff in [capacity, durability, flavor, texture]))

if __name__ == '__main__':
    total_teaspoons = 100
    with open('../../input/day15/input') as fh:
        lines = (line.split(": ", 1) for line in fh)
        line_with_ingredients = (
            (line[0], dict(map(str.split, line[1].split(', ')))) for line in lines)
        ingredients = [Ingredient(**line[1])
                       for line in line_with_ingredients]
    perms = permutations(range(total_teaspoons + 1), len(ingredients))
    combinations, combinations_500 = tee(
        (perm for perm in perms if sum(perm) == 100), 2)
    print(max(score(combination, ingredients) for combination in combinations))
    print(max(score(combination, ingredients, 500)
              for combination in combinations_500))
