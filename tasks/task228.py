def p(d):
 for _ in[0]*4:d=[*map(list,zip(*d[::-1]))];(I,J,Y),(X,*_)=[(i,j:=r.index(m),j+c-1)for i in range(10)if len({*(r:=d[i])})==2<(c:=r.count(m:=max(r)))>3];d[I-1][J-1]=d[X-1][Y-1];d[X-1][Y-1]=0
 return d