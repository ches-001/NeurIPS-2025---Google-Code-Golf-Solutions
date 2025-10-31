def p(d,R=range):
 def F(i,j,V,c):
  if 0<=i<20>j>=0<d[i][j]==c and(i,j)not in V:V+=[(i,j)];[F(i+1-a//3,j+1-a%3,V,c)for a in R(9)]
 for k in R(400):
  i,j=k//20,k%20
  if d[i][j]==5:
   F(i,j,V:=[],5)
   if len(V)!=24:continue
   for m in R(400):
    a,b=m//20,m%20;c=d[a][b];F(a,b,T:=[],c)
    if T and 5!=c>1 and i<a<i+7>0<j<b<j+7:
     for t in R(400):
      F(t//20,t%20,U:=[],1)
      if len(U)==len(T):
       A,B=zip(*U);M,N=zip(*T)
       if max(A)-min(A)==max(M)-min(M)and max(B)-min(B)==max(N)-min(N):
        for s,o in U:h,l=T[0];d[s][o]=d[h][l]
 return d