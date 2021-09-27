import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

shif_text = sys.argv[1]

no_gap = list(shif_text.replace(' ', ''))

for k in range(5, len(no_gap), 5):
  no_gap[k] = ' ' + no_gap[k]

join_text = ''.join(no_gap)

five_w = (join_text.split(' '))

res = []

for l in five_w:
  if len(l) == 5:
    res.append(l)

res1 = []

for word in res:
  for k in word:
    if k.islower():
      res1.append('a')
    else:
      res1.append('b')

for k in range(5, len(res1), 5):
  res1[k] = ' ' + res1[k]

shif = ''.join(res1).split(' ')

reshif = []
for k in range(0, len(shif)):
  num_alf = key.index(shif[k])
  word_alf = alphabet[num_alf]
  reshif.append(word_alf)

res = "".join(reshif)
print(res)

