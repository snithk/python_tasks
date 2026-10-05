#Print the first 5 even numbers.
count = 0
for i in range(1,31,1):
    if i%2==0:
        print(i)
        count += 1
        if count == 5:
            break