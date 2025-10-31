def p(d,R=range):
 def F(i,j,c,V):
  if 0<=i<H>j>=0<d[i][j]==c and(i,j)not in V:V+=[(i,j)];[F(i+1-t//3,j+1-t%3,c,V)for t in R(9)]
 for _ in[0]*8:d=[*zip(*d[::-1])];H=len(d);[exec('d[a]=[*d[a]];d[a][2*j-1-b]=d[i][j-1]')for k in R(H*H)if 0<(c:=d[i:=k//H][j:=k%H])!=d[i][j-1]>0 if not F(i,j,c,V:=[])for a,b in V]
 return d