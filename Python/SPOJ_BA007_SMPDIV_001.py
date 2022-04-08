# your code goes here

t = int(input())
k = 0

def smpdiv(n, x, y):
    for i in range(1, n+1):
        if (i % x == 0 and i % y != 0):
            print(i, end = " ")

while(k < t):
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    k += 1
    smpdiv(n, x, y)
    