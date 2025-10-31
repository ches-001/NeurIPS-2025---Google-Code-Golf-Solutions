def p(d):
 R=range(len(d));m=max(sum(d,[]));(A,I,X),J=zip(*[(i,j)for i in R for j in R if d[i][j]]);D=I-A;B=min(J);Y=B+D*2
 for _ in[0]*15:d=[[[d[i][j],m][i in[A,X]and B<=j<=Y or j in[B,Y]and A<=i<=X]for j in R]for i in R];A-=D;X+=D;B-=D;Y+=D
 return d