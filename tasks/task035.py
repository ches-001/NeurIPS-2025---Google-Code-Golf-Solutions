def p(d):
 for i,(r,c)in enumerate(zip(d,zip(*d))):
  if 0!=r[0]!=8:d[i][r.index(8)]=r[0]
  if 0!=r[9]!=8:d[i][9-r[::-1].index(8)]=r[9]
  if 0!=c[0]!=8:d[c.index(8)][i]=c[0]
  if 0!=c[9]!=8:d[9-c[::-1].index(8)][i]=c[9]
 return d