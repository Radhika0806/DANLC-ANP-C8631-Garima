# 1. Write a Python program to count the occurrences of each word in a given sentence
string1 = "To change the overall look of your document. To change the look available in the gallery"
strings = string1.split()
word = input(
    "write your word to find in the text: To change the overall look of your document. To change the look available in the gallery: ")
count = 0
print(strings)
for i in strings:
    if word == i:
        count += 1
print(f"Occurrence of '{word}' is {count} times")

# 2. Write a Python program to remove a newline in Python
string2 = "\nBest \nDeeptech \nPython \nTraining\n"
stringo = string2.split()
for i in stringo:
    print(i, end=" ")

# 3. Write a Python program to reverse words in a string
string3 = "Deeptech Python Training"
print(string3[::-1])

stringss = string3.split()
for i in stringss:
    print(i[::-1], end=" ")

# 4. Write a Python program to count and display the vowels of a given text
string4 = "Welcome to python Training"
vowels = ["a", "e", "i", "o", "u"]
count = 0
for i in vowels:
    for j in string4:
        if i == j:
            count += 1
            print(j)
print(f"Number of vowels are : {count}")
