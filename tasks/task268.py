def p(p):
 i=len(p);a=lambda p:[*map(list,zip(*p[::-1]))]
 for k in range(4):
  h=[(t,z)for t in range(i)for z in range(i)if p[t][z]];z,h=zip(*h);z,g,f,e=min(z),max(z),min(h),max(h);t=p[z][f];d=p[z].count(t)
  if d<p[g].count(t):
   h,m=f+d//2,e-d//2
   for t in range(g):p[t][h:m+1]=[4]*(m-h+1)
   for t in range(z+1,g):p[t][f+1:e]=[4]*(e-f-1)
   for u in range(z+1):
    t=z-u
    if h>=u:p[t][h-u]=4
    if m+u<i:p[t][m+u]=4
   for t in range(4-k):p=a(p)
   return p
  p=a(p)