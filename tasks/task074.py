def p(d,w=0):
 C=[*zip(*d)]
 for i in range(0,16):
  if i<2:C[i]=d[i]=[[a,b][a==9]for a,b in zip(d[i],C[i])]
  else:T=31-i;C[i]=d[i]=C[T]=d[T]=[min(*u)for u in zip(d[i],d[T],C[i],C[T])]
 return C if w else p(d,w+1)