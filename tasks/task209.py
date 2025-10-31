def p(d):
 A,B=zip(*[(i,j)for i,r in enumerate(d)for j,c in enumerate(r)if c==4]);Q=[r[min(B):max(B)+1]for r in d[min(A):max(A)+1]];W=[*zip(*filter(any,zip(*filter(any,d[max(A)+1:]))))];N=sum([4!=v>0 for r in Q for v in r])
 for a in range(2,5):
  e,x=len(W)*a,len(W[0])*a;w=len(Q[0]);U=[[W[i//a][j//a]for j in range(x)]for i in range(e)]
  for k in range(len(Q)*w):
   i,j=k//w,k%w;Z=[r[j:j+x]for r in Q[i:i+e]];S=[c==v for a,b in zip(U,Z)for c,v in zip(a,b)if 4!=v>0]
   if S and all(S)&(sum(S)==N):
    for a in range(e):
     for b in range(x):Q[i+a][j+b]=U[a][b]
    return Q