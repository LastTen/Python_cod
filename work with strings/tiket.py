import sys

def plusz(num):
  nup_pl = []
  for k1 in num:
    nup_pl.append(k1)

  while len(nup_pl) < 6:
    nup_pl.insert(0, "0")

  return ''.join(nup_pl)

def num_sum(tiket_num):
  sum_num1 = list(tiket_num[0:3:+1])
  sum_num2 = list(tiket_num[3:6:+1])

  int_lst1 = sum([int(x) for x in sum_num1])
  int_lst2 = sum([int(x) for x in sum_num2])
  if int_lst1 == int_lst2:
    return 1
  else:
    return 0

num1 = sys.argv[1]
num2 = sys.argv[2]

tik = []
happy_tiket = []
for i in range(int(num1), int(num2)+1):
  tik.append(plusz(str(i)))

for k in tik:
  happy_tiket.append(num_sum(k))

print(sum(happy_tiket))





