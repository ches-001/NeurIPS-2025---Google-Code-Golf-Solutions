def p(d):
 A=sum(d,[]);S=[*{*A}-{0,8}];H=len(d);W=len(d[0])
 def F(i,j,c):d[i][j]=c;[F(a,b,S[c==S[0]])for a,b in((i,j+1),(i,j-1),(i+1,j),(i-1,j))if 0<=a<H>0<=b<W and 8!=c!=0 and d[a][b]==0]
 for k in range(H*W):i=k//W;j=k%W;F(i,j,d[i][j])
 return d