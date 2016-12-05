from itertools import count
from random import randint
from string import ascii_lowercase
from hashlib import md5

doorID = 'ffykfhsq'

def code(advanced=False):
    for i in count():
        hash = md5((doorID + str(i)).encode('utf8')).hexdigest()
        if hash[:5] == '0' * 5:
            if advanced:
                yield hash[5:7]
            else:
                yield hash[5]
        elif advanced:
            yield None, None

gen_code = code()
print(''.join(next(gen_code) for i in range(8)))

unfilled = list(range(8))
passwd = ['_' for i in range(8)]
for pos, val in code(True):
    try:
        pos = int(pos)
    except (TypeError, ValueError):
        continue
    finally:
        if randint(0, 1500) == 0:
            print(''.join(char if char != '_' else ascii_lowercase[randint(0, len(ascii_lowercase) - 1)] for char in passwd), end='\r')
    if pos in unfilled:
        passwd[pos] = val
        unfilled.pop(unfilled.index(pos))
        if not unfilled:
            break
print(''.join(passwd))
