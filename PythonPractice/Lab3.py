# 1.	Wap to check whether a character is alphabet or not.
charValue = input("Write your character: ")
if 65 <= ord(charValue) <= 90 or 97 <= ord(charValue) <= 122:
    print(f"{charValue} is an alphabet")
else:
    print("Given value is not an alphabet")

# 2.	Wap to check whether a number is negative, positive or zero.
num = int(input("Write your number: "))
if num > 0:
    print(f"{num} is positive")
elif num == 0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative")

# 3.    Wap to check login and password.

correctID = 1234
pwd = "password"

id = input("Write your Login id: ")
password = input("Write your password: ")
if id == correctID:
    print(f"{id} id is correct")
    if password == pwd:
        print("Your password is correct")
    else:
        print("Your password is incorrect")
else:
    print("your id is incorrect")


# 4. Wap to check if the user has provided the correct currency note for deposit or not.

note = input("Write the value: ")
if note == (500 or 2000 or 100 or 200 or 50):
    print(f"{note} is Current currency note")
else:
    print(f"{note} is not correct currency note")

# 5.    Wap to check whether a character is alphabet, number or special character.

inputVal = input("Write your character: ")
if 48 <=ord(inputVal) <= 57:
    print("Given value is a number")
elif 65 <= ord(inputVal) <= 90:
    print("Given value is an upper case alphabet")
elif 97 <=ord(inputVal) <= 122:
    print("Given character is a lower case alphabet")
else:
    print("Given value is a special character")

# 6.    Input units of electricity from user and print the bill according to the following criteria
# a    Less than 200 : no bill
# b.    Next 200-300  -   1.2/perunit       100*1
# c.     Next 300-400  -1.5/perunit           100*2
# d.    Next 400-500  - 2.5/perunit          100*3
# e.    Above 500 -   8/per unit

bill = 0
unit = float(input("Enter units of electricity"))
if unit<200:
    print("No bill...Enjoy!")
elif unit<=300:
    bill = (unit - 200) * 1.2
elif unit<=400:
    bill = (100*1.2)+((unit-300)*1.5)
elif unit<=500:
    bill = (100*1.2)+(100*1.5)+(unit-400)*2.5
else:
    bill = (100*1.2)+(100*1.5)+(100*2.5)+(unit-500)*8

print(f"The Electricity bill for {unit} is {bill}")
# 7.    Input amount and print its denomination :-
# a.    2000X
# b.    500 X
# c.     200 X
# d.    100 X
# e.    50 X
# Example :-
# Input Amount = 13450
# 2000X 6=12000
# 500X 2=1000
# 200X2=400
# 50X1=50
# Total 13450

inputVal = int(input("Write the amount: "))
fakeVal = inputVal
if inputVal % 50 == 0:
    if inputVal // 2000 > 0:
        print(f"2000 X {inputVal // 2000} = {(inputVal // 2000) * 2000}")
        inputVal = inputVal%2000

    if inputVal // 500 > 0:
        print(f"500 X {inputVal // 500} = {(inputVal // 500) * 500}")
        inputVal = inputVal%500

    if inputVal // 200 > 0:
        print(f"200 X {inputVal // 200} = {(inputVal // 200) * 200}")
        inputVal = inputVal%200

    if inputVal // 100 > 0:
        print(f"100 X {inputVal // 100} = {(inputVal // 100) * 100}")
        inputVal = inputVal%100

    if inputVal // 50 > 0:
        print(f"50 X {inputVal // 50} = {(inputVal // 50) * 50}")
        inputVal = inputVal%50
else:
    print("Amount should be more than 50")
print("Total amount = ", fakeVal)
# __________________OR_____________________
# amount = int(input("Write your amount: "))
# fakeAmount = amount
# value = [2000, 500, 200, 100, 50]
# for i in range(len(value)):
#     count = fakeAmount // value[i]
#     print(f"{value} X {count} are taken")
#     fakeAmount = fakeAmount % value[i]
#
# print(f"Total amount is {amount}")


# 8.  input bank login and password and check whether it is valid or not
# if login is successful, then give options to user for the following:-
# 1. Change password
# 2. Check Balance
# 3. Deposit Amount
# 4. Withdraw Amount

validID = 1234
validPwd = "abcd"
Balance = 45000

inputID = int(input("Write your id: "))
if inputID == validID:
    inputPwd = str(input("Write your password: "))
    if inputPwd == validPwd:
        print("What you want to do:"
              "\nChange Password"
              "\nCheck Balance"
              "\nDeposit Amount"
              "\nWithdraw Amount")
        choice = input()
        if choice == "Change Password":
            oldPwd = input("Write your old password: \n")
            if oldPwd == validPwd:
                newPwd = input("Write your new password: \n")
                cnfmPwd = input("Rewrite your password for confirmation: \n")
                if newPwd == cnfmPwd:
                    validPwd = newPwd
                print("Your password has been changed")
            else:
                print("Password can't be changed for now, Try again later!")
        elif choice == "Check Balance":
            print(f"Your current balance is {Balance}")
        elif choice == "Deposit Amount":
            depAmount = int(input("How much amount you want to deposit? \n"))
            print(f"Your total balance is {Balance + depAmount}")
        elif choice == "Withdraw Amount":
            withdrawAmount = int(input("How much amount you want to withdraw? \n"))
            print(f"Your total balance is {Balance + withdrawAmount}")
    else:
        print("Wrong Password")
else:
    print("Wrong login ID")

# 9.  write a program to generate the following payslip for an employee
# Enter Basic salary:
# Enter Exp:
# Enter name:
# INTERANAL
# INPUT SALARY AND EXPERIENCE AND NAME
# DA   :    5% OF BS
# TA:    6.5% OF BS
# CCA: 8% OF BS
# HRA: 10% OF BS
# PF: 12.5 % OF BS
# TOTAL SALARY: BS+DA+TA+CCA+HRA+PF+BONUS
#  NetSalary : TOTAL SALARY-PF

BasicSalary = int(input("Write your salary: "))
Experience = float(input("Write your Experience: "))
Name = str(input("What's your name? \n"))

print("__________________________________________________________________________________________________________________")
print("                                                  PAY SLIP")
print("__________________________________________________________________________________________________________________")


DA = 0.05 * BasicSalary
TA = 0.065 * BasicSalary
CCA = 0.08 * BasicSalary
HRA = 0.10 * BasicSalary
PF = 0.125 * BasicSalary
# BONUS:
# EXP>25     BONUS:   25% OF BS
# EXP>20    BONUS:   20 % OF BS
# EXP>15 BONUS: 15 % OF BS
# EXP<15   BONUS   10% OF BS
if Experience > 25:
    Bonus = 0.25*BasicSalary
elif Experience > 20:
    Bonus = 0.20*BasicSalary
elif Experience > 15:
    Bonus = 0.15*BasicSalary
else:
    Bonus = 0.10*BasicSalary

TotalSalary = BasicSalary+DA+TA+CCA+HRA+PF+Bonus
NetSalary = TotalSalary-PF

print(f"Name : {Name}\n")
print(f"Experience : {Experience}\n")
print(f"Salary : {BasicSalary}\n")

print(f"DA : {DA}\n")
print(f"TA : {TA}\n")
print(f"HRA : {HRA}\n")
print(f"PF : {PF}\n")
print(f"Bonus : {Bonus}\n")
print(f"Total Salary : {TotalSalary}\n")
print(f"Net Salary : {NetSalary}")
