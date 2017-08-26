def __count_pattern__(word):
    # word = 'akin got 230 in UTME'
    num = 0
    for i in range(1, word.__len__()):
        pattern = '1' + '0' * i + "1"
        position = word.find(pattern)
        while position != -1:
            num = num + 1
            position = word.find(pattern, position+1)
    return num

count = input()
Arr = {}
for i in range(0, count):
    s = raw_input().strip()
    Arr[i] = __count_pattern__(s)
for j in Arr:
    print Arr[j]
