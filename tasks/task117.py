def p(d,E=enumerate):
 I,J=[(i,j)for i,r in E(d[1:-1],1)for j,c in E(r[1:-1],1)if c if str(d).count(str(c))==5 if all(d[a][b]==c for a in[i-1,i+1]for b in[j-1,j+1])][0]
 for i,r in E(d):
  for j,c in E(r):
   if d[I][J]!=c>0:a=2*I-i;b=2*J-j;d[a][j]=d[i][b]=d[a][b]=d[i][j]
 return d