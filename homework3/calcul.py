a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
import random
option = random.choice(['+', '-', '*', '/'])
print(option)
if option == '+':
    print("the addition",a+b)
elif option is '-':
    print("the substruction",a-b)
elif option == '*':
    print("the multiplication",a*b)
elif option is '/':
    if b!=0:
     print("the division",a/b)
    else:
     print("error:zerodivision") 
    
