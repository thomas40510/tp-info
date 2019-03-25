import random
def pswd(n):
    a='azertyuiopqsdfghjklmwxcvbn0123456789AZERTYUIOPQSDFGHJKLMWXCVBN'

    pswd = ""
    for i in range(n):
        pswd+=a[random.randint(0,len(a)-1)]
    print(pswd)


for k in range(5):
    pswd(15)
