import random
def pswd(n):
    a='azertyuiopqsdfghjklmwxcvbn0123456789'

    pswd = ""
    for i in range(n):
        pswd+=a[random.randint(0,len(a))]
    return pswd

print(pswd(8))
