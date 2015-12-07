from itertools import count
from md5 import md5

def findnumzeros(input, numzeros):
    zeros='0'*numzeros
    for i in count():
        if md5(input+str(i)).hexdigest()[:numzeros]==zeros:
            return i

input='iwrupvqb'

print findnumzeros(input, 5)
print findnumzeros(input, 6)
