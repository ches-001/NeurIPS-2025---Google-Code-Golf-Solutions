def p(d):
 t={(l,n)for l in range(len(d))for n in range(len(d[0]))if d[l][n]&2};F=lambda a,l:[a and(F(a[1:],l)or not a[0]&l and F(a[1:],l|a[0])),l][t<=l]
 for n in 2,3:
  l=[l for z in range(len(d))for i in range(len(d[0]))for l in[{(l,n)for l in range(-n,n+1)for l,n in[(z+l,i),(z,i+l)]if len(d)>l>-1<n<len(d[0])}]if min(d[l][n]for l,n in l)&2]
  if l:=F(l,set()):
   for l,n in l:d[l][n]+=3*(d[l][n]&1)
   return d