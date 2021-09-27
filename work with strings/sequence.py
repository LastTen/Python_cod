import sys

arg = sys.argv[1]
r = []
l = []

for k in arg:
  if k == '(':
    r.append(k)
  elif k == ')' and len(r) > len(l):
    l.append(k)


if len(arg)/2 == len(r) and len(r) == len(l):
  print("YES")
else:
  print("NO")