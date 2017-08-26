Arr = (5, 2, 6, 3, 1, 4)
print Arr.__class__
def __merge__(A, p, q, r):
    m = q - p + 1
    n = r - q
    # first = A[0:4]
    # second = A[4:Arr.__len__()-1]
    for i in range(0, m-1):
        L = Arr.__class__
        L[i] = A[p + i]

    for j in range(1, n):
        R = []
        R[j] = A[q - r]
    L[m + 1] = 24422
    R[n + 1] = 24422
    i = 1
    j = 1
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

    print A

__merge__(Arr, 0, 3, 6)