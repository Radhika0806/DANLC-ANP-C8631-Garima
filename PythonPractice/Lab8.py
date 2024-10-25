# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
file = open("C:\\Users\\hp\\Desktop\\Conditional Formatting[1].txt", "r")
lines = file.readlines()
for i in lines:
    print(i.strip())
file.close()

# 2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
files = open("C:\\Users\\hp\\Desktop\\New Text Document.txt", "r")
count = 0
content = files.read()
# Splitting the words: wordList = files.read().split()
for i in content:
    # print(i)
    if ord(i) == 32:
        count += 1
print(count)
files.close()

# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”
files = open("C:\\Users\\hp\\Desktop\\New Text Document.txt", "r")
count = 0
content = files.read()
# _______Method 1______
for i in content:
    # print(i)
    if 65 <= ord(i) <= 90:
        count += 1
print(count)


# 4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
def display_words():
    filename = input("Write your text file location: ")
    with open(filename, "r") as filee:
        wordList = filee.read().split()
        count = 0
        for i in wordList:
            if len(i) < 4:
                print(i)
                count += 1
        return count


if __name__ == '__main__':
    print(display_words())

# 5. wap to copy the contents of one file into another. input both file names with path from user

with open("C:\\Users\\hp\\Desktop\\New Text Document.txt", "r") as file5:
    content = file5.read()
with open("C:\\Users\\hp\\Desktop\\New Text Document2.txt", "w") as files5:
    files5.write(content)
with open("C:\\Users\\hp\\Desktop\\New Text Document2.txt", "r") as files5:
    for i in files5:
        print(i)

# 6. Wap to search a particular word in a file and also prints number of occurrences.

with open("C:\\Users\\hp\\Desktop\\New Text Document.txt", "r") as file6:
    word = input("What word you want to find: ")
    count = 0
    wordList = file6.read().split()
    for i in wordList:
        find = i.lower()
        if find == word:
            count += 1
    print(count)

# 7. Wap to search a string and replace it with another string (all occurrences)

file_path = "C:\\Users\\hp\\PycharmProjects\\pythonProject1\\textFile.txt"

with open(file_path, "r") as file7:
    lines = file7.readlines()

search_str = input("Write your string to be replaced: ")
replace_str = input("What you want to replace with: ")

modified_lines = []

for line in lines:
    modified_line = line.replace(search_str, replace_str)
    modified_lines.append(modified_line)

with open(file_path, "w") as file7:
    for line in modified_lines:
        file7.write(line)
with open(file_path, "r") as file7:
    for line in file7:
        print(line, end="")
