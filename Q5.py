import math

mylist=[]
r=0
k=int(input("enter the length of array:"));
for a in range(k) :
    f=int(input(f"Enter element {a + 1}: "))
    mylist.append(f)
    a=a+1;
for a in range(k) :
    if a%2==0:
        r=r+math.fabs(mylist[a])
    else:
        r=r-math.fabs(mylist[a])
print(f"maximum sum is {r}")
