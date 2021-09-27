
def type_list(list_folder):
  type_res = []
  for k in list_folder:
    if type(k) == str:
      word = k + '*' + ','
      type_res.append(word)
    elif type(k) == list:
      k[0] = k[0] + '-'
      w = type_list(k).replace('*', '**')
      type_res.append(w)

  return ''.join(type_res)

def count(levl_word, filename):
  i = 0
  while i < len(levl_word):
    if levl_word[i].replace('*', '') == filename:
      return i
    i = i +1

def file_search(folder, filename):
  res = [folder[0]]
  srt_folder = type_list(folder[0:len(folder)])
  levl_word = srt_folder.split(',')
  count_l = count(levl_word, filename)
  num_word = levl_word[0:count_l+1]
  print(num_word)




file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 
'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')