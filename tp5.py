
'''
Ex. 1


file = open("zika.txt","r")

for line in file:
    print(line, end='')

file.close()
'''
'''
Ex. 2

file = open("zika.txt","r")

a = 0
for line in file :
    if (a==7):
        break
    else:
        a+=1

print(line,end="")
file.close()
'''
'''
Ex. 3

file = open("zika.txt", "r")

for line in file:
    print(line, end="")
    if ("ORIGIN" in line):
        break


file.close()
'''
'''
Ex. 4

file = open("zika.txt", "r")
newFile = open("nouveau.txt","w")

for line in file:
    newFile.write(line)
    if ("ORIGIN" in line):
        break
file.close()
newFile.close()
print(open("nouveau.txt","r").read())
'''
'''
Ex. 5
'''
def begin():
    for line in file:
        if ("ORIGIN" in line):
            break
def analyze():
    a = 0
    t = 0
    g = 0
    c = 0
    for line in file:
        a += line.count("a")
        t += line.count("t")
        g += line.count("g")
        c += line.count("c")
    print (a,t,g,c)

def baseCount():
    file = open("zika.txt","r")
    begin()
    analyze()
    file.close()

'''
Ex. 6
'''
file = open("zika.txt","r")
begin()

fileText = file.read()

def isLetter(string):
    newString=""
    for c in string:
        if(c=="a" or c=="t" or c=="g" or c=="c"):
            newString+=c
    return (newString)
isLetter(fileText)
print(isLetter(fileText).count("gattaca"))
