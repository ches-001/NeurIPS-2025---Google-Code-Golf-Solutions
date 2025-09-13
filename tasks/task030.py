def p(d):
 E=enumerate;M={};e=[[0]*len(i)for i in d]
 for i,r in E(d):
  for j,c in E(r):
   if c:M[c]=M.get(c,[])+[(i,j)]
 for k in M:
  for i,(r,c)in E(M[k]):e[M[1][i][0]][c]=k
 return e