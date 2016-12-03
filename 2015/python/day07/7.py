from collections import namedtuple

Wire = namedtuple('Wire', ['in', 'out'])
wires, ands, ors, nots, rshifts, lshifts = {}, {}, {}, {}, {}, {}
with open('../../input/day07/input') as fh:
    for instruction in fh:
        input, output = instruction.rstrip().split(' -> ')
        if 'AND' in input:
            op1, op2 = input.split(' AND ')
            wires[output] = wires[op1] & wires[op2]
        elif 'OR' in input:
            op1, op2 = input.split(' OR ')
            wires[output] = wires[op1] | wires[op2]
        elif 'NOT' in input:
            # hopefully NOT doesn't get directly applied to numbers...
            wires[output] = ~wires[input.split('NOT ')[1]] & 65535
        elif 'LSHIFT' in input:
            op1, op2 = input.split(' LSHIFT ')
            wires[output] = wires[op1] << int(op2)
        elif 'RSHIFT' in input:
            op1, op2 = input.split(' RSHIFT ')
            wires[output] = wires[op1] >> int(op2)
        else:
            wires[output] = int(input)
