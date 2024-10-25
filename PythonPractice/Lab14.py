import numpy as np

# Calculating first n prime numbers
# def prime(n):
#     arr = []
#     count = 1
#     i = 1
#     while count <= n:
#         temp = True
#         for j in range(2, int(i / 2) + 1):
#             if i % j == 0:
#                 temp = False
#                 break
#         if temp:
#             arr.append(i)
#             count += 1
#         i += 1
#
#     new_arr = np.array(arr)
#     print(new_arr)
#
#
# if __name__ == "__main__":
#     prime(10)


# 1. Convert the below list into numpy array then display the array
my_list = [1, 2, 3, 4, 5]
print("Numpy array: ")
arr1 = np.array(my_list)
print(arr1)


# 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2
# and display the result.
# index1 = arr1.index(arr1[0])
print("First index is ", arr1[0])
print("Second index is ", arr1[4])
arr2 = arr1*2
print("After applying doubling each element: ")
print(arr2)



















