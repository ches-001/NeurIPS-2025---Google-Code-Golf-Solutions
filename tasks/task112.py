def p(d,E=enumerate):
 K=sum(d,[]).index(3);W=len(d[0])
 for i,r in E(d):
  for j,c in E(r):
   if c==2:d[i][int(2*(K%W+.5)-j)]=d[int(2*(K//W+.5)-i)][j]=d[i][j]
 return d