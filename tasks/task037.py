def p(d,R=range(10)):
 for c in{*sum(d,[])}-{0}:
  (I,J),(X,Y)=[(i,j)for i in R for j in R if d[i][j]==c]
  for r in d[I:X]:r[J]=c;J+=2*(Y-J>0)-1
 return d