# Write a program that takes input of 2 values and adds them.
# The program should only accept numbers and floats only or
# otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    try:
    
        value1 = float(input("Enter the first number: "))
        value2 = float(input("Enter the second number: "))
    
        result = value1 + value2
        print(f"The result of {value1} + {value2} is: {result}")
        break  
    except ValueError:
        print("Invalid character entered. Please enter numbers or floats only.")
