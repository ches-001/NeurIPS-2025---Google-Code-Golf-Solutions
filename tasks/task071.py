def p(d,A=range(16),H=len):
 Q=lambda v:{*[c for r in v for c in r]};D=[*zip(*d)]
 for i in A:
  for j in A:
   if v:=d[i][j]:
    J=15-d[i][::-1].index(v);w=(J-j)+1;F=w//2;C=-(w//-2);M=D[j+F:j+C];L=D[:j+F];R=D[j+C:]
    if(M and Q(M)!=Q(L))or H(Q(L))>2:q=H(L)-H(R);S=([[0]*16]*q+R[::-1]+M+R)[abs(min(0,q)):]
    else:S=(L+M+L[::-1]+[[0]*16]*(H(R)-H(L)))[:16]
    return [*map(list,zip(*S))]