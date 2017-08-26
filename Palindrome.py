def is_palindrome(word):
    limit = len(word)/2
    first_half = word[0:limit]
    endpoint = len(word) % 2 == 0
    last = limit
    if endpoint:
        last = limit - 1
    second_half = word[len(word)+1:last:-1]
    print (second_half)
    if first_half == second_half:
        return True
    else:
        return False
print(is_palindrome('mom'))
