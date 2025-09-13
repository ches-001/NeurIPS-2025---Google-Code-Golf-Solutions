def p(d,R=range):
 H,W=len(d),len(d[0])
 for k in R(H*W):
  i=k//W;j=k%W
  if d[i][j]==2 and any(d[a][b]==2 for a,b in[(i,j-1),(i,j+1),(i-1,j),(i+1,j)]if 0<=a<H>0<=b<W):
   for a in R(i-1,i+2):
    for b in R(j-1,j+2):
     if 0<=a<H>0<=b<W:d[a][b]=d[a][b]or 3
 return d