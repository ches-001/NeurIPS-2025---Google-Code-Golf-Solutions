def p(d,Q=range):
 H=len(d);W=len(d[0]);A=sum(d,[]);S={*A};M=max(S,key=A.count);S-={M};D=[[M]*W for _ in d];R=[];C=[]
 for k in S:
  V=[(i,j)for i in Q(H)for j in Q(W)if d[i][j]==k]
  for i,j in V:a=H//2+i-(V[0][0]+V[-1][0])//2;b=W//2+j-(V[0][1]+V[-1][1])//2;D[a][b]=k;R+=[a];C+=[b]
 return[r[min(C):max(C)+1]for r in D[min(R):max(R)+1]]