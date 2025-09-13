def p(d,E=enumerate):
 for i,r in E(d):
  for j,(c,C) in E(zip(r,zip(*d))):
   if c==0 and 2 in C[i:]:d[C.index(2,i)][j]=0;r[j]=2
 return d