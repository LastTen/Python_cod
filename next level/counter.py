def clean_list(list_to_clean):
  res = []
  res.append(list_to_clean[0])
  for k in list_to_clean:
    try:
      if res.index(k):
        res = res
    except ValueError:
      res.append(k)
  return(res)

def counter(a, b):
  list_b = list(str(b))
  list_a = list(str(a))
  res = []
  for k in list_b:
    try:
      if list_a.index(k) >=0:
        res.append(k)
    except ValueError:
      res = res
  return len(clean_list(res))





print(counter(1233211, 12128))