z_num = {'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1,'0':1}

def count_holes(n):
  num1 = []
  res = []
  if type(n) == float:
    return("ERROR")
  else:
    try:
      num = int(n)
      if num >= 0:
        num1.append(num)
      elif num < 0:
        num = (- num)
        num1.append(num)
      else:
        print(0)
    except ValueError:
      return("ERROR")
    i = 0
    us_num = str(num1[0])
    for k in us_num:
      if z_num[k]:
        res.append(z_num[k])
    return sum(res)



print(count_holes(0))
print(count_holes("01"))
print(count_holes("28888888000000"))
print(count_holes(-8000000))
print(count_holes(-8.0))
print(count_holes('-8.5'))
