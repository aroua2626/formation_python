def even(x):
    if x%2==0:
        return True
    else:
        return False
list_even=[]
nums=[1,2,3,4,5,6,7,8,9]
l=len(nums)
for i in range(l):
 x=nums.pop(0)
 if even(x):
    list_even.append(x)
print(list_even)
