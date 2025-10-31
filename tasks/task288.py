def p(d):
 Q=len(d)//2;w=3
 for i in range(Q+1):
  if d[-2][Q-i]<1:d[-w][Q-i]=d[-w][Q+i]=d[-1][Q];w+=1
 return d