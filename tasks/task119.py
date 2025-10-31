def p(d):
 for _ in[0]*4:
  d=[*map(list,zip(*d[::-1]))];I,J=divmod(sum(d,[]).index(8),12);a,b=[[-1,1][8 in d[0]],1]
  while d[0][11]==d[11][11]>0<=(I:=I+a)<12>(J:=J+b)>=0:d[I][J]=d[I][J]or 3;b=[b,-b][d[I][J+b]>0]
 return d