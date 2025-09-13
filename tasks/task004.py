def p(d):
 l=range;M=len(d);N=len(d[0]);R=l(M);C=l(N-1);O=[[0 for _ in l(N)]for _ in l(M)];s=any
 for r in R:
  if (r<M-1 and not s(d[r+1]))or(r==M-1 and s(d[r])):
   O[r]=d[r]
   t=[i for i,v in enumerate(O[r])if v]
   if t:
    t=t[-1];O[r-1][t]=d[r-1][t]
    if t+1<N:O[r-1][t+1]=0
    continue
  if not s(O[r]):
   for c in C: O[r][c+1]=d[r][c]if d[r][c]else 0
 return O