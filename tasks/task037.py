def p(d):
 A=range;R=A(10);M={};D={}
 for r in R:
  for c in R:
   if v:=d[r][c]:
    if v not in D:
     if v not in M:M[v]=r,c
     else:f=M.pop(v);p=1 if r<f[0]else -1;q=1 if c<f[1]else -1;[d[r+p*u].__setitem__(c+q*u,v)for u in A(abs(r-f[0])+1)];D[f]=1
 return d