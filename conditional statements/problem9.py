'''
Display the season based on the month number.
    3–5 → Spring, 6–8 → Summer, 9–11 → Autumn, 12/1/2 → Winter.
'''
n=int(input("enterthe month : "))
if n>=3 and n<=5:
    print('Spring season')
elif n>=6 and n<=8:
    print('Summer season')
elif n>=9 and n<=11:
    print('Autumn season')
else:
    print('Winter. season')
