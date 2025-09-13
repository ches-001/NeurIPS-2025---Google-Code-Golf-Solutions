def p(d,w=0):
 S=0,0
 for r in d:
  for j,(c,C)in enumerate(zip(r,zip(*d))):
   if 0<j<len(r)and r.count(c)==C.count(c)==1:
    if r[j-1]==0:S=j+1,len(r)
    if r[j+1]==0:S=j-1,-1,-1
    for u in range(*S):r[u]=r[u]or c
 d=[*map(list,zip(*d))];return d if w else p(d,w+1)