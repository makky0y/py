# Find the number of slot i.e. |(Zm)*|/|<p>|
#!/usr/bin/python
from fractions import gcd

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def genZmStar(m):
    zmStar=[]
    for a in range(1,m):
      if gcd(a,m) == 1:
        zmStar.append(a)
    return zmStar,len(zmStar)
    

def cyclic_g(p,m,cg_p,zmStar):
    cg_p=[]
    cg_p.append(1)
    for a in range(1,m):
      b=(p**a)%m
      if b==1:
         break
      cg_p.append(b) 
    return len(cg_p);


for p in range(1,5):
    if is_prime(p):
      print(p)
      cg_p=[]
      for m in range(4096,33456):
        zmStar,msize=genZmStar(m)
        #msize=len(zmStar)
        if not gcd(m,p) == 1:
          continue
        order=cyclic_g(p,m,cg_p,zmStar)
        if msize/order >= 500:
            print(" p:" +str(p)+" m:"+str(m)+" <p>ord="+str(order)+" |(Zm*)|="+str(msize)+" #slot="+str(msize/order))
