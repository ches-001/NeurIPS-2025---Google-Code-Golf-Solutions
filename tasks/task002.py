def p(d):
 R=range(1,len(d)-1);O=[]
 for r in R:
  for c in R:
   if not d[r][c]:d[r][c]=4
 while O!=d:
  O=[i[:]for i in d]
  for r in R:
   for c in R:
    if d[r][c]==4 and not(d[r-1][c]and d[r+1][c]and d[r][c-1]and d[r][c+1]):d[r][c]=0
 return d