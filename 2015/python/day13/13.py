import re
from itertools import permutations
# from collections import namedtuple

# SubjectiveHappiness = namedtuple('SubjectiveHappiness', 'subject happiness')


def total_happiness(happiness, order):
    return sum(individual_happiness(happiness, order, P, i) for i, P in enumerate(order))


def individual_happiness(happiness, order, P, i):
    return happiness[P][order[i - 1]] + happiness[P][order[(i + 1) % len(order)]]


def gethappiness(file):
    fornumbers = re.compile(r"([0-9]+)")
    for line in file:
        happiness = int(re.search(fornumbers, line).group())
        line = line.split()
        obj, gainorlose, subj = line[0], line[2], line[-1][:-1]
        if gainorlose == 'lose':
            happiness *= -1
        # yield obj, SubjectiveHappiness(subj, happiness)
        yield obj, {subj: happiness}

if __name__ == '__main__':
    with open('../../input/day13/input') as fh:
        file = fh.readlines()
    file = list(map(str.strip, file))
    happiness = {}
    for name, happ in gethappiness(file):
        try:
            happiness[name].update(happ)
        except KeyError:
            happiness[name] = happ
    print(max(total_happiness(happiness, permutation)
              for permutation in permutations(happiness)))
    # To make sure I don't change the dict while iterating over it
    for name, happlist in happiness.items():
        happlist.update({'ME': 0})
    happiness['ME'] = {}
    for name in happiness:
        happiness['ME'].update({name: 0})
    print(max(total_happiness(happiness, permutation)
              for permutation in permutations(happiness)))
