#Print the first 5 prime numbers.
count = 0
for i in range(1,100,1):
    sum=0
    for j in range(1,i+1,1):
        if i%j==0:
            sum+=1
    if sum==2:
        print(i)
        count += 1
        if count == 5:
            break