from functools import reduce


def looksay(string):
    S = list(string)
    last = S.pop(0)
    curcount = 1
    res = ""
    while True:
        try:
            new = S.pop(0)
        except IndexError:
            res += str(curcount) + last
            break
        if last == new:
            curcount += 1
        else:
            res += str(curcount) + last
            last = new
            curcount = 1
    return res

if __name__ == '__main__':
    # for i in range(6):
    #     print(reduce(lambda x, y: y(x), [looksay] * i, "1"))
    after40 = reduce(lambda x, y: y(x), [looksay] * 40, "1113222113")
    print(len(after40))
    # This takes hours somehow?!
    after50 = reduce(lambda x, y: y(x), [looksay] * 10, after40)
    print(len(after50))
