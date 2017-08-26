def decideIfPangram(s):
    sentence = s.strip()
    base = 'abcdefghijklmnopqrstuvwxyz'
    answers = 'answers'
    for i in range(0,len(base)):
        character = base[i]
        if sentence.find(character) != -1:
            answers = 'pangram'
        else:
            answers = 'not pangram'
            break
    print (answers)
search = raw_input()
newword = search.lower()
decideIfPangram(newword)