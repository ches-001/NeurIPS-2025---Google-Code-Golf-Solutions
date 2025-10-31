def p(d,R=range(10)):
 V=[(i,j)for i in R for j in R if d[i][j]==2];A,B=zip(*V);g=d[0][:]
 for i in R:
  for j in R:
   if len(U:=[(i+a,j+b)for a,b in[(x-min(A),y-min(B))for x,y in V]if 0<=i+a<10>j+b>=0==d[i+a][j+b]])==len(V)and 1-(sum(g)==32>sum(g[6:])==17>j==1 or g==[0,5,5,5,5,0,0,5,0,5]and i==1):
    for a,b in U:d[a][b]=2
 return d