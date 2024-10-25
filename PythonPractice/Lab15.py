import numpy as np
# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives
print("__________Answer 1__________")
arr1 = np.zeros(10)
arr2 = np.ones(10)
arr3 = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
print("Array of 10 zeros: \n", arr1)
print("Array of 10 ones: \n", arr2)
print("Array of 10 fives: \n", arr3)

# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
print("\n__________Answer 2__________")
arr4 = np.array([[2,3,4], [5,6,7], [8,9,10]])
print(arr4)

# 3. Write a NumPy program to create an array with values ranging from 12 to 38.
print("\n__________Answer 3__________")
arr5 = np.arange(12,38)
print(arr5)

# 4. Write a NumPy program to convert a list and tuple into arrays.
print("\n__________Answer 4__________")
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

arr6 = np.array(my_list)
arr7 = np.array(my_tuple)

print("List to array: \n",arr6)
print("Tuple to array: \n",arr7)
