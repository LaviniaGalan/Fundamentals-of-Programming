def display():
    s = ''
    for i in list_of_elem:
        if i == 0:
            break
        s = s+str(i)+'+'
    print(s)

def prime(p):
    if p==0 or p==1:
        return 0
    if p == 2:
        return 1
    if p%2==0:
        return 0
    d = 3
    while d*d<=p:
        if p%d==0:
            return 0
        d+=2
    return 1

def check(k):    
    return prime(list_of_elem[k]) == 1 and sum(list_of_elem)!=n-1

def bkt(counter):
    for number in range(2, n):
        list_of_elem[counter] = number
        if check(counter)==True:
            if sum(list_of_elem) == n:
                display()
            else:
                bkt(counter+1)

n = int(input('n = '))
list_of_elem = [0]*100
bkt(0)