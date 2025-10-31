def p(d,R=range(15)):
 def F(i,j):
  if i<15>j and d[i][j]>7:d[i][j]=0;F(i+1,j);F(i,j+1)
 for a in R:F(a,0);F(0,a)
 return[[[[c:=d[i][j],4][c>7],8-5*any(any(r[j-(j>0):j+2])for r in d[i-(i>0):i+2])][c<1]for j in R]for i in R]