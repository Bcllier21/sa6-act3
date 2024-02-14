to_sort = ["Custom", "Sort", "Order", "Function", "Junction", "Yeah"]

sorter = sorted(to_sort, key = lambda x: (len(x), x[0]))

print(sorter)
