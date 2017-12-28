import random as rd

alpha='azertyuiopqsdfghjklmwxcvbn'

def shakespeare(n,t):
    t=''
    l=[]
    for i in range(n):
        c = rd.randrange(26)
        l.append(alpha[c])
    return(t.join(l))
    #return (l.count(t))

print(shakespeare(1000000).count("hello"))
