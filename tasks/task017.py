def p(d,E=enumerate):
 while not all([all(r)for r in d]):
  for i,r in E(d):
   for j,c in E(r):r[j]=c or d[j][i]or sorted([e for e in d if e[0]==r[0]or e[-1]==r[-1]],key=lambda x:sum([i!=0 for i in x]))[-1][j]
 return d