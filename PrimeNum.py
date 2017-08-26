# num = 2
# n = input("enter the number")
# for num in range(2, n):
#     if num > 1:
#        # check for factors
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
from pprint import pprint
import urllib2
import json
def jsonDefault(object):
    return object.__dict__
u = urllib2.urlopen('https://getbible.net/json?passage=1John3:19')
y = u.read()
# resp = json.loads(u.read().decode('utf-8'))
# jsonAbder = json.dumps(resp, default=jsonDefault)
print(y)
verse_positon = y.find('\"verse\"')
start = verse_positon + 9
stop = y.find('\"',start+1)
reading = y[start:stop]
print reading