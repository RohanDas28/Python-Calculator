# add two numbers
def add():
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")


# subtract two numbers
def subtract():
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")


# multiply two numbers
def multiply():
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The product of {num1} and {num2} is {num1 * num2}")


# divide two numbers
def divide():
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))
    print(f"The division of {num1} and {num2} results in {num1 / num2}")


def exponent():
    num = eval(input("Enter number to be exponented: "))
    power = eval(input("Enter power to be raised at: "))
    print(f"{num} raised to {power} is {num ** power}")


def sqrt():  # sqrt -> square root
    num = eval(input("Enter number whose square root you want to know: "))
    print(f"Square root of {num} is {num ** 0.5}")


def cbrt():  # cbrt -> cube root
    num = eval(input("Enter number whose cube root you want to know: "))
    print(f"Cube root of {num} is {num ** (1/3)}


if __name__ == "__main__":
    while True:
        # Taking input from the user
        select = int(input("Please select operation -\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Exponentation\n"
            "6. Square Root\n"
            "7. Cube Root\n"
            "8. Quit\n"))

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
            print("Thanks for visiting!")
            quit()

        else:
            print("Invalid input!")

        print("\n************ Thanks for using the calculator **************\n")
