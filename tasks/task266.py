def p(d):
 A=sum(d,[]).index(2);d[I:=A//5][J:=A%5]=0
 for k in range(4):
  x=I+2*(k//2)-1;y=J+2*(k%2)-1
  if 0<=x<3>0<=y<5:d[x][y]=[3,6,8,7][k]
 return d