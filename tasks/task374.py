def p(d):
 def F(i,j,V):d[i][j]=0;V+=[(i,j)];[F(x,y,V)for x,y in[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]if 0<=x<10>y>=0 if d[x][y]]
 for V,c in zip(sorted([(V:=[],F(i,j,V))[0]for k in range(100)if d[i:=k//10][j:=k%10]],key=len),[2,4,1]):
  for a,b in V:d[a][b]=c
 return d