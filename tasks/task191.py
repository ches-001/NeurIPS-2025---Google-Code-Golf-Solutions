def p(d,R=range,D=divmod):
 o=[0]*23;d=[[0]*2+r+[0]*2 for r in [o,o,*d,o,o]];L=sum(d,[]);I,J=D(L.index(1),27);Z,H=D(728-L[::-1].index(1),27);V=[(i,j,d[i][j])for i in R(I,Z+1)for j in R(J,H+1)];A,B,_=zip(*V);V=[(i-min(A),j-min(B),c)for i,j,c in V];A,B,_=zip(*V);X=(max(A)+min(A))//2;Y=(max(B)+min(B))//2
 for _ in[0]*4:
  for _ in[0]*2:
   for k in R(729):
    i,j=D(k,27);U=[(i+a,j+b,c)for a,b,c in V];x,y,_=zip(*U);S=max(x);T=max(y)
    if S<27>T and all(d[a][b]==[0,4][c==4]for a,b,c in U):
     for a,b,c in U:d[a][b]=c
   V=[(a,2*Y-b,c)for a,b,c in V]
  V=[(-b+X+Y,a-X+Y,c)for a,b,c in V]
 return[r[2:-2]for r in d[2:-2]]