def p(d):
 L=len;R=range;C={};Z=lambda T,H:[[min,max][i>=2](T[i],H[i])for i in R(L(T))]
 for r in R(L(d)):
  for c in R(L(d[0])):v=d[r][c];s=(r,c)*2;C[v]=Z(C.get(v,s),s)
 w=C[min(C,key=lambda x:C[x][3]-C[x][1])];return[s[w[1]:w[3]+1]for s in d[w[0]:w[2]+1]]