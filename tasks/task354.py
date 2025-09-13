def p(d,R=range(10)):
 def F(i,j,c):d[i][j]=c;[F(x,y,c)for x,y in[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]if 0<=x<10>y>=0 if d[x][y]==5]
 [F(i,j,d[0][j])for i in R for j in R if d[0][j]if d[i][j]];return d