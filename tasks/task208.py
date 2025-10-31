def p(d,R=range(441),D=divmod,M=min):
 v=M(L:=sum(d,[]),key=L.count);V=[D(k,21)for k in R if L[k]==v];I,J=zip(*V);V=[(i-M(I),j-M(J))for i,j in V]
 for k in R:
  i,j=D(k,21);U=[(i+a,j+b)for a,b in V];X,Y=zip(*U);S=max(X);T=max(Y)
  if 1-any([sum(q[min(Y)+1:T])for q in d[M(X)+1:S]])>0<S<21>T:
   for a,b in U:d[a][b]=v
 return d