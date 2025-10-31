def p(d):
 F=lambda x:[*map(list,zip(*x[::-1]))];D=[[0]*4 for _ in[0]*4]
 for _ in[0]*4:
  d=F(d);D=F(D)
  for k in range(144):
   if (c:=d[i:=k//12][j:=k%12])==d[i+1][j]==d[i][j+1]>0:D[0][0]=D[1][0]=D[0][1]=c
 return D