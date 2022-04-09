N = int(input())
k = 0
s = 0

while k < N:
    n = int(input())
    if n > 0:
        s += n
    else:
        s = s
    k += 1

return s