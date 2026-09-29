for i in range(1,10,1):
    for j in range(1,9,1):
        if i==9 or j==4 or (i+j==5 and i<=3):

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()