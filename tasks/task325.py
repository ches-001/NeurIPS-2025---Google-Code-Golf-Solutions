def p(d,R=range):
 def F(i,j,s=0):
  if len(d)>i>=0<=j<W>0<d[i][j]:d[i][j]=0;s+=1;[F(i+1-a//3,j+1-a%3)for a in R(9)]
  return s
 W=len(d[0]);W=R(sum(F(k//W,k%W)for k in R(300)));return[[8*(i==j)for j in W]for i in W]