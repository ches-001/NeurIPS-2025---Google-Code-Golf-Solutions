def p(d,R=range(9)):
 for _ in R:d=[[[c:=d[i][j],7][sum(d[a][b]>0 for a,b in[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]if a<9>b)>1>c]for j in R]for i in R]
 return d