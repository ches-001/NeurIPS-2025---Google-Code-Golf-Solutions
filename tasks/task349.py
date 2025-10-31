def p(d,R=range):
 def F(i,j,V):
  if W>j>=0<=i<H>0<d[i][j]==9 and(i,j)not in V:V+=[(i,j)];[F(i+1-a//3,j+1-a%3,V)for a in R(9)]
 for _ in[0]*4:
  d=[*map(list,zip(*d[::-1]))];H,W=len(d),len(d[0])
  for k in R(H*W):
   F(k//W,k%W,V:=[])
   if V:A,B=zip(*V);I=max(A);J=max(B);Y=min(B);w=max(I-min(A),J-Y)+1;t=0;[[[exec('d[x][a]=3')for a in R(Y-t-1,J+t+2)if H>(x:=I+e+1)>=0<=a<W!=d!=t],t:=t+1]for e in R(w//2)]
 return[[C[i]or[C[i],1][9 in C[:i]]for C in zip(*d)]for i in R(H)]