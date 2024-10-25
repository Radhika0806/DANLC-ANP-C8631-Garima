# 1. Write a Python program to find the number of times 4 appears in the tuple.
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)
# Output: 3
count = 0
for i in tuplex:
    if i == 4:
        count+=1
print(f"4 appears {count} times in the tuple")

# 2.Write a Python program to convert a list to a tuple.
listx = [5, 10, 7, 4, 15, 3]
# Output: (5, 10, 7, 4, 15, 3)
tup = tuple(listx)
print(tup)

# 3. Write a Python program to calculate the sum of the numbers in a given tuple.
sum = 0
tuples_list = [(1, 2), (3, 4), (5, 6)]
for i in tuples_list:
    for j in i:
        sum += j
print(f"Sum of values in the tuples: {sum}")

# 4.Write a python program and iterate the given tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# keys = ["Name", "Employee ID", "Department", "Salary"]

print("Employee Records:")
for i in employee3, employee2, employee1:
    print("Name:", i[0])
    print("Employee ID:", i[1])
    print("Department:", i[2])
    print("Salary: $", i[3])
    print()





