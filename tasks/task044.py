def p(d):
 C=max([C[i]for i in range(10)for j,C in zip(range(10),zip(*d))if sum(x:=[*d[i][j-(j>0):j+2],*C[i-(i>0):i+2]])==2*C[i]or x.count(C[i])==2]);L=[]
 def F(i,j,V,c):
  if 0<=i<10>j>=0<d[i][j]==c and(i,j)not in V and (i,j)not in L:V+=[(i,j)];[F(i+1-a//3,j+1-a%3,V,c)for a in range(10)]
 for k in range(100):
  F(k//10,k%10,V:=[],5);L+=V
  if V:
   A,B=zip(*V);U=[(i,j)for i in range(min(A),max(A)+1)for j in range(min(B),max(B)+1)if d[i][j]<1]
   if U:
    A,B=zip(*U);Q=[(i-min(A),j-min(B))for i,j in U]
    for m in range(100):
     F(x:=m//10,y:=m%10,Z:=[],d[x][y]);S=[(i+x,j+y)not in L and i+x<10>j+y and C!=(c:=d[i+x][j+y])>0<c!=5 for i,j in Q]
     if all(S)and sum(S)==len(Z):
      for t in range(len(Q)):a,b=Q[t];a+=x;b+=y;s,t=U[t];d[a][b],d[s][t]=d[s][t],d[a][b];L+=[(s,t)]
 return d