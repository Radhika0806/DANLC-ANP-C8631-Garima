import statistics
# 1. Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
# Output: 6.2
print("__________Answer 1__________")
sum = 0
count = 0
for i in test_dict.values():
    sum += i
    count += 1

Mean = statistics.mean(test_dict.values())
print("Mean of values is: ", sum/count)
print("Calculated by using built-in mean method: ", Mean)

# 2.Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("__________Answer 2__________")
newDict = {}
newDict.update(dic1)
newDict.update(dic2)
newDict.update(dic3)
for key, value in newDict.items():
    print(f"{key}",":", f"{value}", end= "   ")
print("\n")

# 3.Write a Python program to get the key, value and item in a dictionary.
print("__________Answer 3__________")
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("Key", end=" ")
print("Value")
for key, value in dict_num.items():
    print(f"{key}","  ", f"{value}")

# 4.Write a Python program to get the key, value and item in a dictionary.
input_dict = {1: 10, 2: 20, 3:None, 4: 40, 5: None, 6: 60}

print("__________Answer 4__________")
print("Key", end=" ")
print("Value")
for key, value in input_dict.items():
    if value is not None:
        print(f"{key}","  ", f"{value}")

