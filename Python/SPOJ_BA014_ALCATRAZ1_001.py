# your code goes here

N = int(input())
k = 0

def alcatraz1(n):
    sum = 0
    for i in n:
        sum += int(i)
    print(sum)

while (k < N):
    n = input()
    n = str(n) 
    k += 1
    alcatraz1(n)