def prime(p):
    if p==0 or p==1 or p==2:
        return 0
    if p%2==0:
        return 0
    d=3
    while d*d<=p:
        if p%d==0:
            return 0
        d+=2
    return 1

n=input()
n=int(n)
if n%2!=0:
    if prime(n-2)==1:
        print('2 '+str(n-2))
    else:
        print ('impossible')
else:
    ok=0
    k=3
    while  ok==0:
        if prime(k)==1 and prime(n-k)==1:
            print (str(k)+' '+str(n-k))
            ok=1
        k+=2

            
    
