# Check generator in (Z/mZ)* and its order 
#!/usr/bin/python
from fractions import gcd

isSort=1
m=257
zmStar=[]

# (Z/mZ)*
for a in range(1,m):
    if(gcd(a,m)==1):
        zmStar.append(a)
print("** multiplicative group (Z/"+str(m)+"Z)*   **")
print("  (Z/"+str(m)+"/Z)*=",end="")
print(zmStar)
print(str(len(zmStar)))


order=[]
cg_3=[]
a=3
cg_3.append(1)
for e in range(1,m):
    b=(a**e)%m
    if b == 1:
        order.append(e)
        break;
    cg_3.append(b)

idx=0
numSlot=16
for a in cg_3:
    if(idx==numSlot-1):
        print(str(a)+",")
    else:
        print(str(a)+",",end="")
    idx=(idx+1)%numSlot
