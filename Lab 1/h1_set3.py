def sumDiv(p):
    sum=1
    d=2
    while d*d<p:
        if p%d==0:
            sum+=d
            sum+=p/d
        d+=1
    if d*d==p:
        sum+=d
    return sum
n=input()
n=int(n)
n=n-1
ok=1
while n>2 and ok==1:
    if sumDiv(n)==n:
        print (n)
        ok=0
    n=n-1
if ok==1:
    print ('impossible')
    
