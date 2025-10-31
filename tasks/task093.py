def p(d):
 for _ in[0]*4:
  d=[*map(list,zip(*d[::-1]))]
  if x:=d[0].count(5):
   for r in d:a=r.index(5)+x-1;r[a:]=sorted(r[a:])[::-1]
 return[[c and 5 for c in r]for r in d]