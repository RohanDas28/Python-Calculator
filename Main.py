"""
This is a simple python calculator.
"""


def add():
    '''adds two numbers'''
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")


def subtract():
    '''subtracts two numbers'''
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")


def multiply():
    '''multiplies two numbers'''
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The product of {num1} and {num2} is {num1 * num2}")


def divide():
    '''divides two numbers'''
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    # to check if divided by zero
    try:
        print(f"The division of {num1} and {num2} results in {num1 / num2}")
    except exception as e:
        print(e)


def exponent():
    '''exponentiates a number'''
    num = eval(input("Enter number to be exponented: "))
    power = eval(input("Enter power to be raised at: "))
    print(f"{num} raised to {power} is {num ** power}")


def sqrt():
    '''sqrt -> square root'''
    num = eval(input("Enter number whose square root you want to know: "))
    print(f"Square root of {num} is {num ** 0.5}")


def cbrt():
    '''cbrt -> cube root'''
    num = eval(input("Enter number whose cube root you want to know: "))
    print(f"Cube root of {num} is {num ** (1/3)}")


def recurse_factor(n):
    # recursive function to find factorial
    if n == 1:
        return n
    else:
        return n * recurse_factor(n - 1)


def fact():
    '''finds factorial of a number'''
    # NOTE- This is recursive and can only calculate till python data bounds
    num = int(input("Enter the number whose factorial you want to find: "))
    if num <= 0:
        print("Factorial doesn't exist for negative numbers" if num < 0 else 'The factorial of 0 is 1')
    else:
        print(f"Factorial of {num} is {recurse_factor(num)}")


def main():
    # Taking input from the user
    try:
        select = int(input("Please select operation -\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Exponentation\n"
            "6. Square Root\n"
            "7. Cube Root\n"
            "8. Factorial\n"
            "9. Quit\n"))
    except Exception as e:
        print(f'{e} Error,\n Invalid Option...')
        main()

    if select == 1:
        add()

    elif select == 2:
        subtract()

    elif select == 3:
        multiply()

    elif select == 4:
        divide()

    elif select == 5:
        exponent()

    elif select == 6:
        sqrt()

    elif select == 7:
        cbrt()

    elif select == 8:
        fact()

    elif select == 9:
        print("Thanks for visiting!")
        quit()

    else:
        print("Invalid input!")
    main()
    print("\n************ Thanks for using the calculator **************\n")


if __name__ == "__main__":
    main()
