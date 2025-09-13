def p(d):
 H=len(d)-1;V=[]
 for k in range(H*H):
  i,j=k//H,k%H
  if d[i][j]==5 and(i,j)not in V:d[i-1][j-1:j+3]=[1,0,0,2];d[i+2][j-1:j+3]=[3,0,0,4];V+=[(i,j),(i,j+1),(i+1,j),(i+1,j+1)]
 return d