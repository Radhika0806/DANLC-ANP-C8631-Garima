# # Q1. Wap to print first 10 prime numbers
count = 0
num = 3
while count <= 10:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1

# Q2. Wap to print all the Armstrong numbers between a given range.
import math
svalue = int(input("Write your first value: "))
lvalue = int(input("Write your end value: "))
arr = [*range(svalue,lvalue+1)]
count = 0
for i in arr:
    arr2 = []
    inputVal = str(i)
    for j in inputVal:
        arr2.append(int(j))
    sum = 0
    for j in arr2:
        sum += int(math.pow(j,3))
    if sum == i:
        count+=1
if count == 0:
    print("No Armstrong number belongs to your given range")

# Q3. Wap to print multiplication tables from a given range.
start = int(input("From which value you want to start printing tables? "))
end = int(input("Write your last value: " ))
while start <= end:
    for i in range(1, 11):
        print(i*start, end = " ")
    print()
    start += 1

# Q4. Patterns
# 1. 1st pattern
inputVal = int(input("Write your value: "))
for i in range(1,inputVal+1):
    for j in range(0,i):
        print(i, end = " ")
    print()


# 2. 2nd pattern (Half-pyramid)
for i in range(1, inputVal+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()

# 3. 3rd pattern
count = 1
for i in range(1, inputVal+1):
    for j in range(1, i+1):
        print(count, end = " ")
        count += 1
    print()

# 4. 4th pattern
for i in range(1, inputVal+1):
    for j in reversed(range(1, i+1)):
        print(j, end = " ")
    print()

# 5. 5th pattern
for i in range(1, inputVal+1):
    x = inputVal-i
    print(" "*x, end="")
    for j in range(1, i + 1):
        print(j, end = "")
    x -= 1
    print()
# Different pattern
print("Different pattern")
for i in range(1, inputVal+1):
    for j in reversed(range(0, inputVal-i)):
        print(""*j,end = " ")
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

# 6th pattern
for i in range(0, inputVal):
    for j in reversed(range(1, inputVal-i+1)):
        print(j, end=" ")
    print()

# 7th pattern
for i in range(1, inputVal+1):
    print(" "*i, end = "")
    for j in range(0, inputVal-i+1):
        print(j+1, end="")
    print()

# 8th pattern
for i in range(1, inputVal+1):
    print("  "*(inputVal-i), end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in reversed(range(1, i)):
        print(j, end=" ")
    print()
for i in range(1, inputVal+1):
    print("  "*(i), end=" ")
    for j in range(1, inputVal-i+1):
        print(j, end=" ")
    for j in reversed(range(1, inputVal-i)):
        print(j, end=" ")
    print()

# 9th pattern
for i in range(1, inputVal+1):
    print("  "*(inputVal-i), end=" ")
    for j in reversed(range(inputVal-i+1, inputVal+1)):
        print(j, end=" ")
    for j in range(inputVal-i+2 , inputVal+1):
        print(j, end=" ")
    print()
for i in range(1, inputVal+1):
    print("  "*(i), end=" ")
    for j in reversed(range(i+1, inputVal+1)):
        print(j, end=" ")
    for j in range(i+2, inputVal+1):
        print(j, end=" ")
    print()

# 10th pattern
for i in range(1, inputVal+1):
    for j in reversed(range(1, i+1)):
        print(j, end=" ")
    print()

# 11th pattern
for i in range(1, inputVal+1):
    for j in range(inputVal-i+1, inputVal+1):
        print(j, end=" ")
    print()

# 12th pattern
for i in range(1, inputVal+1):
    for j in range(i, inputVal+1):
        print(j, end=" ")
    print()

# 13th pattern
for i in range(1, inputVal+1):
    print("  "*(i-1), end=" ")
    for j in reversed(range(i, inputVal+1)):
        print(j, end=" ")
    print()

# 14th pattern (Inverted Half pyramid)
for i in range(0, inputVal):
    for j in range(1, inputVal-i+1):
        print(j, end=" ")
    print()

# 15th pattern (Hollow Half Pyramid)
for i in range(1, inputVal+1):
    for j in range(1, inputVal+1):
        if j == 1:
            print(j, end=" ")
        elif j == i:
            print(j, end=" ")
        elif i == inputVal and 0 < j < inputVal:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

# 16th pattern (Full pyramid)
for i in range(1, inputVal+1):
    for j in range(inputVal - i):
        print(" ", end="")
    for j in range(i, 2 * i):
        print(j, end="")
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end="")

    print()

# 17th pattern (Hollow full pyramid)
for i in range(1, inputVal+1):
    print(" "*(inputVal-i), end="")
    for j in range(1, i+1):
        if j == 1 or i == j or i == inputVal:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    print()

# 18th pattern (Hollow inverted half pattern)
for i in range(1, inputVal+1):
    for j in range(1, inputVal+1):
        if i == 1:
            print(j, end=" ")
        elif j == 1:
            print(i, end=" ")
        elif j == inputVal - i + 1:
            print(inputVal, end=" ")
        else:
            print(" ", end=" ")
    print()

# ABC pattern
for i in range(1, inputVal+1):
    character = inputVal + 64
    if 65 <= character <= 90:
        print(" "*(inputVal-i), end="")
        for j in range(1, i+1):
            print(chr(j+64), end="")
        for j in reversed(range(1, i)):
            print(chr(j+64), end="")
        print()











