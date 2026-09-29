#Print 1–50, skipping multiples of 3.
for i in range(1,51,1):
    if i%3==0:
        continue
    print(i)