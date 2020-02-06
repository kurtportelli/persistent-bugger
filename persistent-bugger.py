import operator, functools

def persistence(n):
    count = 0
    while n > 9:
        len_of_num = len(str(n))
        split_num = [int(str(n)[index]) for index in range(len_of_num)]
        n = functools.reduce(operator.mul, split_num)
        count = count + 1
    return count
