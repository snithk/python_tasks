#Stop when 3 consecutive odd numbers occur between 1 and 50.
c=0
for i in range(1,51,2):
    print(i)
    c+=1
    if c==3:
        break
d=0
for i in range(1,51,1):
    if i%2!=0:
        d+=1
        print(i)
    
    if d==3:
        break