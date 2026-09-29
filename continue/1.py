#Print 1–50, skip multiples of 3, stop at 40.
for i in range(1,51,1):
    if i%3==0:
        continue
    if i==40:
        break
    print(i,end=" ")


