#add two numbers 
add=lambda a,b:a+b

#subtract two numbers 
subtract=lambda a,b:a-b

#multiply two numbers 
multiply=lambda a,b:a*b

#divide two numbers 
divide=lambda a,b:a/b

#one number raiseToPower another 
raiseToPower=lambda a,b:a**b

if __name__ == "__main__":
    while True:
        print("Please select operation -\n"
                "1. Add\n"
                "2. Subtract\n" 
                "3. Multiply\n"
                "4. Multiply\n"
                "5. Raise to power of\n"
                "6. Quit\n") 


        # Taking input from the user 
        select = input("Select operations form 1, 2, 3, 4, 5 :") 
        if select == '6': 
            print("\n************ Thanks for using the calculator **************\n")
            exit() 

        number_1 = int(input("Enter first number: ")) 
        number_2 = int(input("Enter second number: ")) 

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
        elif select == '5': 
            print(number_1, "^", number_2, "=", 
                            raiseToPower(number_1, number_2))
        else: 
            print("Syntax Error!")  
        print("\n************ Thanks for using the calculator **************\n")
