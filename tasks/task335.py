def p(d,R=range):
 F=lambda c:next((i,r.index(c))for(i,r)in enumerate(d)if c in r);I,J=F(8);X,Y=F(2)
 for a in[R(X,I),R(I+1,X+1)][I<X]:d[a][J]=4
 for a in[R(Y+1,J),R(J,Y)][J<Y]:d[X][a]=4
 return d