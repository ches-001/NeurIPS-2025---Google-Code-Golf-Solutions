def p(d):
 for _ in[0]*2:
  d=[*map(list,zip(*d))]
  for t,r in enumerate(d):
   if len({*r})>2:a,b=filter(bool,r);w=r.index;i=w(a);x=w(b);e=(x-i-5)//2;z=i+e+1;l=x-e-1;r[i+1:i+e+2]=[a]*-~e;r[l:x]=[b]*-~e;d[t+1][z]=d[t-1][z]=a;d[t+1][l]=d[t-1][l]=b;d[t+2][z:x-e]=d[t-2][z:x-e]=[a,a,b,b];break
 return d