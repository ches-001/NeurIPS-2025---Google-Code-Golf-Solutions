def p(d):
 R=range
 for r in R(9):
  for c in R(9):
   if d[r][c]==2:d[r+1][c+1]=d[r-1][c-1]=d[r+1][c-1]=d[r-1][c+1]=4
   elif d[r][c]==1:d[r+1][c]=d[r-1][c]=d[r][c+1]=d[r][c-1]=7
 return d