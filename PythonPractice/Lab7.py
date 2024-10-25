# 1. Write a Python program to Count all letters, digits, and special symbols from the given string
# Output: Chars = 8 Digits = 3 Symbol = 4
inputStr = "P@#yn26at^&i5ve"
scount = 0
dcount = 0
ccount = 0
for i in inputStr:
    if 32 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 90 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
        scount += 1
    elif 48 <= ord(i) <= 57:
        dcount += 1
    elif 65 <= ord(i) <= 90 or 96 < ord(i) <= 122:
        ccount += 1
print("Chars:" ,ccount, "  Digits:" ,dcount, "  Symbol:" ,scount)

# 2. Write a Python program to remove duplicate characters of a given string.
# Output: String and Function
inputStr2 = "String and String Function"
str1 = ""
for ch in inputStr2:
    if ch not in str1:
        str1 += ch
print(str1)

splitted = inputStr2.split()
list = []
for i in splitted:
    list.append(i)
newStr = ""
for ch in splitted:
    if ch not in newStr:
        newStr += ch + " "
print(newStr)

# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
# Output:
# UpperCase : 5
# LowerCase : 18
# NumberCase : 5
# SpecialCase : 11
inputStr3 = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
ucount = 0
lcount = 0
ncount = 0
scount = 0
for i in inputStr3:
    if 32 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 90 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
        scount += 1
    if 48 <= ord(i) <= 57:
        ncount += 1
    if 65 <= ord(i) <= 90:
        ucount += 1
    if 97 <= ord(i) <= 122:
        lcount += 1

print("Upper Case: ", ucount)
print("Lower Case: ", lcount)
print("Number Case: ", ncount)
print("Special Case: ", scount)

# 4. Write a Python Count vowels in a string
# Output: Total vowels are: 8
inputStr4= "Welcome to Python Assignment"
vowels = ["a", "e", "i", "o" ,"u"]
count = 0

for i in inputStr4:
    for j in vowels:
        lLetters = i.lower()
        if lLetters == j:
            count += 1
print("Total vowels are:", count)


