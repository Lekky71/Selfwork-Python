Arr = [6, 5, 4, 1, 2, 3]
for j in range(1, Arr.__len__()):
    key = Arr[j]
    i = j - 1
    while i > -1 and Arr[i] > key:
        Arr[i+1] = Arr[i]
        i = i - 1
    Arr[i+1] = key
print Arr


