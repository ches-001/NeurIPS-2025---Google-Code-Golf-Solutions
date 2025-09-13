def p(d):
 R=range(30);M={}
 for r in R:
  for c in R:M[d[r][c]]=M.get(d[r][c],[])+[(r,c)]
 A,B=zip(*[(r,c)for r in R for c in R if d[r][c]==min(M,key=lambda x:abs(M[x][0][0]-M[x][-1][0]))]);return[c[min(B):max(B)+1]for c in d[min(A):max(A)+1]]