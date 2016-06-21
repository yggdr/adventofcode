from collections import namedtuple
from operator import attrgetter

reindeer = namedtuple('Reindeer', 'name, speed, flytime, resttime, points')


def distance(deer, racetime):
    whole, part = divmod(racetime, deer.flytime + deer.resttime)
    return (whole * deer.flytime + min(deer.flytime, part)) * deer.speed


def update_points(Reindeer, racetime):
    longest_distance = max(distance(deer, racetime) for deer in Reindeer)
    Reindeer = [deer._replace(points=deer.points + 1 if distance(deer, racetime)
                              == longest_distance else deer.points) for deer in Reindeer]
    return Reindeer

if __name__ == '__main__':
    racetime = 2503
    with open('../../input/day14/input') as fh:
        splitted = (line.split(' ') for line in fh)
        Reindeer = [reindeer(line[0], int(line[3]), int(
            line[6]), int(line[13]), 0) for line in splitted]

    print(max(distance(deer, racetime) for deer in Reindeer))
    for i in range(racetime):
        Reindeer = update_points(Reindeer, i + 1)
    print(max(Reindeer, key=attrgetter('points')).points)
