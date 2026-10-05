#Print odd numbers, skip evens, stop at the first multiple of 7.
for i in range(1,100,1):
    if i%2==0:
        continue
    if i%7==0:
        break
    print(i,end=" ")