#Print 1–30, skipping even numbers.
for i in range(1,31,1):
    if i%2==0:
        continue
    print(i)