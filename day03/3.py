with open('input') as fh:
    input=fh.read()

class Plane(object):
    def __init__(self):
        self.x, self.y = 0, 0
        self.plane={(0,0): 1}

    def __len__(self):
        return len(self.plane)

    def __add__(self, other):
        self.plane.update(other.plane)
        return self

    def move(self, dir):
        if dir=='>':
            self.x+=1
        elif dir=='<':
            self.x-=1
        elif dir=='^':
            self.y+=1
        elif dir=='v':
            self.y-=1
        else:
            raise ValueError('Illegal Input')
        self.add(self.x, self.y)

    def add(self,x,y):
        try:
            self.plane[(self.x,self.y)]+=1
        except KeyError:
            self.plane[(self.x,self.y)]=1

def rundir(plane, input):
    for dir in input:
        plane.move(dir)

P=Plane()
rundir(P, input)
print(len(P))

P1=Plane()
P2=Plane()
rundir(P1, input[::2])
rundir(P2, input[1::2])
print(len(P1+P2))
