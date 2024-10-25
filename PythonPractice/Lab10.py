# def findAndReplace(list, findVal, ReplaceVal):
#     valueFound = False
#     empList = []
#     for i in list:
#         if i == findVal:
#             print("Value is found")
#             i = ReplaceVal
#             valueFound = True
#
#         empList.append(i)
#
#     if valueFound:
#         print("New list is as follows: ")
#         for i in empList:
#             print(i, end=' ')
#
#     else:
#         print("Value not found")

# 1. Write a Python program to sum all the items in a list.

def sumup(list):
    add = 0
    for i in list:
        add += i

    print(add)


# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.
def largeandsmall(list):
    maxVal = float('-inf')
    minVal = float('inf')
    for i in list:
        if maxVal < i:
            maxVal = i
        if minVal > i:
            minVal = i
    print(f"Maximum value is: {maxVal}")
    print(f"Minimum value is: {minVal}")


# 3. Write a Python program to find duplicate values from a list and display those.

def duplicates(list):
    duplicacy = False
    if duplicacy == False:
        for i in range(len(list)):
            count = list[i]
            for j in range(i + 1, len(list)):
                # print(j)
                if count == list[j]:
                    print(f"Duplicate value in the list is {count}")
                    duplicacy = True
    else:
        print("No duplicates")


# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list: [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

def splitList(list, splitVal):
    print("Splitting the list into two parts")
    tempList = []
    i = 0
    while i<splitVal:
        tempList.append(list[i])
        i+=1
    print("List 1")
    for i in tempList:
        print(i ,end=" ")

    print("\nList 2")
    for i in range(splitVal, len(list)):
        print(list[i], end=" ")



# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order: black white green red

def traverse(list):
    for i in reversed(range(0, len(list))):
        print(list[i], "index =", end=" ")
        print(i)


def traverse2(list):
    templist = []
    for i in range(len(list) - 1, -1, -1):
        templist.append(list[i])

    for i in range(len(templist)):
        print(templist[i], end=" ")
        print("index =", len(list) - 1 - i)


# 6. Given the nested list `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, write code to print the second element of the first list and
# the third element of the third list.

def element(arr, row, column):
    x = arr[row-1][column-1]
    return x


# 7. Write a function `transpose(matrix)` that takes a matrix (list of lists) and returns its transpose.
def matrice(matrix):
    print("Given matrix: ")
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def function(matrix):
    print("Transpose of given matrix is: ")
    count = 0
    for i in matrix:
        for j in matrix:
            pass
        count += 1
    for a in range(0, count):
        for b in range(len(matrix)):
            print(matrix[b][a], end=" ")
        print()
    matrice(matrix)



# 8. Given the list `numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]`, write a list comprehension to create a new list containing only the even numbers.

def comprehension(list):
    print("Comprehension list of even numbers: ")
    templist = []
    for i in list:
        if i%2 == 0:
            templist.append(i)
    for i in templist:
        print(i, end=" ")

# 9. Given two lists `a = [1, 2, 3]` and `b = [4, 5, 6]`, write code to merge them into a single list and then flatten a list of lists
#`c = [[1, 2], [3, 4], [5, 6]]` into a single list.

def flatten(matrix):
    print("Flatten list will be: ")
    tempList = []
    for i in matrix:
        for j in i:
            tempList.append(j)
    for i in tempList:
        print(i, end=" ")

def merging(list1, list2, list3):
    print("Merged list: ")
    tempList = []
    for i in list1:
        tempList.append(i)
    for i in list2:
        tempList.append(i)
    for i in tempList:
        print(i, end=" ")
    print("\t")
    flatten(list3)


# 10. Write a function `rotate_list(lst, k)` that rotates a list to the right by `k` positions. For example, `rotate_list([1, 2, 3, 4, 5], 2)`
# should return `[4, 5, 1, 2, 3]`

def rotate_list(lst, k):
    print("After rotation, elements will look like: ")
    for i in range(len(lst)-k, len(lst)):
        print(lst[i], end=" ")
    for i in range(len(lst)-k):
        print(lst[i], end=" ")


if __name__ == '__main__':
    list = [1, 2, "str", 8, 4, 5, 8, 3, "str"]
    list2 = [1, 1, 2, 3, 4, 4, 5, 1, 4]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Original_list = ['red', 'green', 'white', 'black']
    numbers = [15, 3, 7, 20, 13, 9, 25, 1, 10]
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [[1, 2], [3, 4], [5, 6]]
    newList = [1,2,3,4,5,6,7]


    # findAndReplace(list, str, 10)
    # sumup(list)
    # largeandsmall(list)
    # duplicates(list)
    # splitList(list2, 5)
    # traverse(list)
    # traverse2(Original_list)
    # print("________Answer sixth________")
    # print("second element of the first list is ", element(matrix,2,1))  # second element of the first list
    # print("third element of the third list is ", element(matrix,3,3))  # third element of the third list
    # print("\n________Answer seventh________")
    # function(matrix)
    # print("\n________Answer eighth________")
    # comprehension(numbers)
    # print("\n________Answer ninth________")
    # merging(a,b,c)
    # print("\n________Answer tenth________")
    # rotate_list(newList, 3)



















