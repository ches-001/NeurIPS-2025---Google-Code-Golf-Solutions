def p(o,p=enumerate,R=range):
 t={(n,a)for(n,t)in p(o)for(a,l)in p(t)if l}
 while t:
  a={n:[]for n in t}
  for m in R(363):
   k=m//3;l=m%3;h=k//11;f=k%11;n={(h+[n//2,n,0][l],f+[n%2,0,n][l])for n in R([4,3,3][l])}
   if n<=t:[a[t].append(n)for t in n]
  f=min(t,key=lambda n:len(a[n]));n=a[f][0];t-=n
  for(a,l)in n:o[a][l]=len(n)*6-16
 return o