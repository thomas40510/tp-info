def drawhm(n):
    if n==2:
        print (" _________     ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
    if n==1:
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
        print ("|              ")
    else :
        if n==3:
            print (" _________     ")
            print ("|         |    ")
            print ("|         0    ")
            print ("|              ")
            print ("|              ")
            print ("|              ")
            print ("|              ")
        if n==4 :
            print (" _________     ")
            print ("|         |    ")
            print ("|         0    ")
            print ("|         |    ")
            print ("|              ")
            print ("|              ")
            print ("|              ")
        if n==5:
            print (" _________     ")
            print ("|         |    ")
            print ("|         0    ")
            print ("|        /|\\  ")
            print ("|              ")
            print ("|              ")
            print ("|              ")
        if n==6:
            print (" _________     ")
            print ("|         |    ")
            print ("|         0    ")
            print ("|        /|\\  ")
            print ("|        / \\  ")
            print ("|              ")
            print ("|              ")

for i in range(7):
    drawhm(i)
    print(i)
