def p(d):
 E=enumerate;R=range;H={}
 for i,r in E(d):
  for j,c in E(r):H[c]=H.get(c,[])+[(i,j)]
 for k in H:
  P,Q=zip(*H[k]);a=min(P);b=min(Q);y=max(P);z=max(Q);U=set()
  for i in R(a,y+1):U.add((i,b));U.add((i,z))
  for j in R(b,z+1):U.add((a,j));U.add((y,j))
  if {*H[k]}==U:return[c[b+1:z]for c in d[a+1:y]]