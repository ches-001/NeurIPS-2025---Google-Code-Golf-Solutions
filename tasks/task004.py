def p(d,p=enumerate):
 a=[[0]*len(d[0])for _ in d]
 for q in{*sum(d,[])}:
  f=[(y,x)for y,r in p(d)for x,v in p(r)if v==q];k,l=map(max,zip(*f))
  for y,x in f:a[y][x+(y<k)*(x<l)]=q
 return a