password="aroua2626"
for i in range(3):
    p=str(input("enter the password:"))
    if str(p)==str(password):
        print("you're correct:")
        break
    else:
        print("you can repeat 3 times")
        continue
