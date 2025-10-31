def p(x):
 a=x;l,n=15,10
 g=lambda b:max(o:=sum(b,[]),key=o.count)
 def s(y,t):
  for u in range(9):
   i,m=y+1-u//3,t+1-u%3
   if n>m>=0<=i<l:yield i,m
 def i(b):
  o=b;u=g(o);n,k=15,10;m,d=set(),[]
  for t in range(n):
   for x in range(k):
    e=o[t][x]
    if e==u:continue
    r,l=set(),{(t,x)}
    while l:
     p=set()
     for(a,i)in l:
      y=o[a][i]
      if y==e:r.add((a,i));m.add((a,i));[p.add((o,a))for(o,a)in s(a,i)if k>a>=0<=o<n]
     l=p-m
    if r:d+=[(e,(*sorted(r),))]
  return d
 def m(e):return min(e)[0]
 def k(e):return min(e)[0],min(o for(a,o)in e)
 def r(y):a,o=y;i,m=k(o);return a,sorted((o-i,a-m)for(o,a)in o)
 def c(y,t):o,a=y;i,m=t;return o,sorted((o+i,a+m)for(o,a)in a)
 f=g(a);x=i(a);e={}
 for(d,o)in x:e[o]=d
 d=[(a,o)for(o,a)in e.items()]
 if not d:return[o[:]for o in a]
 t=sorted(d,key=lambda y:(m(y[1]),k(y[1])[1]));p=m(t[0][1]);x=p
 for y in range(p+1,l):
  if any(a[y][o]!=f for o in range(n)):x=y
  elif x>=p:break
 e,u=set(),t[0][0]
 for(d,o)in t:
  if m(o)<=x:e|={*o}
  else:break
 b=min(o for(o,a)in e);q=min(o for(a,o)in e);p=sorted((o-b,a-q)for(o,a)in e);e=u,p
 def r(l):
  a=None;e,o,i=[],a,-1
  for(n,t)in l:
   r=m(t)
   if r<=x:continue
   l=max(o for(o,a)in t)
   if o is a or r>i+1:
    if o is not a:e+=[(u,sorted(o))]
    o={*t};i=l
   else:o|={*t};i=max(i,l)
  if o is not a:e+=[(u,sorted(o))]
  return e
 t=r(t);y=[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)];b=[]
 for(d,o)in t:t=k(o);x=c(e,t);x=[set(c(x,o)[1])for o in y];d=set(o);p=[(o,len(o&d),min(o for(o,a)in o)if o else u('inf'))for o in x];m=max(p,key=lambda k:(k[1],-k[2]));g=max(o for(a,o)in o);b+=[(m[0]if m[1]>0 else d,g)]
 i=[o[:]for o in a]
 for(p,j)in b:
  for(y,r)in p:
   if r<=j:continue
   if 0<=y<l and 0<=r<n and i[y][r]==f:i[y][r]=1
 return i