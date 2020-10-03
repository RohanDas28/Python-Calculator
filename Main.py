#add two numbers 
def add(num1, num2): 
	return num1 + num2 

#subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

#multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

#divide two numbers 
def divide(num1, num2): 
	return num1 / num2 
if __name__ == "__main__":
    while True:
        print("Please select operation -\n"
                "1. Add\n"
                "2. Subtract\n" 
                "3. Multiply\n"
                "4. Multiply\n"
                "5. Quit\n") 


        # Taking input from the user 
        select = input("Select operations form 1, 2, 3, 4, 5 :") 
        if select == '5': 
            print("\n************ Thanks for using the calculator **************\n")
            exit() 

        try:
            number_1 = int(input("Enter first number: "))
        except ValueError:
            print('First number is not number')
            continue
        try:
            number_2 = int(input("Enter second number: "))
        except ValueError:
            print('Second number is not number')
            continue

        if select == '1': 
            print(number_1, "+", number_2, "=", 
                            add(number_1, number_2)) 

        elif select == '2': 
            print(number_1, "-", number_2, "=", 
                            subtract(number_1, number_2))  

        elif select == '3': 
            print(number_1, "*", number_2, "=", 
                            multiply(number_1, number_2))  

        elif select == '4': 
            print(number_1, "/", number_2, "=", 
                            divide(number_1, number_2))  
        
        else: 
            print("Syntax Error!")  
        print("\n************ Thanks for using the calculator **************\n")
