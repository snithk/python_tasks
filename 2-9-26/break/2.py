#Find the first prime number between 50 and 100.

for i in range(50,100):
    sum=0
    for j in range(1,i+1,1):
        if i%j==0:
            sum+=1
    if sum==2:
        print(j)
        break

