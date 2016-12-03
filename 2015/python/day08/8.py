length, memlength, encodedlength, skip = 0, 0, 0, 0
with open('../../input/day08/input') as input:
    for line in input:
        line = line.strip()[1:-1]
        memlength += len(line) + 2
        # Compensate for the [1:-1], then add \" at beginning and end, makes 6
        encodedlength += 6
        for pos, char in enumerate(line):
            encodedlength += 2 if char in "\"\\" else 1
            if skip:
                skip -= 1
                continue
            length += 1
            if char == "\\":
                if line[pos + 1] == 'x':
                    skip = 3
                elif line[pos + 1] in "\\\"":
                    skip = 1

print(memlength, length, memlength - length,
      encodedlength, encodedlength - memlength)
