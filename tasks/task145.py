def p(d,R=range):
 H,W=len(d),len(d[0]);U=[];T=R(-1,2);F=lambda i,j,V:W>j>=0<=i<H and d[i][j]<1 and(i,j)not in V and not V.add((i,j))and[F(i+a,j+b,V)for a in T for b in T]and V;O=[V for i in R(H)for j in R(W)if(i,j)not in U if(V:=F(i,j,set()))if(U:=U+[*V])];a,*_,z=sorted(map(len,O))
 for o in O:
  for i,j in o:l=len(o);d[i][j]=8**(l<z)*(l in[a,z])
 return d