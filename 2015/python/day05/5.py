from re import search
from string import ascii_lowercase

doubleletters = [i + i for i in ascii_lowercase]
pairs = [i + j for i in ascii_lowercase for j in ascii_lowercase]
forbiddenstrings = ('ab', 'cd', 'pq', 'xy')


def noforbiddenstrings(fstr, input):
    for line in input:
        if not sum(map(line.count, fstr)):
            yield line


def hasnumvowels(num, input):
    for line in input:
        vowels = ('a', 'e', 'i', 'o', 'u')
        if sum(map(line.count, vowels)) >= num:
            yield line


def doubleletter(input):
    for line in input:
        if sum(map(line.count, doubleletters)) > 0:
            yield line


def pairletters(input):
    for line in input:
        for pair in pairs:
            if line.count(pair) > 1:
                yield line
                break

with open('../../input/day05/input') as input:
    noforbidden = noforbiddenstrings(forbiddenstrings, input)
    hasdouble = doubleletter(noforbidden)
    vowelreq = hasnumvowels(3, hasdouble)
    print(len(list(vowelreq)))


with open('../../input/day05/input') as input:
    lineswithpairs = pairletters(input)
    lineswithreps = (line for line in lineswithpairs if search(
        r"([a-z])[a-z]\1", line))
    print(len(list(lineswithreps)))
