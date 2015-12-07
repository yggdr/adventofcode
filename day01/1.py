with open('input') as fh:
    input=fh.read()

print(input.count('(')-input.count(')'))

for i,_ in enumerate(input):
    if input.count('(', 0, i) - input.count(')', 0, i) == -1:
        print(i)
        exit()
