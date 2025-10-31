def p(d,E=enumerate,s=1):
 for _ in[0]*2:
  d=[*zip(*d)]
  if any(d[0]+d[-1])*s:(J,C),(Y,V)=sorted([(j,c)for r in d for j,c in E(r)if c]);q=(Y-J)*2;d=[[[c,[[c,V][(j-Y)%q<1],C][(j-J)%q<1]][j>=J]for j,c in E(r)]for r in d];s=0
 return d