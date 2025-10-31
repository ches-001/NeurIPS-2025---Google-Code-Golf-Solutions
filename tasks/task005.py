def p(m,R=range):
 _,Y,X,t=min([(sum(t:=[r[x:x+3]for r in m[y:y+3]],m).count(0),y,x,t)for y in R(19)for x in R(19)])
 for h in R(9):
  for k in R(1,19):
   a,b=4*(1-h//3),4*(1-h%3);y=Y+a*k;x=X+b*k
   for w in R(9):
    if a|b!=0<=x+(j:=w%3)<21>y+(i:=w//3)>=0:m[y+i][x+j]=t[i][j]and max(max(r[X+b:X+b+3])for r in m[Y+a:Y+a+3])
 return m