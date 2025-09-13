def p(d):
 R=range;M=len(d);N=len(d[0]);d*=2;d=[d[i]*2 for i in R(M*2)]
 def W(r,c):
  if 0<=r<M*2 and 0<=c<N*2 and d[r][c]==0:d[r][c]=8
 [(W(r+1,c+1),W(r-1,c+1),W(r-1,c-1),W(r+1,c-1))for r in R(M*2)for c in R(N*2)if d[r][c]not in[0,8]];return d