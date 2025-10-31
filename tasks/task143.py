def p(d,R=range(10)):
 C={*sum(d,[])}-{0,5,t:=max(d[0][:3]+d[2][:3])};F=lambda c,a=0,b=0:[(i-a,j-b)for i in R for j in R if d[i][j]==c];W=F(t);A,B=zip(*W);W=F(t,min(A),min(B))
 for c in C:
  V=F(c);A,B=zip(*V)
  if F(c,min(A),min(B))==W:
   for i,j in V:d[i][j]=5
 return d