def p(d):
 N=len(d);R=range(1,N)
 for i in R:d[i-1][N-i]=2;d[N-1][i]=4
 return d