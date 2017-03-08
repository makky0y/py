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
for a in zmStar:
    for e in range(1,m):
        b=(a**e)%m
        if b == 1:
            order.append(e)
            break;
print(order)
if not 16 in order:
    print("SUCK")
