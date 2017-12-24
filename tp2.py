'''
Ex. 1
'''
def table (n,p):
    for i in range(0,p+1):
        print(n,"X",i, " = ", n*i)

'''
Ex. 2
'''
def conversion(h, m, s):
    h = h*3600
    m = m*60
    s = s+m+h
    return s

def hms(s):
    h = 0
    m = 0
    while (s>=3600):
        s = s-3600
        h+=1
    while (s>=60):
        s = s-60
        m+=1

    return h, m, s

def duree(h1,m1,s1,h2,m2,s2):
    return hms(conversion(h2,m2,s2)-conversion(h1,m1,s1))


'''
Ex. 3
'''
def f(n):
    if (n%2==0):
        return int(n/2)
    else :
        return 3*n+1

def syracuse(n):
    print (n, end= " ")
    while (n!=1):
        n = f(n)
        print (n, end= " ")

'''
Ex. 4
'''

def recherche(car, texte):
    for i in(texte):
        if i == car:
            return True
        else :
            return False

def position(car, texte):
    n = 0
    for i in(texte):
        n += 1
        if (i == car):
            return n

def compte(car, texte):
    n = 0
    for i in (texte):
        if (i == car):
            n+=1

    return n

def prefixes(texte):
    n = ''
    for i in(texte):
        n = n+i
        print (n)

def remplace(car, texte, nouveau):
    n = ''
    for i in (texte):
        if (i == car):
            i = nouveau
        n = n+i
    return n
