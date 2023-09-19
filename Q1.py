s1=input()
s2=input()
a=len(s1)
a1=len(s2)
c=0
for element in s1 :
 for element1 in s2 :
  if element==element1 :
   c=c+1;
if c==a and a==a1 :
    print("same")
else:
    print("different")