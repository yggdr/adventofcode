import re

encoding = {'U': 1j, 'R': 1, 'D': -1j, 'L': -1}
layout = {
        -1+1j: 1,  1j: 2, 1+1j: 3,
        -1:    4,   0: 5,    1: 6,
        -1-1j: 7, -1j: 8, 1-1j: 9
}
strange_layout = {
                              2j:  1,
               -1+1j:  2,     1j:  3,    1+1j:  4,
        -2: 5, -1:     6,      0:  7,       1:  8, 2: 9,
               -1-1j: 'A',   -1j: 'B',   1-1j: 'C',
                             -2j: 'D',
}

def decode():
    pos = 0
    with open('../../input/day02/input') as fh:
        for seq in fh:
            seq = seq.strip()
            mapped = map(lambda x: (x[0], len(x)), re.findall(r'U+|R+|D+|L+', seq))
            for dir, length in mapped:
                pos += length * encoding[dir]
                pos = complex(max(min(pos.real, 1), -1),
                              max(min(pos.imag, 1), -1))
            yield layout[pos]

def decode_strange():
    pos = -2j
    with open('../../input/day02/input') as fh:
        # fh = ['LUURULUR']
        for seq in fh:
            seq = seq.strip()
            mapped = map(lambda x: (x[0], len(x)), re.findall(r'U+|R+|D+|L+', seq))
            for dir, length in mapped:
                new_pos = pos
                for i in range(length):
                    new_pos += encoding[dir]
                    if new_pos not in strange_layout:
                        break
                    pos = new_pos
            yield strange_layout[pos]

print(list(decode()))
print(list(decode_strange()))
