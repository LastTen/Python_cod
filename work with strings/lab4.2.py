import sys

text = sys.argv

text.pop(0)

r_text = text[::-1]

join_text = ' '.join(r_text)

print(join_text)