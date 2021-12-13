def square(num):
    return num*num


def _abs_(num):
    if num >= 0:
        return num
    else:
        return num*-1


def _round_(num, length):
    text = str(num)
    decimal = ''
    integer = ''
    not_int = False
    for i in text:
        if not_int:
            decimal += i
        elif i != '.':
            integer += i
        if i == '.':
            not_int = True
    integer = int(integer)
    decimal = decimal[0:length]
    return integer + int(decimal)/(10**length)


def _sqrt_(num, tol = 0.001, decimals = 3):
    sq = num/2
    n0 = 0
    n1 = num
    while _abs_(square(sq) - num) >= _abs_(tol):
        if square(sq) == num:
            return sq
        elif square(sq) < num:
            n0 = sq
        else:
            n1 = sq
        sq = n0 + (n1 - n0)/2
    return _round_(sq, decimals)
