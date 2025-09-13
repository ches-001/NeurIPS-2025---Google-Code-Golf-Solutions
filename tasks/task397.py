def p(d,R=range):
 O=[]
 for i in R(10):
  for j in R(10):
   if(v:=d[i][j])not in[0,3]and(i,j)not in O:
    V=[(a+i,b+j)for a,b in[(0,1),(1,0),(1,1)]];O+=V
    for k in R(len({*[v]+[d[a][b]for a,b in V]})):d[i+2+k][j:j+2]=[3]*2
 return d