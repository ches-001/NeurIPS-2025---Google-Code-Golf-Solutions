R=range;L=len
def W(d,v,E,h,w):
 C=[];A=R(-1,2)
 for i in A:
  for j in A:
   r,c=v[0]+i,v[1]+j;u=(r,c)
   if 0<=r<h and 0<=c<w and d[r][c]and u not in E:
    if d[r][c]==2:return 1
    E+=[u];C+=[W(d,u,E,h,w)]
 return any(C)
def p(d):h=L(d);w=L(d[0]);E=[[(i,j),(i,j+1),(i+1,j),(i+1,j+1)]for i in R(h)for j in R(w)if d[i][j]==2][0];return[[any([W(d,v,E,h,w)for v in E])*8]]