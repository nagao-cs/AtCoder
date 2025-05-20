def solve():
  s = input()
  chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
  
  s_set = set()
  for c in s:
    s_set.add(c)
  
  candidate = chars - s_set
  if candidate:
    return candidate.pop()
  
if __name__ == '__main__':
  print(solve())
  