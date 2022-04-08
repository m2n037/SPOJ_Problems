# your code goes here

def smpsum(a,b):
    sum =0
    for i in range(a, b+1):
        sum += i*i
    print(sum)

a,b = input().split()
a = int(a)
b = int(b)
smpsum(a,b)
