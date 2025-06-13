p1 = (input("first player choosing: "))
p2 = (input("second player choosing: "))
if str(p1) == str(p2) :
   print("repeat please!")
elif str(p1) == 'rock'  or  str(p1) == 'scissors' and str(p2) =='paper':
  print("p1 is the winner")
elif str(p2) =='rock' or str(p2) == 'scissors' and str(p1) =='paper':
  print("p2 is the winner")

