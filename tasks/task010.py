def p(d):
 m={}
 for r in d:
  for c in range(9):
   if r[c]:m[c]=m.get(c,len(m)+1);r[c]=m[c]
 return d