import math
#Ask the user to make a choice
print("Welcome to the Calculator!")
print("Please choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6.power")
print("7.square")
# Get the user's choice
choice = input("Enter the number of your choice (1-7): ")
def off_on(choice):
    while True:
        if choice in (1,7):
            continue
        elif choice==exit:
             break
def sum(num1,num2):
    return print(f"{num1}+{num2}={num1+num2}")

def subtraction(num1,num2):
    return print(f"{num1}-{num2}={num1-num2}")

def product(num1,num2):
    return print(f"{num1}*{num2}={num1*num2}")

def division(num1,num2):
    return print(f"{num1}/{num2}={num1/num2}")

def modulo(num1,num2):
    return print(f"{num1}%{num2}={num1%num2}")

def power_nbr(num1,num2):
    s = 1
    for i in range(int(num2)):
        s = s * num1
    return print(f"{num1}^{num2}={s}")



    # Get the two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
for i in choice:  
    if choice == '1':
        sum(num1,num2)
        continue
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
       product(num1,num2)
    elif choice == '4':
       division(num1,num2)
    elif choice == '5':
        modulo(num1,num2)
    elif choice == '6':
         power_nbr(num1,num2)
    elif choice =='7':
         print(f"the squareof the number{num1}:{math.sqrt(num1)}")        
    else:
        print("Invalid choice. Please run the program again and select a valid operation.")
