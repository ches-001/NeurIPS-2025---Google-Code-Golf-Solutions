def p(d):
 R=range;M=N=len(d);d[0]=d[-1]=[3]*M
 for i in R(M):d[i][-1]=3
 m=M-1;M=1;n=0;N=N-2;e=-1;f=1
 while m>=0 and n>=0:
  for r in R(m,M,e):d[r][n]=3
  e*=-1;M,m=m-e*1,M+e*1
  for c in R(n,N,f):d[m][c]=3
  f*=-1;N,n=n-f*1,N+f*1
 return d