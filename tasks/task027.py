def p(d):
 R=range(10);V=[(i,j)for i in R for j in R if d[i][j]];A,*_,B=sorted(sum(V,()))
 for i,j in V:x=int(2*(A+B)/2-j);d[x][i]=2-d[x][i]
 return d