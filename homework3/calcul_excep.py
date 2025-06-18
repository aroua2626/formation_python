import random
option = random.choice(['+', '-', '*', '/'])
print(option)
try:
 a = float(input("enter the first number:"))
 b = float(input("enter the second number:"))
 if option == '+':
    print("the addition",a+b)
 elif option is '-':
    print("the substruction",a-b)
 elif option == '*':
    print("the multiplication",a*b)
 elif option is '/':
     print("the division",a/b)
except Exception as ZeroDivisionError: #exept zerodivisionerror:
 print("the division error")
