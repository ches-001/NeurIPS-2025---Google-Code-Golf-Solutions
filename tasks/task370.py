def p(d,E=enumerate):
 m=min(A:=sum(d,[]),key=A.count);V=[(i,j)for i,r in E(d)for j,c in E(r)if c<1];X,Y=divmod(A.index(m),W:=len(d[0]));H=len(d);Q=[-1,0];X=X-V[Q[0 in d[X-1]]][0];Y=Y-V[Q[0 in[*zip(*d)][Y-1]]][1];n=0
 for _ in[0]*4:
  for a,b in V[n:]:
   if H>(s:=a+X)>=0<=(t:=b+Y)<W:d[s][t]=m;V+=[(s,t)];n+=1
 return d