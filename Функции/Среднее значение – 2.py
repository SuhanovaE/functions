def average(values):
    lenval = len(values)
    if lenval == 0:
        return 0
    else:
        return sum(values) / lenval


print(average([1, 5, 500, 10]))
print(average([1, 2, 3, 4, 5]))
print(average([-5, 2]))
