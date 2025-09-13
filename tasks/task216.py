def p(d):
 V=[];H=0
 for k in range(400):
  i,j=k//20,k%20;O=[(i,j)];P=0
  if d[i][j]and(i,j)not in V:
   for a,b in O:P+=d[a][b]==2;O+=[(x,y)for x,y in[(a+1,b),(a-1,b),(a,b+1),(a,b-1)]if 0<=x<20>y>=0 if d[x][y]if(x,y)not in O]
   V+=O
   if P>H:H=P;A,B=zip(*O)
 return[r[min(B):max(B)+1]for r in d[min(A):max(A)+1]]