def p(d):
 E=enumerate
 for i,r in E(d):
  for j,(c,C)in E(zip(r,zip(*d))):
   if c==8:
    if 8 in r[j+1:]:a=j+r[j+1:].index(8);r[j+1:a+1]=[3]*(a-j)
    if 8 in C[i+1:]:
     for f in range(i+1,i+C[i+1:].index(8)+1):d[f][j]=3
 return d