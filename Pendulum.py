go = True
while go is True:
    try:
        length = float(input("enter the value of the length of the pendulum>>"))
        gravity = input("enter your value of g >>")
        go = False
    except:
         print("FOOL!!! ENTER A GODAMN NUMBER>>")


if go is False:
    import math
    period = 2 * math.pi * math.sqrt(length/gravity)
    print "The period of this pendulum is %.2f seconds" % period

