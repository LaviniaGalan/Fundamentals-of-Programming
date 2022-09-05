
n = int(input("n = "))

def display(x):
    s = ''
    d = {0 : '(', 1:')'}
    for i in range (0, n):
        s = s + d[x[i]]
    print(s)
    print('')
 
def check(k, x):
    cp = 0
    op = 0
    for i in range(0, k+1):
        if x[i] == 0:
            op += 1
        else:
            cp += 1
    return cp <= op and op <= n/2

def bkt_rec(k):

    for p in [0, 1]:
        res[k] = p
        if check(k, res) is True:
            if k == n-1:
                display(res)
            else:
                bkt_rec(k+1)

def next_elem(sol):
    if sol[-1] == 1:
        return None
    return sol[-1]+1

def bkt_it():
    sol = [-1]
    while len(sol) > 0:
        elem = next_elem(sol)
        while elem is not None:
            sol[-1] = elem
            if check(len(sol)-1, sol) is True:
                if len(sol) == n:
                    display(sol)
                else:
                    sol.append(-1)
                    break
            elem = next_elem(sol)
        if elem is None:
            sol = sol[:-1]

res = [-1]*(n+2)
print('recursiv:')
bkt_rec(0)
print('iterativ:')
bkt_it()

