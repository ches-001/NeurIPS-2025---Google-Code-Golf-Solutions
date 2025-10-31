def p(d,R=range(9)):
 V=[(i,j)for i in R for j in R if d[i][j]];A,B=zip(*V);W=[(i-A[0],j-B[0])for i,j in V if d[i][j]==2];m=max({*sum(d,[])}-{2})
 for a,b in W:
  for i,j in V:
   while 0<=(i:=i+2*a-1)<9>(j:=j+2*b-1)>=0:d[i][j]=m
 return d