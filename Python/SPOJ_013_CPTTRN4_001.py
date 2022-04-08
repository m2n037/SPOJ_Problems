# your code goes here

N = int(input())
k = 0

def matrx(l,c,h,w):
    for i in range(1,l*h+l+2):
        for j in range(1,c*w+c+2):
            if (i == 1) or (i % (h+1) == 1):
                print("*", end = "")
            elif (i < l*h+l+1) and ((j == 1) or (j % (w+1) == 1)):
                print("*", end = "")
            else:
                print(".", end = "")
            j += 1
        print("")
        i+=1
    print("\n")

while (k < N):
    l, c, h, w = input().split()
    l = int(l)
    c = int(c)
    h = int(h)
    w = int(w)
    k += 1
    matrx(l,c,h,w)