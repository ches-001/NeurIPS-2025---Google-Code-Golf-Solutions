def p(d):
 for m in range(2916):
  k=m//9;s=m%9;i=k//18;j=k%18;w=4-s%3;x=i+4-s//3;y=j+w
  if x<=18>=y and sum(sum([r[j:y]for r in d[i:x]],[]))in[0,2]:
   for r in d[i:x]:r[j:y]=[2]*w
 return d