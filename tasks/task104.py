def p(d):
 z=[0];a=[[3]*4+z*5]*4+[z*4+[3]*4+z]*4+[z*9]
 for k in d[0][::2]+d[2][::2][::-1]:
  if k:return a
  a=[*zip(*a[::-1])]