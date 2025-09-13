def p(d):
 R=range;M=R(12);C=lambda i:max(0,min(i,12-1))
 for r in M:
  for c in M:
   v=d[r][c];u=d[C(r-1)][c];b=d[C(r+1)][c];a=d[r][C(c-1)];i=d[r][C(c+1)]
   if u==b==a==i!=0:
    for i in R(1,3):d[r-i][c-i]=d[r+i][c+i]=d[r-i][c+i]=d[r+i][c-i]=v;d[r-i][c]=d[r+i][c]=d[r][c-i]=d[r][c+i]=u
 return d