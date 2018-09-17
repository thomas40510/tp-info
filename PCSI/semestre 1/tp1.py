
'''
#Ex. 1

name = input('Quel est votre nom ? ')
print ('bonjour', name)
a = int(input('Entrez un nombre entier : '))
b = int(input('Entrez un autre entier : '))

if (a == b):
    print('les deux nombres sont égaux')
elif (a < b):
    print('Le plus grand des deux vaut : ', b)
else :
    print('Le plus grand des deux vaut : ', a)
'''

'''
#Ex. 2

while True:
    a = int(input('Entrez un entier entre 0 et 10 : '))
    if (0<=a<=10):
        break
    else : print('le nombre saisi n\'est pas compris entre 0 et 10 !')
for i in range(1,a+1):
    print(i*'*')
'''

'''
#Ex. 3

while True:
    a = int(input('Entrez un entier entre 0 et 10 : '))
    if (0<=a<=10):
        break
    else : print('le nombre saisi n\'est pas compris entre 0 et 10 !')
for i in range(0,a):
    print((a-i)*'*')
'''

'''
#Ex. 4

while True:
    a = int(input('Entrez un entier entre 0 et 10 : '))
    if (0<=a<=10):
        break
    else : print('le nombre saisi n\'est pas compris entre 0 et 10 !')

for n in range(0,a+1):
    for i in range(1,a+1):
        print(i*'*')
'''

'''
#Ex. 5

yr = int(input('Entrez une année : '))

if ((yr%400) == 0 or ((yr%4) == 0 and (yr%100) != 0)):
    print ('L\'année', yr, 'est bissextile.')
else :
    print('L\'année', yr, 'n\'est pas bissextile')
'''

'''
#Ex. 6

f,g = 1,0
a = int(input('Nombre : '))
n = 0
while (n !=a):
    n = n+1
    h = g
    g = f+g
    f = h
    #print (n, '|', g)

print ('le nombre est :',g)
'''

'''
#Ex. 7
'''
while True:
    a = int(input('Entrez un entier entre 0 et 10 : '))
    if (0<=a<=10):
        break
    else : print('le nombre saisi n\'est pas compris entre 0 et 10 !')

cp = input('Entrez un premier caractère : ')
ci = input('Entrez un second caractère : ')

for i in range (1,a+1):
    if (i%2 == 0):
        for j in range (1,a+1):
            if(j%2 == 0):
                print (cp, end='')
            else :
                print (ci, end='')
        print()
    else:
        for j in range (1,a+1):
            if (j%2 == 0):
                print (ci, end='')
            else:
                print (cp, end='')
        print()
