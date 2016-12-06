from collections import Counter
from itertools import groupby, tee
from string import ascii_lowercase

class AlphaCounter(Counter):
    def most_common(self, n=None):
        most = super().most_common(n)
        least_most = most[-1][1]
        num_least = sum(1 for _, count in most if count == least_most)
        first = most[:len(most) - num_least]
        groups = [(k, list(g)) for k, g in groupby(first, key=lambda x: x[1])]
        sorted_least = sorted(char for char, howoften in self.items() if howoften == least_most)[:num_least]
        return list(self._group_sorted(groups)) + [(item, least_most) for item in sorted_least]

    def _group_sorted(self, groups):
        for num, lst in groups:
            for char, _ in sorted(lst):
                yield char, num

def calc_chksum(name):
    return ''.join(k for k, v in AlphaCounter(name).most_common(5))

def valid_chksum(lines, func=lambda splitted: int(splitted[-1].split('[')[0])):
    for line in lines:
        splitted = line.strip().split('-')
        if calc_chksum(''.join(splitted[:-1])) == splitted[-1].split('[')[1][:-1]:
            yield func(splitted)

def rot(char, num):
    return ascii_lowercase[(ascii_lowercase.index(char) + num) % 26]

with open('../../input/day04/input') as fh:
    fh1, fh2 = tee(fh)
    print(sum(valid_chksum(fh1)))
    for encoded, num in valid_chksum(fh2, func=lambda splitted: (splitted[:-1], splitted[-1].split('[')[0])):
        roomname = ' '.join(encoded)
        decoded = ''.join(char if char == ' ' else rot(char, int(num)) for char in roomname)
        if 'object' in decoded:
            print(num)
