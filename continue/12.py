#Print 1–40, skipping multiples of 4.
for i in range(1,41,1):
    if i%4==0:
        continue
    print(i)
