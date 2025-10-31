def p(d,E=enumerate):
 def F(i,j,V):
  if len(d)>i>=0<=j<len(d[0])and d[i][j]and(i,j)not in V:V+=[(i,j)];[F(i+1-a//3,j+1-a%3,V)for a in range(9)]
  return sum([d[a][b]==9 for a,b in V])
 for _ in[0]*28:d=[*zip(*[[[c,(c>0)*2][sum(r[j-1:j+2])==9>0<i>0<d[i-1][j]==3 or r[j-(j>0)]==2]for j,c in E(r)]for i,r in E(d)][::-1])]
 for t in range(20):d=[*zip(*[[[[[c,[1,1,6][a:=F(i,j,[])]][c!=9>a>0],9][j>0<=i<len(d)-1>2!=c==r[j-1]==d[i+1][j]>0],[c,r[j-(j>0)]or c][c==9]][t>16]for j,c in E(r)]for i,r in E(d)][::-1])]
 return d