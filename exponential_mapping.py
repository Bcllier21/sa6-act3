constant = int(input("Enter value for constant n: "))
num_list = [1, 3, 7, 11, 15]

lmd_raise = lambda x: x**constant
raised = list(map(lmd_raise, num_list))
print(raised)
