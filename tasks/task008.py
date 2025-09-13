def p(d):
 A=range;L=len;M=L(d);N=L(d[0]);R=A(M);C=A(N);V=[];[(V.append((r,c)))for r in R for c in C if d[r][c]==2];K=lambda i:max(0,min(i,M-1));Y=lambda j:max(0,min(j,N-1));G=[];i=1;j=1
 while not G:
  for p in V:
   if G:break
   r=p[0];c=p[1];u=K(r+i);v=Y(c+j);s=K(r-i);h=Y(c-j)
   if d[K(s-1)][c]==8:i=-i;j=0
   if d[K(u+1)][c]==8:j=0
   if d[r][Y(h-1)]==8:i=0;j=-j
   if d[r][Y(v+1)]==8:i=0
   if i==0 or j==0:G=[(f[0]+i,f[1]+j)for f in V]
  i+=1;j+=1
 for p in V:d[p[0]][p[1]]=0
 for g in G:d[g[0]][g[1]]=2
 return d