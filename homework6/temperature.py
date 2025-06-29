temps=[]
while True:
    temp=input("enter the temperature:")
    if temp.lower() =='q':
       break
    else:
     temps.append(temp)
print("the list of temperature:",temps)        
l=len(temps)
print("number of readings",l)
print("the maximum",max(temps))
print("the minimum",min(temps))
