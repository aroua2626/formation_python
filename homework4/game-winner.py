first=0
second=0
for i in range(3):
 print("Options are: Rock, Paper, Scissors")

 p1 = input("Player 1, enter your choice: ").strip().lower()
 p2 = input("Player 2, enter your choice: ").strip().lower()


 if p1 == p2:
    print("It's a tie!")

 elif (p1 == "rock" )or\
     (p1 == "scissors" and p2 == "paper"):
    print("Player 1 wins!")
    first+=1

 elif (p2 == "rock" )or \
     (p2 == "scissors" and p1 == "paper"):
    print("Player 2 wins!")
    second+=1

 else:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
if first>second:
   print("p1 is the winner")
else:
    print("p2 is the winner")   
