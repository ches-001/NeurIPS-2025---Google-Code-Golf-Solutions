def p(d):
 for _ in[0]*4:F=lambda c:[i for i,r in enumerate(d)if c in r];d=[*zip(*d[::-1])];I=F(8)[0];X=F(2)[-1];d=[d,[[0]*len(d[0])]*(D:=I-X-1)+d[:X+1]+d[I:]][D>0]
 return d