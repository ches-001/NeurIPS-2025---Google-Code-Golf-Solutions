def p(d):
 H=len(d);W=len(d[0]);R=range;_,X,Y,A,B=max([[h*w,i,j,h,w]for h in R(2,H+1)for w in R(2,W+1)for i in R(H-h+1)for j in R(W-w+1)if[*zip(*d[i:i+h])][j:j+w]==[(0,)*h]*w])
 for r in d[X:X+A]:r[Y:Y+B]=[6]*B
 return d