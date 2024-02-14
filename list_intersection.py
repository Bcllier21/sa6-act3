lst1 = [1, 2, 4, 6, 8, 12, 19]
lst2 = [2, 5, 6, 8, 11, 17]

intersect = list(filter(lambda x: x in lst2, lst1))

print(intersect)