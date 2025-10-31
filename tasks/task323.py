def p(d):
 I,J=divmod(sum(d,[]).index(8),13);a=1;b=0
 for s in range(1,25):
  if I+a<13>J-b>=0:d[I+a][J-b]=5
  if I-a>=0<=J+b<13:d[I-a][J+b]=5
  a+=s%4<2;b+=s%4>1
 return d