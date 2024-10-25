# Q1 :  wap to print the following pattern(min 10 elements)
# A      1 8 27 64 125 --------
inputNum = int(input("Till where you want to print cubic numbers "))
for i in range(1, inputNum + 1):
    i = i*i*i
    print(i)

# Q2 : wap to find the sum of first 10 natural numbers.

sum = 0
for i in range(1,11):
    sum = sum + i
print("Sum of first 10 natural numbers is: ", sum)

# Q3. Wap to input 10 numbers from user and find their sum and average.

print("Write 10 numbers to be calculated: ")
sum = 0
avg = 0
for i in range(1,11):
    num = int(input())
    sum = sum+ num
avg = sum/10
print("Sum of the given numbers will be: ", sum)
print("Average of given numbers will be:", avg)

# Q4. Wap to print the factorial of a number.
# N=6  fact= 6*5*4*3*2*1

inputNum = int(input("Type the number for which you want to calculate factorial "))
fact = 1
for i in range(1, inputNum + 1):
    fact = fact * i

print(f"Factorial of {inputNum} is {fact}")

# Q5. Wap to print the sum of the series
# 1 4 9 16 25 36 49 64

arr = [1, 4, 9, 16, 25, 36, 49, 64]
sum = 0
for i in arr:
    sum += i
print(f"Sum of the series will be {sum}")

# Q6. Wap to find the binary number of the given integer.
# 1.      Input a number
# 2.      Find the modulus of this number by 2 and save it into an array
# 3.      After the loop is finished, print the array in reverse.
import math
inputNum = int(input("Write a number to calculate its binary value: "))
fakeNum = inputNum
arr = []
while fakeNum != 0:
    val = fakeNum%2
    arr.append(val)
    fakeNum //= 2
print(arr[::-1])

# Q7. Wap to print all the lower case alphabets.
print("Lower case alphabets are written below: ")
for i in range(97,123):
    print(chr(i), end="  ")

# Q8. Wap to input 10 numbers from user and find the minimum and maximum number.
print("Write 10 numbers to find min and max values among them: ")
arr = []
for i in range(1, 11):
    inputNum = float(input())
    arr.append(inputNum)
max = max(arr)
min = min(arr)
print(f"Maximum number is {max}")
print(f"Minimum number is {min}")

# Q9. Wap to print all the leap years from 1 to n.
lastYear = int(input("Write the year number till which you want to print leap years: "))
for i in range(1, lastYear+1):
    if i % 100 == 0 or i % 4 == 0:
        print(i)

# Q10. Wap to read age of 15 people and find the number of adults, babies and school age students.

print("Write ages of 15 people for classification them into babies, adults and school students")
arr = []
for i in range(15):
    age = int(input())
    arr.append(age)
baby = []
school = []
adult = []
invalid = []
for i in arr:
    print(i)
    if i <= 4:
        # print(f"people with age {i} is baby")
        baby.append(i)
    if 4 < i <= 18:
        # print(f"people with age {i} is school age student")
        school.append(i)
    if 85 >= i >= 19:
        # print(f"people with age {i} is adult")
        adult.append(i)
    if i > 85:
        print(f"{i} is an invalid age, write age from 0 to 85")
        invalid.append(i)
print(f"Number of babies are {len(baby)}")
print(f"Number of school age students are {len(school)}")
print(f"Number of adults are {len(adult)}")
print(f"Number of invalid ages are {len(invalid)}")
