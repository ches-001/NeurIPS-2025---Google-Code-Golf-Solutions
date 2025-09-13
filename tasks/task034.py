def p(d):
 R=range;M=R(9);Q=[];V=[];O=[-1,1];F=lambda i:max(0,min(i,8))
 for r in M:
  for c in M:
   if v:=d[r][c]:
    V+=[(r,c)]
    if v!=2:C=v
    else:Q+=[(r,c)]
 for i in R(2):
  for j in R(2):
   r,c=V[0];a=r+i;b=c+j
   if (a,b)in Q:
    while 0<=a<9 and 0<=b<9:
      for x in R(-1,2):d[F(a+x)][F(b)]=C;d[F(a)][F(b+x)]=C
      a+=O[i];b+=O[j]
 return d