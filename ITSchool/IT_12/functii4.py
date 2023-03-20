def zero_one(lst):
    lst[0] = 1

matrix = [
    [0, 3, 4, 4],
    [2, 34, 24, 43],
]

print(matrix)
zero_one(matrix) #pass by reference
print(matrix)
