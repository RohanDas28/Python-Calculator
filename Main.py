"""
This is a simple python calculator.
"""


def add():
    '''adds two numbers'''
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")


def subtract():
    '''subtracts two numbers'''
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")


def multiply():
    '''multiplies two numbers'''
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"The product of {num1} and {num2} is {num1 * num2}")


def divide():
    '''divides two numbers'''
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    # to check if divided by zero
    try:
        print(f"The division of {num1} and {num2} results in {num1 / num2}")
    except ZeroDivisionError as e:
        print(e)


def exponent():
    '''exponentiates a number'''
    num = int(input("Enter number to be exponented: "))
    power = int(input("Enter power to be raised at: "))
    print(f"{num} raised to {power} is {num ** power}")


def sqrt():
    '''sqrt -> square root'''
    num = int(input("Enter number whose square root you want to know: "))
    print(f"Square root of {num} is {num ** 0.5}")


def cbrt():
    '''cbrt -> cube root'''
    num = int(input("Enter number whose cube root you want to know: "))
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


def NTW(n=-1):
    if(n==-1):
        n = int(input("Enter the number whose conversion you want to find: "))
    units = ["", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen" ]
    tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if (n < 20):
        return units[n]
    if (n < 100):
        return tens[n//10]+(" " if (n % 10 != 0) else "")+units[n % 10]
    if (n < 1000):
        return units[n//100]+" Hundred"+(" " if (n%100!= 0) else "")+NTW(n % 100)
    if (n < 100000):
        return NTW(n//1000) +" Thousand"+(" " if (n % 10000 != 0) else "")+NTW(n % 1000)
    if (n < 10000000):
        return NTW(n//100000)+" Lakh"+(" " if (n % 100000 != 0) else "")+NTW(n % 100000)
    return NTW(n//10000000)+" Crore"+(" " if (n % 10000000 != 0) else "")+NTW(n % 10000000)



def main():
    while True:
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
                "9. Number To Words\n"
                "10. Quit\n"))
        except ValueError as e:
            print(f'{e} Error,\n Invalid Option...')
            continue

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
            print("\n",NTW(),"\n\n\n")


        elif select == 10:
            print("Thanks for visiting!")
            break

        else:
            print("Invalid input!")

    print("\n************ Thanks for using the calculator **************\n")


if __name__ == "__main__":
    main()
