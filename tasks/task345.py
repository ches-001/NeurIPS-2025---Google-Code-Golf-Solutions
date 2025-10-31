def p(d,R=range(10)):
 for j in R:
  if d[-1][j]==2:
   c=0
   for i in R:
    if d[~i][j+c]>4:c+=1;d[-i][j+c]=2
    d[~i][j+c]=2
 return d