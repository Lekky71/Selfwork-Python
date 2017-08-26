# #An alien has been shot down
#
# alien_color = str(raw_input("Enter the alien color : "))
# # alien_color = str(alien_color)
# if alien_color == 'green' :
#     print('You just earned 5 points')
# if alien_color == 'yellow' :
#     print('you just earned 10 points')
# if alien_color == "red":
#     print('you just earned 15 points')
# # else :
# #     print("pele o")
import urllib2, json
u = urllib2.urlopen('https://getbible.net/json?passage=1John1:77')
b = u.read()
print (b)
y = str(b)

# OpenBiblePage open holy bible to {Book} {Chapter} verse {Verse}
# OpenBiblePage open my holy bible to {Book} {Chapter} verse {Verse}
# OpenBiblePage open the scriptures to {Book} {Chapter} {Verse}