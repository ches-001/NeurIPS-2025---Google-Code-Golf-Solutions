def T(V):U=[*zip(*V)];x=(min(U[1])+max(U[1]))//2;y=(min(U[2])+max(U[2]))//2;return [*zip(*[((u,-c+y+x,r-x+y),(u,c-y+x,-r+x+y),(u,2*x-r,c))for u,r,c in V])]
def p(d):
 R=range;L=len;V=[];U=[];H=L(d);W=L(d[0]);E=[]
 for i in R(H):
  for j in R(W):
   if (c:=d[i][j]):
    O=[(c,i,j)];d[i][j]=0
    for v in O:O+=[((c,x,y),exec("d[x][y]=0"))[0]for a,b in[(0,-1),(0,1),(1,0),(-1,0)]if 0<=(x:=v[1]+a)<H>0<=(y:=v[2]+b)<W if(c:=d[x][y])]
    if len(O)>3:E+=[O];V+=O
    else:U+=O
 for O in E:
  for i in R(-H,H):
   for j in R(-W,W):
    Q=[(v[0],v[1]+i,v[2]+j)for v in O];B=T(Q);S=[I for I in B+T(B[0]) if len([v for v in I if v not in V and v in U])==3]
    if S:
     for u,r,c in S[0]:d[r][c]=u
 return d