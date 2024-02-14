from functools import reduce

digit = 125

sum_digit = reduce(lambda x, y: x + y, [int(d) for d in str(digit)])

print(sum_digit)