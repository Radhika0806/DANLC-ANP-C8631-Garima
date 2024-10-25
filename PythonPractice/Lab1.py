# Ques 1. Write a program to Input two numbers and Print their addition, subtraction, multiplication ,division and modulus.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# addition
print(a+b)

# subtraction
print(a-b)

# multiplication
print(a*b)

# division
print(a/b)

# modulus
print(a%b)

# Ques 2.Write a program to input length and breath of a rectangle and print its Area?
length = int(input("Write length: "))
breadth = int(input("Write breadth: "))
Area = print(length*breadth)

#Ques 3. Write a program to input total marks of a student and print students' percentage.
engMarks = float(input("English marks out of 100 are: "))
hinMarks = float(input("Hindi marks out of 100 are: "))
mathMarks = float(input("Math marks out of 100 are: "))
totalMarks = engMarks + hinMarks + mathMarks
print("TotalMArks are: " , totalMarks)
percentageOfMarks = (totalMarks/300)*100
print("Percentage of Total MArks will be: ", percentageOfMarks)

# Ques 4. Write a program to input basic salary of an employee and print bonus(10% of Basic salary).
salary = float(input("Write your salary: "))
bonus = 0.10 * salary
print("Bonus will be: ", bonus)
