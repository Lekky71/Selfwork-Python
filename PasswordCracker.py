def __cracker__(times):
    trial = str(raw_input())
    word = raw_input()
    trials = trial.split()
    password = ""
    while trials.__sizeof__() > 0:

        for t in trials:
            if word.__contains__(t) or password.__contains__(t):
                start = word.find(t)
                end = t.__len__() + 1
                if start == 0:
                    password += t + " "
                    word = word.replace(word[start: end], "")
                    trials.remove(t)
            else:
                print "WRONG PASSWORD"
                break
    print password

__cracker__(1)

