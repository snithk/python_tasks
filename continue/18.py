#Print 1–200, skipping multiples of 3 or 5.
for i in range(1,201,1):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")