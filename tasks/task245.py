def p(d,E=enumerate):
 def F(v):V=[*zip(*[(i,j)for i,r in E(d)for j,c in E(r)if c==v])];return(min(V[0])+max(V[0]))//2,(min(V[1])+max(V[1]))//2
 G=F(3);R=F(2);return[[2*(d[i-G[0]+R[0]][j-G[1]+R[1]]==2)+c*(c!=2)for j,c in E(r)]for i,r in E(d)]