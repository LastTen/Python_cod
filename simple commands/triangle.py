import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

fir = x + y
sec = x + z
thr = y + z 

if fir <= z or sec <= y or thr <= x:
  print("not triangle")
else:
  print("triangle")