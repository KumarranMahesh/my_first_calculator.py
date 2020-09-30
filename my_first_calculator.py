# my_first_calculator.py by AceLewis
# TODO: Make it work for all numbers
if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

reply = input("Do you want to enter the digital calculator (Press y for yes and n for no) : ")

while reply == "y":

    print('Add, subtract, multiply or divide any numbers')
    num1 = int(input('Please enter the first number : '))
    sign = input('What do you want to do? +, -, /, *, **, //(Quotient) or %(Remainder) : ')
    num2 = int(input('Please enter the second number : '))

    if sign == "+":
        print(f"Sum of the two numbers is {num1 + num2}")
    elif sign == "-":
        print(f"Difference between the two numbers is {num1 - num2}")
    elif sign == "/":
        print(f"Division of the two numbers is {num1 / num2}")
    elif sign == "*":
        print(f"Multiplication of the two numbers is {num1 * num2}")
    elif sign == "**":
        print(f"The answer of the exponent is {num1 ** num2}")
    elif sign == "//":
        print(f"Quotient of the two numbers' division is {num1 // num2}")
    elif sign == "%":
        print(f"Remaider of the two numbers' division is {num1 % num2}")
    else:
        print("Please enter a valid input")
    reply = input("Do you want to use the digital calculator again (Press y for yes and n for no) : ")
    continue
