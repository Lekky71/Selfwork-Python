def max_heapify(a, i):
    heap_size = len(a)
    l = 2 * i
    r = 2 * i + 1
    if l <= heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)


def build_max_heap(a):
    for i in range(len(a) / 2, -1, -1):
        max_heapify(a, i)


arry = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
build_max_heap(arry)
print arry
