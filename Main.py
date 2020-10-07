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
#Finding aquare
def square(num): 
	return num*num
if __name__ == "__main__":
    while True:
        try:
	        print("Please select operation -\n"
	                "1. Add\n"
	                "2. Subtract\n" 
	                "3. Multiply\n"
	                "4. Divide\n"
	                "5. Square\n"
	                "6. Quit\n") 
	
	
	        # Taking input from the user 
	        select = input("Select operations from 1, 2, 3, 4, 5, 6 :") 
	        if select== '5':
	        	number = int(input("Enter the number: "))
	        	sq=square(number)
	        	print(f"The square of {number} is {sq}")
	        	print("\n************ Thanks for using the calculator **************\n")
	        	continue
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
	         	
	        
	        else: 
	            print("Syntax Error!")  
	        print("\n************ Thanks for using the calculator **************\n")
	        continue
        except ValueError:
	         print("Enter a Integer only.")
	         continue
	        
