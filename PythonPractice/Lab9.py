# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

val1 = float(input("Write first number: "))
val2 = float(input("Write second number: "))
try:
    div = val1/val2
    print(f"Division of the given numbers is {div}")
except ZeroDivisionError as var:
    print("ZeroDivisionError: ", var)

# 2. Write a Python program that prompts the user to input an integer and raises(use custom exception to raise this error: it will be raised if
# the value provided is not between 1 and 1000) a ValueError exception if the input is not a valid integer.

from ValueErrorException import ValueError

numb = int(input("Enter number "))
try:
    if numb < 1 or numb > 1000:
        raise ValueError(numb)
    else:
        print(numb, "lies between 1 and 1000")
except ValueError as error:
    print("ValueError: ", error)

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    fileName = input("Write your file path ")
    file = open(fileName, "r")
    if file:
        print("Given file exists")
except FileNotFoundError as error:
    print("FileNotFoundError: ", error)

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

val1 = input("Write your 1st numerical value: ")
val2 = input("Write your 2nd numerical value: ")

i = float(val1)
j = float(val2)
# _____for Value Error______
try:
    if i:
        print(f"{val1} is numeric value")
except ValueError as err:
    print(err, f",so {val1} is not numeric value")
try:
    if j:
        print(f"{val2} is numeric value")
    else:
        raise ValueError
except ValueError as err:
    print(err, f",so {val2} is not numeric value")

# _____for Type Error____

try:
    try:
        val1 = int(val1)
        changesVal1 = 3 + val1
        print("first value is numerical")

    except ValueError:
        raise TypeError("TypeError in first value: \nFirst value is not numerical, recheck first value")

except TypeError as e:
    print(e)

try:
    try:
        val2 = int(val2)
        changesVal2 = 3 + val2
        print("second value is numerical")

    except ValueError:
        raise TypeError("TypeError in second value: \nFirst value is not numerical, recheck second value")

except TypeError as e:
    print(e)

# 5. File Parsing with Detailed Error Handling
# - Write a function `parse_file` that reads a file containing numerical data (one number per line) and returns a list of these numbers.
#   Use exception handling to manage:
# - File not found.
# - Permission denied.
# - Value errors (e.g., non-numeric data).
# - Provide detailed error messages indicating the line number and nature of the error.

def parse_file(fileName):
    tempList = []
    try:
        with open(fileName) as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            try:
                tempList.append(int(line.strip()))
            except ValueError as err:
                print(f"ValueError: {err} on line {i+1}")
    except FileNotFoundError as err1:
        print("FileNotFoundError:", err1, "\nGiven file doesn't exist at the given location")
    except PermissionError as err2:
        print("PermissionError:", err2, "\nPermission denied for file access")
    return tempList


# 6. Multiple Exception Types in User Input
# - Write a function `get_valid_date` that prompts the user to enter a date in the format `YYYY-MM-DD`. Use exception handling to manage:
# - Invalid format (e.g., not enough parts, non-numeric parts).
# - Invalid date values (e.g., month not in 1-12, day not valid for the given month).
# - Ensure the function keeps asking for input until a valid date is entered and returns a `datetime.date` object.

import datetime

def get_valid_date():
    while True:
        try:
            date_input = input("Enter a date (YYYY-MM-DD): ")
            parts = date_input.split('-')
            if len(parts) != 3:
                raise ValueError("Incorrect format. Please use YYYY-MM-DD.")
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            valid_date = datetime.date(year, month, day)
            return valid_date
        except ValueError as err:
            print(f"ValueError: {err}. Please enter a valid date in the format YYYY-MM-DD.")


if __name__ == "__main__":
    fileLocation = input("Write your file location\n")
    print("_______Answer 5_______")
    print(parse_file(fileLocation))
    print("_______Answer 6_______")
    print(get_valid_date())

# 7. Custom Exceptions for Business Logic
# - Create custom exception classes `OutOfStockError` and `InvalidOrderError`. Write a function `process_order` that takes an order (a dictionary with item names and quantities) and a stock (a dictionary with item names and available quantities) as arguments. Use exception handling to manage:
# - Out of stock items (raise `OutOfStockError` with a suitable message).
# - Invalid order quantities (e.g., negative or zero, raise `InvalidOrderError` with a suitable message).
# - Test the function with various orders and stock scenarios.

mydict = {'bottles': 4, 'notebook': 3, 'pencil': 8, 'pens': 6, 'candles': 6}


class OutOfStock(Exception):
    def __init__(self):
        super().__init__("The product is out of stock")


class InvalidOrderError(Exception):
    def __init__(self):
        super().__init__("Not sufficient quantity")


def process_order(names, quant):
    if names not in mydict.keys():
        raise OutOfStock
    if quant > mydict[names]:
        raise InvalidOrderError
    print(f"Order Complete for {names}")

try:
    process_order('pens', 5)
except OutOfStock as so:
    print(so)
except InvalidOrderError as oe:
    print(oe)


# 8. Exception Handling in List Operations
# - Write a function `safe_list_access` that takes a list and an index as arguments and returns the element at that index. Use exception handling to manage:
# - Index out of range.
# - Any other error (provide a generic error message).
# - Test the function with various lists and indices, including valid, negative, and out-of-range indices.

def safe_list_access(lt, indices):
    try:
        if not (-len(lt) <= indices <= len(lt)):
            raise IndexError
        print(lt[indices])

    except IndexError:
        print(f"Error: Index {indices} is out of range for list of length {len(lt)}.")
    except Exception as e:
        print(f"Error: {e}")


lst = [34,45,23,56,"hgb","cud", 65, True]
# indices = lst[14]

safe_list_access(lst, -4)


# 9. Exception Handling with Logging
# - Write a function `read_and_log` that reads a file and logs any exceptions that occur to a separate log file. Use exception handling to manage:
# - File not found.
# - Permission denied.
# - Any other error.
# - Ensure the function writes detailed error messages to the log file and test it with various scenarios.

import logging

logging.basicConfig(filename='result.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_and_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except PermissionError:
        logging.error(f"Permission denied: {file_path}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


read_and_log("bjbjdc.txt")


# 10. Write a function convert_to_float that takes a list of strings and attempts to convert each string to a float. Use exception handling to manage:
# Value errors (e.g., strings that cannot be converted to float).
# Any other unexpected errors.
# The function should return a list of successfully converted floats and a list of errors (with the original string and the error message).

def convert_to_float(li):
    f = []

    for s in li:
        try:
            f.append(float(s))
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
    return f


li = ["hgy", 89, 54, 8, "tyg"]
print(f"Successfully converted to floats - ", convert_to_float(li))















