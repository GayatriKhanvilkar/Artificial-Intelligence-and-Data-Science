# Printing Strings in Right Triangle Shape
# P
# Py
# Pyt
# Pyth
# Pytho
# Python
str = input("Enter the String: ")
l = len(str)

for row in range(l):
    for column in range(row+1):
        print(str[column], end="")
    print()

#Printing Numbers in Pyramid Shape

num = int(input("Enter number of rows: "))

for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(end=" ")
    for j in range(1, 0, -1):
        print(j, end=" ")
    for j in range(2, i+1):
        print(j, end=" ")
    print()

#  Printing Numbers in Right Triangle Shape
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#  Printing Numbers in Right Triangle Shape
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

# Printing Numbers in Right Triangle Shape
# 12345
# 1234
# 123
# 12
# 1
n = int(input("Enter a number of rows: "))
for row in range(n, 0, -1):
    for column in range(1, row+1):
        print(column, end=" ")
    print()

# Printing Numbers in Right Triangle Shape
# 55555
# 4444
# 333
# 22
# 1
n = int(input("Enter a number of rows: "))
for row in range(n, 0, -1):
    for column in range(1, row+1):
        print(row, end=" ")
    print()

# Floyd's Triangle- Printing Numbers in Right Triangle Shape
# 1
# 2 3
# 4 5 6
# 7 8 9 10
n = int(input("Enter a number of rows: "))
num =1
for row in range(1, n+1):
    for column in range(1, row+1):
        print(num, end=" ")
        num += 1
    print()



