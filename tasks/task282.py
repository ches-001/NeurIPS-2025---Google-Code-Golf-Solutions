def p(d,R=range):
 V=[]
 for k in R(64):
  i=k//8+1;j=k%8+1
  if d[i][j]and(i,j)not in V:
   for a in R(i-1,i+2):
    for b in R(j-1,j+2):d[a][b]=(1+(abs(i-a)==abs(j-b)==1)*4)*((i,j)!=(a,b));V+=[(a,b)]
 return d