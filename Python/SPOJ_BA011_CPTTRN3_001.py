# your code goes here

N = int(input())
k = 0

def matrx(l,c):
    row = 3*l + 2
    col = 3*c + 2
    for i in range(1,row):
        for j in range(1,col):
            if (i == 1) or (i % 3 == 1):
                print("*", end = "")
            elif (i < row) and ((j == 1) or (j % 3 == 1)):
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