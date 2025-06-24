def prime_num(n):
    if n==2 or n==3:
        return print(f"{n} is a prime")
    elif n<=1 or n%2==0:
        return print(f"{n} is not a prime")
    else:
        for i in range(3,n):
         if n%i==0:
            return print(f"{n}is not prime")
         else:
           return print(f"{n}is prime")
        i+=1     
#factorial
n=int(input("enter the number:"))
def fact(n):
   prod=1
   i=1
   while True: 
    if n==1 or n==0:
        return 1
    elif n<0:
        return fact(-n)
    elif n>1:
        while i<=n:
          prod=prod*i
          i+=1
    return prod   
print(f"the fact is:{fact(n)}")
fact_value=fact(n)
def sum_prime(fact_value): 
   total=0
   while fact_value>0:
      digit=fact_value%10
      if  prime_num(digit):
         total=total+(digit)
         fact_value=fact_value/10
      else:
         fact_value=(fact_value)/10
      return total   
print(f"the sum is:{sum_prime(fact_value)}")   
