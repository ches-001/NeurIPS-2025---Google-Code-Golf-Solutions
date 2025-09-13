def p(d,E=enumerate):
 for i,r in E(d):
  for j,(c,C) in E(zip(r,zip(*d))):
   if c:J=r.index(c,j+1);I=C.index(c,i+1);return[[w and c for w in e[j+1:J]]for e in d[i+1:I]]