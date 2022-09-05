n1=input()
n1=int(n1)
n2=input()
n2=int(n2)
l1=[0,0,0,0,0,0,0,0,0,0]
l2=[0,0,0,0,0,0,0,0,0,0]
while n1!=0:
    l1[int(n1%10)]+=1
    n1=n1/10
while n2!=0:
    l2[int(n2%10)]+=1
    n2=n2/10
ok=1
for i in range(9):
    if l1[i]!=0 and l2[i]==0 or l2[i]!=0 and l1[i]==0:
        print('NO')
        ok=0
    if ok==0:
        break
if ok==1:
    print ('YES')

               
    
