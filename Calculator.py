# lets build a simple calculator
# 1. add    2. subtract     3. multiply     4. divide   5. exit

def add(x, y):
    return x + y    # return the sum of x and y 

def subtract(x, y):
    return x - y    # return the difference of x and y  

def multiply(x, y):
    return x * y    # return the product of x and y

def divide(x, y):
    return x / y    # return the quotient of x and y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

while True:     # Take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):  # Check if choice is one of the four options
        
        num1 = float(input("Enter first number: ")) # Check if choice is one of the four options
        
        num2 = float(input("Enter second number: ")) # Check if choice is one of the four options
        
        if choice == '1':   # Add two numbers
            print(num1, "+", num2, "=", add(num1, num2)) # Check if choice is one of the four options

        elif choice == '2': # Subtract two numbers
            
            print(num1, "-", num2, "=", subtract(num1, num2)) # Check if choice is one of the four options
            
        elif choice == '3': # Multiply two numbers
            
            print(num1, "*", num2, "=", multiply(num1, num2)) # Check if choice is one of the four options
            
        elif choice == '4': # Divide two numbers
            
            print(num1, "/", num2, "=", divide(num1, num2)) # Check if choice is one of the four options
            
        break # break the loop if choice is 5
    
    else:
        print("Invalid Input") # Check if choice is one of the four options     
        
# End of the program