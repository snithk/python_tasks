#Print 1–30, skipping numbers from 10–20.
for i in range(1,31,1):
    if i>=10 and i<=20:
        continue
    print(i)