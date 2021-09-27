import sys


x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
song = "Everybody sing a song:"
si = "la"
la_1 = ((si + "-") * (x - 1)) + si
la_2 = (" " + la_1) * y

if z == 1:
    print(song + la_2 + "!")
else:
    print(song + la_2 + ".")
