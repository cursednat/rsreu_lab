def Pal(n):
    r=0
    nn=n
    while (n>0):
        k=n%10
        r=r*10+k
        n=n//10
    return r==nn
    
p=int(input())
if Pal(p):
    print("YES")
else:
    print("NO")
