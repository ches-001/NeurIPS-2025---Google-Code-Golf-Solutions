def p(d,E=enumerate,S=sorted,R=range,L=len):
 M=L(d);N=L(d[0]);A=R(M);B=R(N);G=[(r,c,d[r][c])for r in A for c in B if d[r][c]];P=lambda i,j:(min(i,j),max(i,j))
 if M < N:
  G=S(G,key=lambda x:x[1]);a,b=P(G[0][1],G[1][1])
  for w,c in E(R(a,N,b-a)):
   for r in A:d[r][c]=G[w%2][2]
 else:
  G=S(G,key=lambda x:x[0]);a,b=P(G[0][0],G[1][0])
  for w,r in E(R(a,M,b-a)):
   for c in B:d[r][c]=G[w%2][2]
 return d