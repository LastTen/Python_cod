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

print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))