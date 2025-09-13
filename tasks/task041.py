def p(d,q=0):
 for r in d:
  for j,c in enumerate(r):
   if c:q=(not q)*c
   else:r[j]=q
 return d