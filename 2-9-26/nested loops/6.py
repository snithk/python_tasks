
#Pairs with Target Sum
#Print all pairs (a, b) between 1 and 50 whose sum is 30. Print each pair only once.
for i in range(1,51,1):
    for j in range(i,51,1):
        if j+i==30:
            print(f"({i}, {j})")
