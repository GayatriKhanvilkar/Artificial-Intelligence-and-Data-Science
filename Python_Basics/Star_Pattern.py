
# Printing * in Right Triangle Shape
# *
# * *
# * * *
# * * * *
# * * * * *
n = int(input("enter the no. of rows: "))
row = 0
while row<n:
    star = row+1
    while star>0:
        print("*", end=" ")
        star -=1
    row +=1
    print()

# Printing Stars in Pyramid Shape Using while loop
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = int(input("enter the no. of rows: "))
row = 0
while row<n:
    space = n-row-1
    while space>0:
        print(end=" ")
        space -=1
    star = row+1
    while star>0:
        print("*", end=" ")
        star -=1
    row +=1
    print()

# Printing Stars '*' in Reverse Right Triangle Shape
# * * *
#   * *
#     *
num = int(input("Enter the no of rows: "))
for i in range(num, 0, -1):
    for j in range(0, num-i):
        print(" ", end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()

# Printing Stars '*' in Reverse Pyramid Shape
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

num = int(input("Enter the no of rows: "))
for i in range(num, 0, -1):
    for j in range(0, num-i):
        print(" ", end="") # Same code as above but difference in end = " " and end = ""....
    for j in range(0, i):
        print("*", end=" ")
    print()

# Print Heart Shape
for row in range(6):
    for column in range(7):
        if (row == 0 and column % 3 != 0) or (row == 1 and column % 3 == 0) or (row-column == 2) or (row+column == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

