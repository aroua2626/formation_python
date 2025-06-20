password= 2828
for i in range(3):
    p=int(input("enter the password:"))
    if int(p)==int(password):
        print("you're correct:")
        break
    else:
        print("you can repeat 3 times")
        continue
