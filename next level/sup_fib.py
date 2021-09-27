
def super_fibonacci(n, m):
  m_count = [1]
  i = m
  while i > 0 +1:
    m_count.append(1)
    i = i - 1
  j = n
  while j > 0:
    sum_f = sum(m_count[len(m_count) - m:len(m_count)])
    m_count.append(sum_f)
    j = j - 1
    print(m_count)
  return(m_count[n-1])


print(super_fibonacci(8, 2))