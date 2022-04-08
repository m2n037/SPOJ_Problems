# your code goes here

N = int(input())
k = 0

def matrx(l,c):
    for i in range(1,l+1):
        for j in range(1,c+1):
            if (i == 1) or (i == l):
                print("*", end = "")
            elif ((i < l) and (j == 1 or j == c)):
                print("*", end = "")
            else:
                print(".", end = "")
            j += 1
        print("")
        i+=1
    print("\n")

while (k < N):
    l, c = input().split()
    l = int(l)
    c = int(c)
    k += 1
    matrx(l,c)
    