def p(d):
 A=range;N=len(d);R=A(N);C=[*zip(*d)];V=[(i,j)for i in R for j in R if d[i][j]==3];O=[[V[0],[V[1]]],[V[1],[V[0]]]]
 while O:
  ((k,l),P),*O=O
  if d[k][l]==2 and all([0<v[0]<N-1>0<v[1]<N-1 for v in P])and(d[P[-1][0]].count(2)==2 or C[P[-1][1]].count(2)==2):break
  W=[[c,P+[(k,l)]]for e in A(-1,2,2)for c in[(k+e,l),(k,l+e)]if 0<=c[0]<N and 0<=c[1]<N and d[c[0]][c[1]]!=8 if c not in P];J=[c for c in W if(c[0][0]==k if P[-1][0]==k else c[0][1]==l)];O+=[W,J][any(J)]
 return[[3 if(r,c)in P else d[r][c] for c in R]for r in R]