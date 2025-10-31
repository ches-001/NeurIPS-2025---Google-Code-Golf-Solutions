def p(d,R=range(10)):
 W=[-1,*[i for i in R if all(d[i])],10];Q=[-1,*[j for j in R if d[0][j]],10]
 for t in[0,1,2]:w=t*len(W)//2-t;x,a=W[w:w+2];z=t*len(Q)//2-t;y,b=Q[z:z+2];d=[[[d[i][j],t+1][x<i<a>=-1<=y<j<b]for j in R]for i in R]
 return d