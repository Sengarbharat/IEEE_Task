import math

mylist=[]
r=0;
k=5
for a in range(k) :
    f=int(input(f"Enter element {a + 1}: "))
    mylist.append(f)
    a=a+1;
a=math.gcd(mylist[0],mylist[1])
for a1 in range(1,5) :
    r=math.gcd(mylist[a1],a)
print(r)