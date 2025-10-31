def p(d, R=range,K=min,M=max):
 F=lambda i,j, V:0<=i<10>j>=0 and d[i][j]==3 and(i,j)not in V and not V.add((i,j))and[F(i+a,j+b,V)for a in R(-1,2)for b in R(-1,2)]and V
 for k in R(100):
  i,j=k//10,k%10
  if d[i][j]==3:
   V=set();F(i,j,V);A,B=zip(*V)
   for a,b in V:d[K(9,M(0,a+[n:=int((len(V)/2)**.5),-n][a>(M(A)+K(A))/2]*2))][K(9,M(0,b+[-n,n][b>(M(B)+K(B))/2]))]=8
 return d