from collections import Counter
from itertools import tee

def getchar(fh, n=None):
    for chars in zip(*fh):
        yield Counter(chars).most_common(n).pop()[0]

with open('input') as fh:
    fh1, fh2 = tee(fh.readlines())
    print(''.join(getchar(fh1, 1)))
    print(''.join(getchar(fh2)))
