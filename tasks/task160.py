def p(d):
 for k in range(64):
  if sum(d[i:=k//8][s:=slice(j:=k%8,j+3)]+d[i+1][s])>4>d[i][j]==1:d[i][s]=d[i+2][s]=[0,2,0];d[i+1][s]=[2]*3
 return d