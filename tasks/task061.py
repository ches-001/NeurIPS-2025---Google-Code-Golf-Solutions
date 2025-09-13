def p(d):
 R=range;N=18;Q=0
 for i in R(N):
  if {*d[i]}in[{1},{0,1}]:
   for j in R(N):d[j][i]=1
   d[i]=[1]*len(d[i]);Q=Q or i-Q
 D=R(-(N//-Q));K=R(1,Q+1)
 for i in D:
  for j in D:
   for a in K:
    for b in K:
     r=Q*i+a;c=Q*j+b
     if r<N and c<N:d[r][c]=d[r][c]or sorted([d[Q*q+a][Q*s+b]for q in D for s in D if Q*q+a<N and Q*s+b<N])[-1]
 return d