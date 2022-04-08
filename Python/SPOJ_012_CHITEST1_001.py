# your code goes here

N = int(input())
k = 0

def chitest1(a,b):
    print(a + b)

while (k < N):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        a = float(a)
        b = float(b)
    k += 1
    chitest1(a,b)