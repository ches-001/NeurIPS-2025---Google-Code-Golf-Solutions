def p(d):
 H=len(d);W=len(d[0]);a,b,x,y=H,0,W,0
 for k in range(H*W):
  i,j=k//W,k%W
  if d[i][j]!=1:a=min(i,a);b=max(i,b);x=min(j,x);y=max(j,y)
  else:d[i][j]=0
 return[r[x:y+1]for r in d[a:b+1]]