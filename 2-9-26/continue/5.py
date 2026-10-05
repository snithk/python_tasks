#Search from 51, skip non-multiples of 9, stop at the first multiple of 9.
c=0
for i in range(51,100,1):
    if i%9!=0:
        continue
    elif i%9==0:
        c+=1
        print(i)
        if c==9:
          
            break