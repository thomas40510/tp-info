L=[1,0,0,2,3,0,4,5,6,7,8,9]
'''
Ex. 1

def position(n,L):
    posx=[]
    for i in range(0,len(L)):
        if L[i]==n:
            posx+=[i]

    return posx
'''
'''
Ex. 2

def lpair(L):
    allpairs=[]
    for i in L:
        if ispair(i):
            allpairs.append(i)

    return allpairs

def ispair(n):
    return n%2==0

def filterpair(L):
    return list(filter(ispair, L))
'''
'''
Ex. 3

def doublons(L):
    for j in range(0,len(L)):
        for i in range(0,len(L)):
            if L[i]==L[j] and i!=j:
                return True

    return False
'''
'''
Ex. 4

def mvzero(L):
    Z = list(filter(lambda x:x!=0, L))
    Z+=(len(L)-len(Z))*[0]
    return Z

def mvzero2(ls):
    j = len(ls)-1
    while j!=0:
        while i!=j:
            if ls[i]==0:
                ls[i]=ls[j]
                ls[j]=0
                while ls[j]==0:
                    j+=(-1)
            i+=i
    return ls
'''
'''
Ex. 5

def nextline(L):
    line=[1]
    for i in range(len(L)-1):
        line.append((L[i]+L[i+1]))
    line.append(1)
    return line

def trianglePascal(n):
    L=[1]
    for i in range(n):
        print(L)
        L=nextline(L)
'''
'''
Ex. 6
'''
def Eratosthene (n):
    L = n*[True]
    L[0]=False
    L[1]=False
    i=2
    while i<n**(1/2):
        if L[i]:
            for k in range(2*i,n,i):
                L[k]=False
        i+=1
    return indexes(L)

def indexes(L):
    ls=[]
    for i in range(len(L)):
        if L [i]:
            ls.append(i)
    return ls
