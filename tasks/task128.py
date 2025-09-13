def p(d,R=range(15)):
 D=[*zip(*d)]
 for i in R:
  for j in R:
   if v:=d[i][j]:d[i-D[j].count(v)][j]=v;d[i][j]=0
 return d