def p(d):
 E=enumerate;M={}
 for i,r in E(d):
  for j,c in E(r):
   if c:M[c]=M.get(c,[])+[(i,j)]
 V,U=zip(*M[min(M,key=lambda x:len(M[x]))]);return[c[min(U):max(U)+1]for c in d[min(V):max(V)+1]]