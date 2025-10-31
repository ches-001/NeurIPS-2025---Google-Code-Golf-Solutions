def p(d,R=range(10)):
 D=d
 for _ in[0]*4:A=sum(D:=[*zip(*D[::-1])],());I,J=divmod(A.index(m:=max(A)),10);d=[d:=[*zip(*d[::-1])],[[[d[i][j],m][I-i==J-j>0]for j in R]for i in R]][J+1<9>I+1>D[I][J+1]<D[I+1][J+1]]
 return d