def p(d,E=enumerate,w=0):
 for r in d:
  for j,c in E(r):
   if c and c in r[j+1:]:J=r[j+1:].index(c);r[j+1:j+J+1]=[c]*J
 d=[*map(list,zip(*d))];return d if w else p(d,E,w+1)