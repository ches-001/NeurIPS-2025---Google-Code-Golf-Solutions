def p(d):
 for _ in[0]*4:d=[*zip(*d[::-1])];H=len(d);W=len(d[0]);F=lambda c:[i for i in range(H)if c in d[i]];X,*_=F(2);d=[d,[[0]*W]*(H-len(f:=[[8]*W]+d[min(I:=F(3)):max(I)+1]+d[X:]))+f][I[0]<X<H>W]
 return d