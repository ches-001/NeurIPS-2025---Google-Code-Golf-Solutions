def p(d,w=0):
 E=enumerate;W=len(d[0]);F=lambda a,c,i:[(k//W+i,k%W)for k,v in E(sum(a,[]))if v==c];S=sum(d,[]);d=eval(str(d).replace(str(([c for c in{*S}if S.count(c)<6]+[0])[0]),'0'))
 for i,r in E(d):
  if all(r):
   for(u,v)in F(d[:i],c:=r[0],0):d[u][v]=0;d[i-1][v]=c
   for(u,v)in F(d[i+1:],c,i+1):d[u][v]=0;d[i+1][v]=c
 d=[*map(list,zip(*d))];return d if w else p(d,w+1)