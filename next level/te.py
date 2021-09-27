def count(folder, filename):
  res = folder
  try:
    if res.index(filename):
      return '/' + filename
  except ValueError:
    count1 = []
    for k in res:
      if type(k) == list:
        count1.append(k[0])
        cou1 = count(k, filename)
        count1.append(cou1)
    return count1

def del_text(fol_text):
  text = fol_text
  i = 0
  while i < len(text):
    if text[i] == []:
      text.pop(i-1)
    i = i + 1
  for k in text:
    if type(k) == list and len(k) > 1:
      del_text(k)
  return text

def serch(serch1):
  res = []
  if serch1[0] == '/':
    res.append(serch1)
    return serch1
  else:
    for k in serch1:
      if type(k) == str:
        res.append(k)
      elif type(k) == list and k != []:
        res.append(', '.join(serch(k)))
  return res

def file_search(folder, filename):
  res = [folder[0]]
  text = count(folder, filename)
  fol_del = del_text(text)
  fil_serch = serch(fol_del)
  if type(fil_serch) == str:
    res.append(filename)
  else:
    typ = ' '.join(fil_serch).replace(',','').split(' ')
    try:
      index = typ.index('/'+ filename)
      file = (typ[0:index])
      file.append(filename)
      revers = '/'.join(file)
      res.append(revers)
      # print('/'.join(res))
    except ValueError:
      return False
  if len(res) > 1:
    return('/'.join(res))




print(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 
'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))

print(file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'))

print(file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me'))
