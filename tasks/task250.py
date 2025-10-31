def p(d):
 for _ in[0]*4:
  d=[*map(list,zip(*d[::-1]))];I,J=divmod(sum(d,[]).index(2),10);W=J+1
  for k in range(I*W+W):
   r=d[i:=k//W];R=d[I-1]
   if r[j:=k%W]>2:
    r[j]=0
    if i==I:r[J-1]=5
    if j==J:R[j]=5
    if i-I==j-J:R[J-1]=5
 return d