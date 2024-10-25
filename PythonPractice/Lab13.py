# 1. Write a Python program to Get Only unique items from two sets.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
# Output: {70, 40, 10, 50, 20, 60, 30}
print("_________Answer 1__________")
newSet = {}
newSet = set1.union(set2)
print(newSet)

# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.
seta = {10, 20, 30, 40, 50}
setb = {30, 40, 50, 60, 70}
# Output: {20, 70, 10, 60}
print("\n_________Answer 2__________")
newSet2 = {}
newset3 = {}
newSet2 = seta.union(setb) - seta.intersection(setb)
newSet3 = seta^setb
print("____Method 1____", newSet3)
print("____Method 2____", newSet2)

# 3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements.
setA = {10, 20, 30, 40, 50}
setB = {60, 70, 80, 90, 10}
# Output: {10}
print("\n_________Answer 3__________")
newSet4 = {}
newSet4 = setA.intersection(setB)
print(newSet4)

# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
sety = {10, 20, 30, 40, 50}
setz = {30, 40, 50, 60, 70}
# Output: {40, 50, 30}
print("\n_________Answer 4__________")
sety = setz.intersection(sety)
print(sety)


