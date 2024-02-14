from functools import reduce

def find_max(lst, lmd):
    the_max = reduce(lmd, lst)
    return the_max

numbers = [13, 2, 49, 104, 322, 21]

max_finder = lambda x, y: x if x > y else y

print(find_max(numbers, max_finder))