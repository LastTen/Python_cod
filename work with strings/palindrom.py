import sys

text = sys.argv[1]


regtext = text.lower().replace(' ', '')
pali = regtext[::-1]

if regtext == pali:
  print('yes')
else:
  print('no')