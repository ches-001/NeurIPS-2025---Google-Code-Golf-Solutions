def p(d,E=enumerate):
 I,J=divmod(sum(d,[]).index(3),len(d[0]))
 for i,r in E(d):
  for j,c in E(r):
   if c==2:d[i][int(2*(J+.5)-j)]=d[int(2*(I+.5)-i)][j]=d[i][j]
 return d