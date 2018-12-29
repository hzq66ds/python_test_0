list = [1, 2, 3, 4, 5, 6]
for x in list:
    print(x, end=";")
print(list[0], list[1])
list[1] = 10
print(list[1])
print(list[4:6])
list = list + list
print(3 in list)
