def p(d,i=0):
 while i<len(d):
  if any(d[i]):r=d[i+1];s=r.index(max(r));r[s+1::2]=[0]*len(r[s+1::2]);i+=3
  else:i+=1
 return d