
# 1. Wap to check whether a number is negative or positive.
number = int(input("Write your number: "))
print("Number is Positive") if number>0 else print("Number is negative")

# ______________________________________________________________________________________________________________________
# 2. Wap to check whether a character is in lower case or upper case.
# A-Z    :     65 to 90
# a-z   :       97 to 122
character = input("Write your character: ")
# print("Given character is Upper Case") if character.isupper() else print("Given character is Lower Case")
print("Given character is Upper Case") if 65 <= ord(character) <= 90 else print("Given character is Lower Case") if 97 <=ord(character) <= 122 else print("Give another ascii code")

# ______________________________________________________________________________________________________________________
# 3. Wap to check whether a year is leap or not.
year = int(input("Write your year: "))
print(year , " is leap year") if (year%4 == 0 | year%100 == 0) else print(year, " is not a leap year")

# ______________________________________________________________________________________________________________________
# 4. Wap to check whether a character is alphabet or not
alphabet = input("Write your value: ")
print("Given value is an alphabet") if 65 <= ord(alphabet) <= 90 else print("Given character is an alphabet") if 97 <=ord(alphabet) <= 122 else print("Given value is not an alphabet")

# ______________________________________________________________________________________________________________________
# 5. Wap to check a character and print whether it is an alphabet, number or Special character.
# Number 0- 9  : 48 to 57
inputVal = input("Write your character: ")
print("Given value is a number") if 48 <=ord(inputVal) <= 57 else print("Given value is an upper case alphabet") if 65 <= ord(inputVal) <= 90 else print("Given character is a lower case alphabet") if 97 <=ord(inputVal) <= 122 else print("Given value is a special character")

# ______________________________________________________________________________________________________________________
# 6. wap to calculate the salary slip
#                               Basic  salary : input from user  // salary=60000
#                               Da     :    2% of basic   // da=0.02*salary
#                               Ta      :   3% of salary
#                Hra  :      10% salary
#                PF     :    15% of salary
#                Total salary=    basic+da+ta+hra+pf;’
#                Net salary =   total-pf;
# Calculate bonus of employee to 25 % of salary by shift operators.

Basicsalary = float(input("Write your salary: "))
da = 0.02 * Basicsalary
ta = 0.03 * Basicsalary
hra = 0.010 * Basicsalary
pf = 0.15 * Basicsalary
Totalsalary = Basicsalary+da+ta+hra+pf
Netsalary = Totalsalary-pf

Bonus = int(Basicsalary * 25) >> 2

print("Salary Slip")
print("Basic Salary: ", Basicsalary)
print("DA (2%): ",da)
print("TA (3%): ", ta)
print("HRA (10%): ", hra)
print("PF (15%): ", pf)
print("Total Salary: ", Totalsalary)
print("Net Salary: ",Netsalary)
print("Bonus (25%): ",Bonus)
