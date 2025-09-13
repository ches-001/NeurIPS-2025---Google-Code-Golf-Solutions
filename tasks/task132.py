def p(d,R=range):
 M={};A=len(d);B=len(d[0])
 for i in R(A):
  for j in R(B):
   if c:=d[i][j]:V=M.get(c,[len(d),0,len(d[i]),0]);M[c]=[min(V[0],i),max(V[1]-1,i)+1,min(V[2],j),max(V[3]-1,j)+1]
 for c in M:
  for i in R(*M[c][:2]):
   for j in R(*M[c][2:]):d[i][j]=c
 return d