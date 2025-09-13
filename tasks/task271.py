def p(d,R=range):
 B=0;U=[]
 for k in R(81):
  i,j=k//9,k%9
  if c:=d[i][j]:
   O=[(i,j,c)];T=0
   for f,g,_ in O:
    T+=d[f][g]==1;d[f][g]=0;O+=[(a,b,l)for a,b in[(f+1,g),(f-1,g),(f,g-1),(f,g+1)]if 0<=a<9>b>=0 if(l:=d[a][b])if(a,b,l)not in O]
   if T>B:B=T;U=sorted(O,key=lambda v:v[0]*9+v[1])
 return[[U[i*3+j][2]for j in R(3)]for i in R(3)]