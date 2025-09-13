def p(d,E=enumerate):
 A,B=zip(*[(i,j)for i,r in E(d)for j,c in E(r)if 5!=c!=0]);C=(min(A)+max(A))//2,(min(B)+max(B))//2
 for i,r in E(d):
  for j,c in E(r):
   if c==5:
    for a,b in zip(A,B):d[a+i-C[0]][b+j-C[1]]=d[a][b]
 return d